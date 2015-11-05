from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

from django.views.generic import ListView

from pure_pagination.mixins import PaginationMixin

def index(request):
    return HttpResponse("World!")

def question(request, symbol_code):
    return HttpResponse("Hello!")
