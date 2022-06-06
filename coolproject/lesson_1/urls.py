from django.urls import path
from .views import *

urlpatterns = [
    path('', show),  # http://127.0.0.1:8000/lesson_1/
    path('top/', topics), # http://127.0.0.1:8000/lesson_1/top/
    path('lesson_1_1/', web)  # http://127.0.0.1:8000/lesson_1/top/

]
