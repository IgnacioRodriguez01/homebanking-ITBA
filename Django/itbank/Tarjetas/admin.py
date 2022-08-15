from django.contrib import admin
from .models import MarcasTarjeta, Tarjetas

# Register your models here.
admin.site.register(Tarjetas)
admin.site.register(MarcasTarjeta)