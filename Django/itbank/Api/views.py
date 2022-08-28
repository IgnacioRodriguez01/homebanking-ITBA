from django.contrib.auth.models import User
from Clientes.models import Cliente, Sucursal
from Cuentas.models import Cuenta, TiposCuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjetas
from Login.models import ClienteUser
from .serializers import *

from rest_framework import status, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# con viewset: (va con router en la urlconf)
# class ClienteViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

# con generics views
# class ClienteDetail(generics.RetrieveUpdateDestroyAPIView)
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

# con class views
class ClienteViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        userLogged = request.user.id
        urlpath = request.path.replace("/api/cliente/", "")

        # Solo clientes registrados
        try:
            clienteId = ClienteUser.objects.get(user_id__exact=userLogged).cliente_id
        except:
            error = {'error': 'Cliente no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)
        
        # Distinto queryset y serializer según URL
        if urlpath.startswith('cliente'):
            cliente = Cliente.objects.get(customer_id=clienteId)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif urlpath.startswith('prestamos'):
            prestamos = Prestamo.objects.all().filter(customer_id=clienteId)
            
            for prestamo in prestamos:
                prestamo.loan_total = convertirBalance(prestamo.loan_total)

            serializer = PrestamoInfoSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif urlpath.startswith('saldo'):
            cuentas = Cuenta.objects.all().filter(customer_id=clienteId)
            
            for cuenta in cuentas:
                tipoCuenta = TiposCuenta.objects.get(tipo_id=cuenta.tipo_cuenta).tipo_name
                cuenta.tipo_cuenta = tipoCuenta
                cuenta.balance = convertirBalance(cuenta.balance)

            serializer = CuentaSerializer(cuentas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, format=None):
        userLogged = request.user.id
        urlpath = request.path.replace("/api/cliente/", "")

        # Solo clientes registrados
        try:
            userLogged = request.user.id
            clienteId = ClienteUser.objects.get(user_id__exact=userLogged).cliente_id

        except:
            error = {'error': 'Cliente no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)

        # Verificar URL
        if urlpath.startswith('editar-direccion'):
            try:
                direccion = Direcciones.objects.filter(cliente_id=clienteId).first()
            except:
                error = {'error': 'Direccion de cliente no encontrada en el sistema.'}
                return Response(error ,status=status.HTTP_404_NOT_FOUND)
            
            # Si el body está vacío, devuelve el elemento actual
            if(request.data == {}):
                serializer = DireccionesSerializer(direccion)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            # Actualiza la dirección
            serializer = DireccionesSerializer(direccion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EmpleadoViews(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, info=None, pk=None,format=None):
        userLogged = request.user.id
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        try:
            # empleadoId = EmpleadoUser.objects.get(user_id__exact=userLogged).empleado_id
            pass
        except:
            error = {'error': 'Empleado no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)

        # Distinto queryset y serializer según URL
        if urlpath.startswith('tarjetas-cliente'):
            tarjetas = Tarjetas.objects.all().filter(cliente_id=pk)
            serializer = TarjetasSerializer(tarjetas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif urlpath.startswith('prestamos-sucursal'):
            # ver como hacer el recuento por sucursal, dependiendo los clientes.
            prestamos = Prestamo.objects.all().filter(cliente_id=pk)
            serializer = PrestamoSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        userLogged = request.user.id
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        try:
            # empleadoId = EmpleadoUser.objects.get(user_id__exact=userLogged).empleado_id
            pass
        except:
            error = {'error': 'Empleado no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)
        
        # Verificar URL
        if urlpath.startswith('editar-direccion'):
            try:
                direccion = Direcciones.objects.filter(cliente_id=pk).first()
            except:
                error = {'error': 'Direccion de cliente no encontrada en el sistema.'}
                return Response(error ,status=status.HTTP_404_NOT_FOUND)
            
            # Si el body está vacío, devuelve el elemento actual
            if(request.data == {}):
                serializer = DireccionesSerializer(direccion)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            # Actualiza la dirección
            serializer = DireccionesSerializer(direccion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

""" 
    def post():
        userLogged = request.user.id
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        try:
            # empleadoId = EmpleadoUser.objects.get(user_id__exact=userLogged).empleado_id
            pass
        except:
            error = {'error': 'Empleado no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)
        
        # Verificar URL
        if urlpath.startswith('nuevo-prestamo/'):
            pass
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete():
        userLogged = request.user.id
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        try:
            # empleadoId = EmpleadoUser.objects.get(user_id__exact=userLogged).empleado_id
            pass
        except:
            error = {'error': 'Empleado no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)

        # Verificar URL
        if urlpath.startswith('anular-prestamo/'):
            pass
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
 """

class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

def convertirBalance(balance):
    balanceStr = str(balance)
    return float(balanceStr[:-2]+'.'+balanceStr[-2:])