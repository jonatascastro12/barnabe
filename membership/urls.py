from django.conf.urls import patterns, url, include
from membership.views import MemberListView, MemberDetailView, \
    MemberUpdateView, MemberFormView, image_upload, MemberListTableView

urlpatterns = patterns('',
    url(r'^/members$', MemberListView.as_view(), name="member"),
    url(r'^/members/list_table$', MemberListTableView.as_view(), name="member_list_table"),
    url(r'^/members/add$', MemberFormView.as_view(), name="member_add"),
    url(r'^/members/image_upload', image_upload, name="member_image_upload"),
    url(r'^/members/(?P<pk>[0-9]+)', include([
        url(r'^[/]$', MemberDetailView.as_view(), name="member_detail"),
        url(r'/edit$', MemberUpdateView.as_view(), name="member_edit"),
    ]))
)
