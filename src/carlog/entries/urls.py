from django.conf.urls.defaults import patterns, url
from carlog.entries.views import car_index, car_details, treatment_index


urlpatterns = patterns('',
    url(r'^car/index/$', car_index),
    url(r'^car/(?P<id>\d+)/$', car_details),
    url(r'^car/(?P<id>\d+)/treatment/index/$', treatment_index),
)