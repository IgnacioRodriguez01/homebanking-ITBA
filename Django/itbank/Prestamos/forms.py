from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

class PrestamoForm(forms.Form):
    tipo = forms.ChoiceField(label = 'Prestamo')
    fecha = forms.DateField(label = 'Fecha de inicio')
    monto = forms.FloatField(label = 'Monto')

def contact(request): 
    prestamo_form = PrestamoForm
    if request.method == "POST":
        if prestamo_form.is_valid():
            tipo = request.POST.get('tipo',"")
            fecha = request.POST.get('tipo',"")
            monto = request.POST.get('tipo',"")
            ##esto es para que muestre los datos en pantalla
            return redirect(reverse('Prestamos')+"?ok")
