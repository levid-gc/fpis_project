# -*- coding: utf-8 -*-

# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect


from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# app specific files

from .models import Team
from .forms import *

from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm, password_change


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='account/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('login'))


def reset(request):
    return password_reset(request, template_name='account/password_reset_form.html',
        email_template_name='account/password_reset_email.html',
        subject_template_name='account/password_reset_subject.txt',
        post_reset_redirect=reverse('login'))


def change(request):
    return password_change(request, template_name='account/password_change_form.html', post_change_redirect=reverse('login'))



def introduction(request):
    #template_var = {"w": u"欢迎您 游客!"}
    #if request.user.is_authenticated():
        #template_var["w"] = u"欢迎您 %s!" % request.user.username
    t = get_template('home/introduction.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def index(request):
    #template_var = {"w": u"欢迎您 游客!"}
    #if request.user.is_authenticated():
        #template_var["w"] = u"欢迎您 %s!" % request.user.username
    return render(request, "home/index.html", {})


def register(request):
    """注册视图"""
    template_var = {}
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            _login(request, username, password)#注册完毕 直接登陆
            return HttpResponseRedirect(reverse("index"))
    template_var["form"] = form
    return render_to_response("account/register.html", template_var, context_instance=RequestContext(request))


def _login(request,username,password):
    '''''登陆核心方法'''
    ret = False
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            auth_login(request, user)
            ret = True
        else:
            pass
    else:
        pass
    return ret


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "home/login.html")


def logout(request):
    """ User Logout """
    auth_logout(request)
    return redirect(reverse('index'))

@login_required(login_url='/login/')
def homepage(request):
    user = request.user
    t = get_template('dashboard.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))





def create_team(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TeamForm()

    t = get_template('account/create_team.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_team(request):
  
    list_items = Team.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('account/list_team.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_team(request, id):
    team_instance = Team.objects.get(id = id)

    t=get_template('account/view_team.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_team(request, id):

    team_instance = Team.objects.get(id=id)

    form = TeamForm(request.POST or None, instance = team_instance)

    if form.is_valid():
        form.save()

    t=get_template('account/edit_team.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
