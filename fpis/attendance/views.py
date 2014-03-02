
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_record(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RecordForm()

    t = get_template('attendance/create_record.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_record(request):
  
    list_items = Record.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('attendance/list_record.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_record(request, id):
    record_instance = Record.objects.get(id = id)

    t=get_template('attendance/view_record.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_record(request, id):

    record_instance = Record.objects.get(id=id)

    form = RecordForm(request.POST or None, instance = record_instance)

    if form.is_valid():
        form.save()

    t=get_template('attendance/edit_record.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
