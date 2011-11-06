from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from django.views.generic.simple import redirect_to
from carlog.main import carlog_main, auth_page, search_page,test_auth_page


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/$', search_page),
    url(r'^social/', include('socialregistration.urls', namespace = 'socialregistration')),
    url(r'^accounts/auth/$', test_auth_page),                       
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^tree/', include('carlog.fangorn.urls')),
    url(r'^entries/', include('carlog.entries.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', carlog_main),
    
)
