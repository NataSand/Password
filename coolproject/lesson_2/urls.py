from django.urls import path, re_path
from .views import *

urlpatterns = [
    path(r'home/', home, name='home-views'),  # http://127.0.0.1:8000/lesson_2/
    #path(r'book/<int:num>/', title, name='book'),
    re_path(r'title/(?P<num>\w+)/', bk, name='book'),
    path(r'index/', index, name='‘index-view'),
    re_path(r'username/(?P<nic>\w+)/', bio, name='bio'),
    path('', show2),  # http://127.0.0.1:8000/lesson_2/
]

