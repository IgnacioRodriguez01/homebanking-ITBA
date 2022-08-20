from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

class PrestamoForm(forms.Form):
    template_name = "Prestamos/form_snippet.html"
    tipo = forms.ChoiceField(label = 'Prestamo', choices=[
        ('HIPOTECARIO', 'Hipotecario'),
        ('PERSONAL', 'Personal'),
        ('PRENDARIO', 'Prendario'),
    ])
    monto = forms.FloatField(label = 'Monto ($)', initial=0)
    fecha = forms.DateField(label = 'Fecha de Inicio', widget=forms.DateInput(attrs={'type': 'date'}))