from django.urls import path
from . import views

urlpatterns = [
    path('homebanking/', views.homebanking, name="homebanking"),
    path('conversor/', views.conversor, name="conversor"),
    path('gastos/', views.gastos, name="gastos"),
]