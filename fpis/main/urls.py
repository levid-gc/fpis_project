from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    'main',
    url(r'^ajax/add/$', 'ajax.add_todo'),
    url(r'^ajax/more/$', 'ajax.more_todo'),
    url(r'', TemplateView.as_view(template_name='main/index.html')),
)
