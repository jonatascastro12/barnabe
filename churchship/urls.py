from django.conf.urls import patterns, url, include
from churchship.views import ChurchListView, ChurchFormView, \
    ChurchChildListTableView, ChurchUpdateView, ChurchDetailView

urlpatterns = patterns('',
    url(r'^/church$', ChurchListView.as_view(), name="church"),
    url(r'^/church/list_table$', ChurchChildListTableView.as_view(), name="church_list_table"),
    url(r'^/church/child_add$', ChurchFormView.as_view(), name="church_child_add"),
    url(r'^/church/(?P<pk>[0-9]+)', include([
        url(r'^[/]$', ChurchDetailView.as_view(), name="church_detail"),
        url(r'/edit$', ChurchUpdateView.as_view(), name="church_edit"),
    ]))
)
