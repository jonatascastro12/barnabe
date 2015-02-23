from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
import six
import json
from barnabe.utils import MESSAGES
from barnabe.views import DashboardListView, DashboardDetailView, DashboardFormView, DashboardUpdateView
from membership import models
from membership.forms import MemberForm, PersonForm
from membership.models import Member, Person


class MemberListView(DashboardListView):
    queryset = models.Member.objects.all()
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        if 'layout' in self.request.GET:
            context['layout'] = self.request.GET['layout']
        return context

    def delete(self, request):
        if (isinstance(request.body, six.string_types)):
            data = json.loads(request.body)
            ids = data['id']
            try:
                selected_members = Member.objects.filter(id__in=ids).all()
                person_ids = []
                for m in selected_members:
                    person_ids.append(m.id)
                Person.objects.filter(id__in=person_ids).delete()
                selected_members.delete()
                messages.success(self.request, MESSAGES['success']['member_remove'])
                return HttpResponse(status=200)
            except:
                return HttpResponse(status=401)


class MemberListTableView(ListView, BaseDatatableView):
    model = models.Member
    columns = ['id', 'person.name', 'member_function']
    order_columns = ['id', 'person.name', 'member_function']

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
        text = '<span attr_name="%s">%s</span>' % (column, text)
        if hasattr(row, 'get_absolute_url'):
            return '<a obj_id="%s" href="%s">%s</a>' % (row.id, row.get_absolute_url(), text)
        else:
            return text


class MemberDetailView(DashboardDetailView):
    model = models.Member

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        return context

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
        person_form.save()
        form.instance.person = person_form.instance
        form.save()
        messages.success(self.request, MESSAGES['success']['member_add'])
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(MemberFormView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['person_form'] = PersonForm(self.request.POST, self.request.FILES)
        else:
            context['person_form'] = PersonForm()

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
        person_form = PersonForm(request.POST or None, request.FILES or None)

        if member_form.is_valid() and person_form.is_valid():
            return self.form_valid(member_form, person_form)
        else:
            return self.form_invalid(member_form)

    def form_valid(self, form, person_form):
        form.save()
        person_form.instance.pk = form.instance.person.pk
        person_form.save()
        messages.success(self.request, MESSAGES['success']['member_update'])
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(DashboardUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['person_form'] = PersonForm(self.request.POST, self.request.FILES)
        else:
            context['person_form'] = PersonForm(instance=self.object.person)

        context['media_css'] += context['form'].media['css']
        context['media_js'] += context['form'].media['js']

        context['media_css'] += context['person_form'].media['css']
        context['media_js'] += context['person_form'].media['js']

        return context

def remove_members(request):
    if request.POST:

        return HttpResponse(200)
    if request.GET:
        return HttpResponseRedirect(reverse('members'))

def memberfunction(request):
    return HttpResponse(200)

def members(request):
    return HttpResponse(200)

def retrieve(request, member_id):
    return HttpResponse(200)

def edit(request, member_id):
    return HttpResponse(200)
