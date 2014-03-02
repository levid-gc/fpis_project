from django.conf.urls import patterns, url

urlpatterns = patterns(
    'contact.views',
    #url(r'', 'contact', name='contact'),
    url(r'suggestion/$', 'suggestion', name='suggestion'),
)
