from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.shortcuts import render
from django.db import models
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse("hello world!!!")
