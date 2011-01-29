from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('ticket.views',
                       (r'^new/$', 'submit_ticket'),
                       (r'^$', 'list_tickets'),
                       (r'^(?P<id>\d+)/$', 'show_ticket'),
                       (r'^mark-solved/(?P<id>\d+)/$', 'mark_solved'),
                       )
