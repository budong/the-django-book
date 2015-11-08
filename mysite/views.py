#!/usr/bin/env python
#coding: utf-8

from django.http import Http404,HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
    return HttpResponse("This is my homepage.")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body> %s </body></html>" % now
#    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date': now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    #assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s),it will be %s. </body></html>" % (offset,dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('request_meta.html',{'values': values})
