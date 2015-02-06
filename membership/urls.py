from django.conf.urls import patterns, url, include
from membership.views import MemberListView, MemberDetailView, \
    MemberUpdateView, MemberFormView, MemberListTableView

urlpatterns = patterns('',
    url(r'^/members$', MemberListView.as_view(), name="members"),
    url(r'^/members/list_table$', MemberListTableView.as_view(), name="member_list_table"),
    url(r'^/members/add$', MemberFormView.as_view(), name="member_add"),
    url(r'^/members/(?P<pk>[0-9]+)', include([
        url(r'^[/]$', MemberDetailView.as_view(), name="member_detail"),
        url(r'/edit$', MemberUpdateView.as_view(), name="member_edit"),
    ]))
)
