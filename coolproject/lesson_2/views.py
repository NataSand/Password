from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Home page!!!")


def bk(request, num):
    return HttpResponse(f'<h1>CHAPTER TITLE<h1><p>{num}<p>')


def index(request):
    return HttpResponse("Index page!!!")


def bio(request, nic):
    return HttpResponse(f'<h1>USERNAME<h1><p>{nic}<p>')


def show2(request):
    return HttpResponse('<h2><font color="red">Welcome to site lesson_2!</font></h2>')
