
from django.conf.urls import patterns, url
from .models import Record
from .views import *

urlpatterns = patterns('',

    (r'record/create/$', create_record),
    (r'record/list/$', list_record ),
    (r'record/edit/(?P<id>[^/]+)/$', edit_record),
    (r'record/view/(?P<id>[^/]+)/$', view_record),
    
)
