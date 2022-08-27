from django.contrib.auth.models import User
from Clientes.models import Cliente, Sucursal
from Cuentas.models import Cuenta, TiposCuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjetas
from Login.models import ClienteUser
from .serializers import *

from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
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
    def get(self, request, info=None, format=None):

        # Solo clientes registrados
        try:
            userLogged = request.user.id
            clienteId = ClienteUser.objects.get(user_id__exact=userLogged).cliente_id
        except:
            error = {'error': 'Cliente no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)
        
        # Distinto queryset y serializer según URL
        if info == None:
            cliente = Cliente.objects.get(customer_id=clienteId)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif info == 'prestamos':
            prestamos = Prestamo.objects.all().filter(customer_id=clienteId)
            
            for prestamo in prestamos:
                prestamo.loan_total = convertirBalance(prestamo.loan_total)

            serializer = PrestamoInfoSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif info == 'saldo':
            cuentas = Cuenta.objects.all().filter(customer_id=clienteId)
            
            for cuenta in cuentas:
                tipoCuenta = TiposCuenta.objects.get(tipo_id=cuenta.tipo_cuenta).tipo_name
                cuenta.tipo_cuenta = tipoCuenta
                cuenta.balance = convertirBalance(cuenta.balance)

            serializer = CuentaSerializer(cuentas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EmpleadoViews(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class ClienteUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, format=None):
        try:
            userLogged = request.user.id
            clienteId = ClienteUser.objects.get(user_id__exact=userLogged).cliente_id
            # empleadoId = EmpleadoUser.objects.get(employee_id__exact=userLogged).empleado_id
        except:
            error = {'error': 'Usuario no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_404_NOT_FOUND)


class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

def convertirBalance(balance):
    balanceStr = str(balance)
    return float(balanceStr[:-2]+'.'+balanceStr[-2:])
    