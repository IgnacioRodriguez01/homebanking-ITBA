from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api import views

router = DefaultRouter()
# router.register(r'cliente', views.ClienteViewSet) #datos propios, saldo/tipo de cuenta x1, modificar direc
# router.register(r'prestamos', views.PrestamosViewSet) #monto/tipo prest. propios, de sucursales, hacer prest., anular prest.
# router.register(r'tarjetas', views.TarjetasViewSet) #tarjetas propias, 
# router.register(r'sucursales', views.SucursalesViewSet) #listado sucursales

# datos (permisos) url/

# Cliente datos (cliente) cliente/
# Cliente saldo (cliente) cliente/saldo
# Cliente prestamos (cliente) cliente/prestamos
# Sucursal prestamos (empleado) empleados/prestamos-sucursales
# Tarjetas cliente (empleado) empleados/tarjetas-cliente
# Generar prestamo (empleado) empleados/nuevo-prestamo
# Anular prestamo (empleado) empleados/anular-prestamo
# Modif direcc (cliente-empleado) cliente/1/editar-direccion ???
# Listado sucursales (publico) sucursales

urlpatterns = [
    #path('', include(router.urls)),
    path('cliente/', views.ClienteViews.as_view(), name='cliente'),
    path('cliente/<info>', views.ClienteViews.as_view(), name='cliente-info'),
    path('sucursales/', views.SucursalesList.as_view(), name='sucursales'),
]