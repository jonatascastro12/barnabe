import imghdr
import json
import os
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from barnabe import errors
from barnabe.settings import MEDIA_ROOT, MEDIA_URL
from barnabe.views import DashboardListView, DashboardDetailView, DashboardFormView, DashboardUpdateView
from membership import models
from membership.forms import MemberForm, PersonForm, PersonContactForm, PersonMainForm


class MemberListView(DashboardListView):
    queryset = models.Member.objects.all()
    paginate_by = 25

class MemberListTableView(ListView, BaseDatatableView):
    model = models.Member
    columns = ['id', 'person.name', 'memberFunction.name']
    order_columns = ['id', 'person.name', 'memberFunction.name']

    def filter_queryset(self, qs):
        """ If search['value'] is provided then filter all searchable columns using istartswith
        """
        if not self.pre_camel_case_notation:
            # get global search value
            search = self.request.GET.get('search[value]', None)
            col_data = self.extract_datatables_column_data()
            q = Q()
            for col_no, col in enumerate(col_data):
                # apply global search to all searchable columns
                if search and col['searchable']:
                    if '.' in self.columns[col_no]:
                        self.columns[col_no] = self.columns[col_no].replace('.', '__')
                    q |= Q(**{'{0}__istartswith'.format(self.columns[col_no]): search})

                # column specific filter
                if col['search.value']:
                    qs = qs.filter(**{'{0}__istartswith'.format(self.columns[col_no]): col['search.value']})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        """ Renders a column on a row
        """
        if '__' in column:
            column = column.replace('__', '.')

        if hasattr(row, 'get_%s_display' % column):
            # It's a choice field
            text = getattr(row, 'get_%s_display' % column)()
        else:
            try:
                text = getattr(row, column)
            except AttributeError:
                obj = row
                for part in column.split('.'):
                    if obj is None:
                        break
                    obj = getattr(obj, part)

                text = obj

        if hasattr(row, 'get_absolute_url'):
            return '<a href="%s">%s</a>' % (row.get_absolute_url(), text)
        else:
            return text


class MemberDetailView(DashboardDetailView):
    model = models.Member

class MemberFormView(DashboardFormView):
    template_name = "membership/member_form.html"
    form_class = MemberForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        member_form = self.get_form(form_class)
        person_form = PersonForm(request.POST, request.FILES)

        if member_form.is_valid() and person_form.is_valid():
            return self.form_valid(member_form)
        else:
            return self.form_invalid(member_form)

    def form_valid(self, form):
        person_form = PersonForm(self.request.POST, self.request.FILES)
        person_form.instance.photo = person_form.data['photo']
        person_form.save()
        form.instance.person = person_form.instance
        form.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(MemberFormView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['person_form'] = PersonMainForm(self.request.POST, self.request.FILES)
            context['person_contact_form'] = PersonContactForm(self.request.POST)
        else:
            context['person_form'] = PersonMainForm()
            context['person_contact_form'] = PersonContactForm()

        context['media_css'] += context['form'].media['css']
        context['media_js'] += context['form'].media['js']

        context['media_css'] += context['person_form'].media['css']
        context['media_js'] += context['person_form'].media['js']

        return context

class MemberUpdateView(DashboardUpdateView):
    model = models.Member
    form_class = MemberForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form_class = self.get_form_class()
        member_form = self.get_form(form_class)
        person_form = PersonForm(request.POST, request.FILES)

        if member_form.is_valid() and person_form.is_valid():
            return self.form_valid(member_form)
        else:
            return self.form_invalid(member_form)

    def form_valid(self, form):
        person_form = PersonForm(self.request.POST, instance=form.instance.person)
        form.save()
        form.instance.person.photo = person_form.data['photo']
        form.instance.person.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(DashboardUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['person_form'] = PersonMainForm(self.request.POST, self.request.FILES)
            context['person_contact_form'] = PersonContactForm(self.request.POST, self.request.FILES)
        else:
            context['person_form'] = PersonMainForm(instance=self.object.person)
            context['person_contact_form'] = PersonContactForm(instance=self.object.person)

        context['media_css'] += context['form'].media['css']
        context['media_js'] += context['form'].media['js']

        context['media_css'] += context['person_form'].media['css']
        context['media_js'] += context['person_form'].media['js']

        return context

def image_upload(request):
    person = PersonForm(request)
    if request.POST and 'photo_crop_data' in request.POST and 'photo_original' in request.POST:

        im = Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), request.POST['photo_original'].lstrip('/').replace('/','\\')))

        crop_data = json.loads(request.POST['photo_crop_data'])
        img_ratio = im.size[0]/float(crop_data["bounds"][0])

        crop_params = (int(round(crop_data['selectionPosition']['left']*img_ratio)),
                       int(round(crop_data['selectionPosition']['top']*img_ratio)),
                       int(round(crop_data['selectionPosition']['left']*img_ratio))+int(round(crop_data['selectionSize']*img_ratio)),
                       int(round(crop_data['selectionPosition']['top']*img_ratio))+int(round(crop_data['selectionSize']*img_ratio))
        )

        thumb_posfix = '_thumb_512'

        original_name, extension = os.path.splitext(im.filename)
        cropped_img = im.crop(crop_params)
        cropped_img.thumbnail((512, 512), Image.ANTIALIAS)
        cropped_img.save(original_name + thumb_posfix + extension)

        filename = os.path.splitext(os.path.split(im.filename)[1])[0]
        newfilename = filename + thumb_posfix + extension

        return HttpResponse(os.path.join(os.path.join(MEDIA_URL, person.instance.photo.field.upload_to), newfilename))


    if request.FILES and 'photo' in request.FILES:
        upload_full_path = os.path.join(MEDIA_ROOT, person.instance.photo.field.upload_to)

        if not os.path.exists(upload_full_path):
            os.makedirs(upload_full_path)
        upload = request.FILES['photo']
        original_name, extension = os.path.splitext(upload.name)
        f = NamedTemporaryFile(mode='w+b')
        upload.name = str(original_name) + '_' + os.path.split(f.name)[1] + str(extension)

        while os.path.exists(os.path.join(upload_full_path, upload.name)):
            f = NamedTemporaryFile(mode='w+b')
            upload.name = str(original_name) + '_' + os.path.split(f.name)[1] + str(extension)

        dest = open(os.path.join(upload_full_path, upload.name), 'wb')

        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()

        try:
            ext = imghdr.what(os.path.join(upload_full_path, upload.name))
            if ext not in ('jpeg', 'jpg', 'png'):
                return HttpResponse(status=406, content=errors.ImageNotJpgOrPngError().response_error())
            im = Image.open(os.path.join(upload_full_path, upload.name))
            if (im.size <= (512,512)):
                return HttpResponse(status=406, content=errors.ImageLessThan512().response_error())
        except IOError:
            return HttpResponse(status=406, content=errors.ImageNotRecognized().response_error())

        return HttpResponse(os.path.join(os.path.join(MEDIA_URL, person.instance.photo.field.upload_to), upload.name))
    return HttpResponse(status=405, content_type='application/json', content=errors.GetRequestNotPermitted.response_error())

def memberfunction(request):
    return HttpResponse(200)

def members(request):
    return HttpResponse(200)

def retrieve(request, member_id):
    return HttpResponse(200)

def edit(request, member_id):
    return HttpResponse(200)
