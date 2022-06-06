from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'', views.product_list, name='product_list'),
    re_path(r'shop/categories/(?P<id>\d+)/(?P<slug>[-\w]+)/', views.product_list,
         name='product_list_by_category'),

    re_path(r'product/(?P<id>\d+)/(?P<slug>[-\w]+)/', views.product_detail,

         name='product_detail'),
]
