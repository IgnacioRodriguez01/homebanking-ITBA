from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def homebanking(request):
    return render(request, 'Homebanking/homebanking.html')

@login_required
def gastos(request):
    return render(request, 'Homebanking/gastos.html')

@login_required
def conversor(request):
    return render(request, 'Homebanking/conversor.html')