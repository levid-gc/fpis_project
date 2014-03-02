
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .models import Team
from account import views

urlpatterns = patterns(
    '',
    #url(r'^index$', views.index, name="index"),
    #url(r'^account/index$', views.index, name="accounts_index"),
    #url(r'^account/register$', views.register, name="register"),
    #url(r'^account/login$', views.login, name="login"),
    #url(r'^account/logout$', views.logout, name="logout"),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.reset_confirm, name='password_reset_confirm'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^change/$', views.change, name='change'),
    url(r'intro$', TemplateView.as_view(template_name='home/introduction.html'), name='intro'),
    url(r'homepage/$', views.homepage, name='homepage'),
    url(r'team/create/$', views.create_team),
    url(r'team/list/$', views.list_team ),
    url(r'team/edit/(?P<id>[^/]+)/$', views.edit_team),
    url(r'team/view/(?P<id>[^/]+)/$', views.view_team),
    
)
