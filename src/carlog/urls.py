from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout


from carlog.entries.views import car_index, car_details, treatment_index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^carlog/car/index/', car_index),
    url(r'^carlog/car/(?P<id>\d+)/$', car_details),
    url(r'^carlog/car/(?P<id>\d+)/treatment/index/$', treatment_index),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
