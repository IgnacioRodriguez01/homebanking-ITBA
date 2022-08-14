from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def homebanking(request):
    return render(request, 'Homebanking/homebanking.html')

def gastos(request):
    return render(request, 'Homebanking/gastos.html')

def conversor(request):
    return render(request, 'Homebanking/conversor.html')