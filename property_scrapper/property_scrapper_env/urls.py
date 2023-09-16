from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_record),
    path('get/', views.get_records)
]