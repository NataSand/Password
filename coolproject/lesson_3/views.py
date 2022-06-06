from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
menu = [{'priority': 100, 'task': 'Составить список дел'},
              {'priority': 150, 'task': 'Изучать Django'},
              {'priority': 1, 'task': 'Подумать о смысле жизни'}]

def index(request):
    posts = Lesson_3.objects.all()
    return render(request, 'lesson_3/index.html', {'posts': posts, 'menu': menu,
                                                   'title': 'Главная страница'})
    #'<h2><font color="green">Welcome to site l}esson_3!</font></h2>'


def about(request):
    return render(request, 'lesson_3/about.html', {'menu': menu,
                                                   'title': 'О сайте'})


def something(request):
    response = HttpResponse('Вот ваш файл')
    response.status = 227
    return response

