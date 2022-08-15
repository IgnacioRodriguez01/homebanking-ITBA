from django.shortcuts import render
from .forms import PrestamoForm

# Create your views here.

def Prestamos(request):
    prestamo_form = PrestamoForm
    return render(request,'Prestamos/Prestamos.html',{'form':prestamo_form})