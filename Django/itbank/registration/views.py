from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def register(request):
    return render(request, 'registration/register.html')