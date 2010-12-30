from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'main.views.home'),
    (r'^contest/$', 'main.views.contest_index'),
    (r'^contest/problem/(?P<problem_id>\d+)/$', 'main.views.problem_detail'),
    (r'^contest/problem/(?P<problem_id>\d+)/input/(?P<testcase_id>\d+)/testinput.in$', 'main.views.problem_input'),
    (r'^contest/problem/(?P<problem_id>\d+)/output/(?P<testcase_id>\d+)/testoutput.out$', 'main.views.problem_output'),
    (r'^about/$', 'main.views.about'),                       
    (r'^error/$', direct_to_template , {'template':'main/error.html'}),
    #(r'^page/$', 'main.views.page'),
    #(r'^(?P<var>\d+)/$', 'main.views.page_with_var'),
)
