from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.Prestamos, name= 'prestamos'),
]