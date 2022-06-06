from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/lesson_3/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/lesson_3/
    path('answer/', something, name='answer'),  # http://127.0.0.1:8000/lesson_3/
]