from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api import views

# datos (permisos) url/

# Cliente datos (cliente) cliente/
# Cliente saldo (cliente) cliente/saldo
# Cliente prestamos (cliente) cliente/prestamos
# Sucursal prestamos (empleado) empleados/prestamos-sucursal/1
# Tarjetas cliente (empleado) empleados/tarjetas-cliente
# Generar prestamo (empleado) empleados/nuevo-prestamo
# Anular prestamo (empleado) empleados/anular-prestamo
# Modif direcc (cliente-empleado) cliente/editar-direccion o empleados/editar-direccion/1
# Listado sucursales (publico) sucursales

urlpatterns = [
    path('cliente/', views.ClienteViews.as_view(), name='cliente'),
    path('cliente/saldo/', views.ClienteViews.as_view(), name='cliente-saldo'),
    path('cliente/prestamos/', views.ClienteViews.as_view(), name='cliente-prestamos'),
    path('cliente/editar-direccion/', views.ClienteViews.as_view(), name='cliente-editardirec'),

    path('empleados/nuevo-prestamo/', views.EmpleadoViews.as_view(), name='empleados-nuevoprestamo'),
    path('empleados/anular-prestamo/<int:pk>/', views.EmpleadoViews.as_view(), name='empleados-anularprestamo'),
    path('empleados/tarjetas-cliente/<int:pk>/', views.EmpleadoViews.as_view(), name='empleados-tarjetas'),
    path('empleados/prestamos-sucursal/<int:pk>/', views.EmpleadoViews.as_view(), name='empleados-prestamossuc'),
    path('empleados/editar-direccion/<int:pk>/', views.EmpleadoViews.as_view(), name='empleados-editardirec'),
    
    path('sucursales/', views.SucursalesList.as_view(), name='sucursales'),
]