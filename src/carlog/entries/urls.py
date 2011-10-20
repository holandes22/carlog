from django.conf.urls.defaults import patterns, url
from carlog.entries.views import mobile_test
from carlog.entries.views import car_details, car_summary, car_editor
from carlog.entries.views import mechanic_details, mechanic_summary, mechanic_editor
from carlog.entries.views import treatment_details, treatment_summary, treatment_editor


urlpatterns = patterns('',
    url(r'^car/(?P<id>\d+)/editor/$|^car/editor/$', car_editor),
    url(r'^car/summary/$', car_summary),
    url(r'^car/(?P<id>\d+)/details/$', car_details),
    url(r'^mechanic/(?P<id>\d+)/editor/$|^mechanic/editor/$', mechanic_editor),
    url(r'^mechanic/summary/$', mechanic_summary),
    url(r'^mechanic/(?P<id>\d+)/details/$', mechanic_details),
    url(r'^treatment/(?P<id>\d+)/editor/$|^treatment/editor/$', treatment_editor),
    url(r'^treatment/car/(?P<car_id>\d+)/summary/$', treatment_summary),
    url(r'^treatment/(?P<id>\d+)/details/$', treatment_details),
    url(r'^car/mobile_test/$', mobile_test),
)