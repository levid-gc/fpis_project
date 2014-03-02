# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()
#import xadmin
#xadmin.autodiscover()



urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    url(r'^index/$', 'account.views.index', name='index'),
    url(r'^login/$', 'account.views.login', name='login'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^homepage/$', 'account.views.homepage', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
)

urlpatterns += patterns ('',

)

urlpatterns += patterns ('',
 (r'^schedule/', include('schedule.urls')),
)

urlpatterns += patterns ('',
 (r'^attendance/', include('attendance.urls')),
)

urlpatterns += patterns ('',
 (r'^api/', include('api.urls')),
)

urlpatterns += patterns ('',
 (r'^contact/', include('contact.urls')),
)

urlpatterns += patterns ('',
 (r'^main/', include('main.urls')),
)



urlpatterns += patterns ('',
 (r'^account/', include('account.urls')),
)

urlpatterns += patterns ('',
 (r'^schedule/', include('schedule.urls')),
)

urlpatterns += patterns ('',
 (r'^attendance/', include('attendance.urls')),
)

urlpatterns += patterns ('',
 (r'^schedule/', include('schedule.urls')),
)
