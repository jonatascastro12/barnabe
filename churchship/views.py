from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect

# Create your views here.
from django.views.generic.list import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from barnabe.views import DashboardUpdateView, DashboardListView, DashboardFormView, DashboardDetailView
from churchship import models
from churchship.forms import ChurchForm


class ChurchListView(DashboardListView):
    paginate_by = 25

    def get_queryset(self):
        return models.Church.objects.filter(barnabeuserchurch__barnabe_user__user=self.request.user, is_mother=False)

    def get_context_data(self, **kwargs):
        context = super(ChurchListView, self).get_context_data(**kwargs)
        context['main_church'] = models.Church.objects.get(barnabeuserchurch__barnabe_user__user=self.request.user, is_mother=True)

        return context

class ChurchDetailView(DashboardDetailView):
    model = models.Church

class ChurchChildListTableView(ListView, BaseDatatableView):
    model = models.Church
    columns = ['id', 'name']
    order_columns = ['id', 'name']

    def get_initial_queryset(self):
        main_church = models.Church.objects.get(barnabeuserchurch__barnabe_user__user=self.request.user, is_mother=True)
        return self.model.objects.filter(church_mother=main_church, is_mother=False)

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

class ChurchFormView(DashboardFormView):
    template_name = "membership/church_form.html"
    form_class = ChurchForm

    def form_valid(self, form):
        church_form = ChurchForm(self.request.POST, self.request.FILES)
        church_form.instance.photo = church_form.data['photo']
        church_form.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(ChurchFormView, self).get_context_data(**kwargs)

        context['media_css'] += context['form'].media['css']
        context['media_js'] += context['form'].media['js']

        context['media_css'] += context['person_form'].media['css']
        context['media_js'] += context['person_form'].media['js']

        return context

class ChurchUpdateView(DashboardUpdateView):
    model = models.Church
    form_class = ChurchForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(DashboardUpdateView, self).get_context_data(**kwargs)

        context['media_css'] += context['form'].media['css']
        context['media_js'] += context['form'].media['js']

        return context
