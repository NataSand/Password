from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h2><font color="blue">Welcome to site lesson_11!</font></h2>')
