from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    return HttpResponse('Hello Django!')

def question(request, symbol_code):
    q = Question.objects.get(symbol_code=symbol_code)
    return HttpResponse(q.question_text)
