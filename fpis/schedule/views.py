
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

# app specific files

from models import *
from forms import *


def create_term(request):
    form = TermForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TermForm()

    t = get_template('schedule/create_term.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_term_single(request):
    form = CreateTermForm(request.POST or None)
    if form.is_valid():
        pass

    t = get_template('schedule/Term/create_term.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))



def list_term(request):
  
    list_items = Term.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('schedule/list_term.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_term(request, id):
    term_instance = Term.objects.get(id = id)

    t=get_template('schedule/view_term.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_term(request, id):

    term_instance = Term.objects.get(id=id)

    form = TermForm(request.POST or None, instance = term_instance)

    if form.is_valid():
        form.save()

    t=get_template('schedule/edit_term.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CourseForm()

    t = get_template('schedule/create_course.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


@login_required(login_url='/login/')
def create_course_single(request):
    """
    Designed just for teachers and students.
    """
    t = get_template('base.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))



def list_course(request):
  
    list_items = Course.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('schedule/list_course.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_course(request, id):
    course_instance = Course.objects.get(id = id)

    t=get_template('schedule/view_course.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_course(request, id):

    course_instance = Course.objects.get(id=id)

    form = CourseForm(request.POST or None, instance = course_instance)

    if form.is_valid():
        form.save()

    t=get_template('schedule/edit_course.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
