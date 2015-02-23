from django.conf.urls import patterns, url, include
from barnabe_admin.views import BarnabeUserListView, BarnabeUserListTableView, BarnabeUserFormView, \
    BarnabeUserDetailView, BarnabeUserUpdateView

urlpatterns = patterns('',
    url(r'^/barnabeusers$', BarnabeUserListView.as_view(), name="barnabeusers"),
    url(r'^/barnabeusers/list_table$', BarnabeUserListTableView.as_view(), name="barnabeuser_list_table"),
    url(r'^/barnabeusers/add$', BarnabeUserFormView.as_view(), name="barnabeuser_add"),
    url(r'^/barnabeusers/(?P<pk>[0-9]+)', include([
        url(r'^[/]$', BarnabeUserDetailView.as_view(), name="barnabeuser_detail"),
        url(r'/edit$', BarnabeUserUpdateView.as_view(), name="barnabeuser_edit"),
    ]))
)
