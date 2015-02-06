from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from . import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barnabe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', 'barnabe.views.logout', name='logout'),
    url(r'^dashboard/overview$', 'barnabe.views.dashboard', name="dashboard_index"),
    url(r'^dashboard/profile$', 'barnabe.views.profile', name="user_profile"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/image_upload', 'barnabe.views.image_upload', name="image_upload"),
    url(r'^dashboard/membership', include('membership.urls'),),
    url(r'^dashboard/churchship', include('churchship.urls'),),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^uploaded_images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )