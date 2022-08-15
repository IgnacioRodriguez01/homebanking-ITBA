from django.contrib import admin
from .models import Cliente, Direcciones, Empleado, Sucursal, TiposCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TiposCliente)
admin.site.register(Empleado)
admin.site.register(Sucursal)
admin.site.register(Direcciones)