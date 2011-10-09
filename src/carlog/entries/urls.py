from django.conf.urls.defaults import patterns, url
from carlog.entries.views import car_details, treatment_index, mobile_test, car_summary, car_editor


urlpatterns = patterns('',
    url(r'^car/(?P<id>\d+)/editor/$|^car/editor/$', car_editor),
    url(r'^car/summary/$', car_summary),
    url(r'^car/(?P<id>\d+)/details/$', car_details),
    url(r'^car/(?P<id>\d+)/treatment/index/$', treatment_index),
    url(r'^car/mobile_test/$', mobile_test),
)