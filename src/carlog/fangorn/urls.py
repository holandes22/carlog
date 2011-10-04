from django.conf.urls.defaults import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from carlog.fangorn.views import get_tree_nodes, get_car_tree_nodes, get_mechanic_tree_nodes

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'get_tree_nodes/$', get_tree_nodes),
    url(r'get_car_tree_nodes/$', get_car_tree_nodes),
    url(r'get_mechanic_tree_nodes/$', get_mechanic_tree_nodes),
)

from carlog.settings import DEBUG
if DEBUG:
    urlpatterns += staticfiles_urlpatterns()