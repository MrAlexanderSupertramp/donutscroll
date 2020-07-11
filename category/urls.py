from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^panel/category/list/$', views.category_list, name='category_list'),
    url(r'^panel/category/add/$', views.category_add, name='category_add'),
    url(r'^panel/category/edit/(?P<pk>\d+)$', views.category_edit, name='category_edit'),
    url(r'^panel/category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete'),
]