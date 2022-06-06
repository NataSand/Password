from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def show(request):
    return HttpResponse("Hello, Django!!! Wonderful action!!! SUCCESSFUL!!!")


def topics(request):
    return HttpResponse("<h1>MAIN TOPICS</h1>")


def web(request):
    return HttpResponse('<p>Hello World!</p>\n'
                        '<p>Django is one of the best framework on '
                        'Python</p>\n'
                        '<hr>')
