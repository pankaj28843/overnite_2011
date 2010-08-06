from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'main.views.home'),
    (r'^submission/(?P<sub_id>\d+)/$', 'main.views.result'),                       
    (r'^error/$', direct_to_template , {'template':'main/error.html'}),
    #(r'^page/$', 'main.views.page'),
    #(r'^(?P<var>\d+)/$', 'main.views.page_with_var'),
)
