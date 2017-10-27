from django.shortcuts import render

# Create your views here.
from blog.models import *
from django.template import loader, Context
from django.http import HttpResponse
from blog import blog


def archive(request):  
    posts = blog.objects.all()
    t = loader.get_template('archive.html')  
    c = Context({'posts':posts})  
    return HttpResponse(t.render(c))