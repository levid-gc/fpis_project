
from django.conf.urls import patterns, url
from models import *
from views import *

urlpatterns = patterns('',

    (r'term/create/$', create_term_single),
    (r'term/list/$', list_term ),
    (r'term/edit/(?P<id>[^/]+)/$', edit_term),
    (r'term/view/(?P<id>[^/]+)/$', view_term),
    
    (r'course/create/$', create_course),
    (r'course/list/$', list_course ),
    (r'course/edit/(?P<id>[^/]+)/$', edit_course),
    (r'course/view/(?P<id>[^/]+)/$', view_course),

    url(r'course/create/single$', create_course_single, name='create_course_single'),
    
)
