from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^entries/', include('carlog.entries.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
