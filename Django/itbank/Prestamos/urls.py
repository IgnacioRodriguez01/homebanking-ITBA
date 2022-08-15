from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Prestamos, name= 'prestamos'),
]