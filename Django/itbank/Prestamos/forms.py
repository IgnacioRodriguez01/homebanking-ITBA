from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

class PrestamoForm(forms.Form):
    tipo = forms.ChoiceField(label = 'Prestamo', choices=[
        ('HIPOTECARIO', 'Hipotecario'),
        ('PERSONAL', 'Personal'),
        ('PRENDARIO', 'Prendario'),
    ])
    monto = forms.FloatField(label = 'Monto')

def prestamo(request): 
    prestamo_form = PrestamoForm
    if request.method == "POST":
        if prestamo_form.is_valid():
            tipo = request.POST.get('tipo',"")
            fecha = request.POST.get('fecha',"")
            monto = request.POST.get('monto',"")
            ##esto es para que muestre los datos en pantalla
            return redirect(reverse('Prestamos'))
