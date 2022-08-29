from __future__ import print_function
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
            return Response(error ,status=status.HTTP_401_UNAUTHORIZED)
        
        # Distinto queryset y serializer según URL
        if urlpath == '': #/api/cliente/
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
            return Response(error ,status=status.HTTP_401_UNAUTHORIZED)

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

"""
Nota: para el registro de empleados se descartó la alternativa de usar el modelo
de Empleado, y relacionar cada uno con un usuario registrado (De la misma manera
que con los clientes) con un modelo EmpleadoUser, y así tener una verificación de
los empleados reales del banco:

 # Solo empleados registrados
        try:
            userLogged = request.user.id
            # empleadoId = EmpleadoUser.objects.get(user_id__exact=userLogged).empleado_id
            pass
        except:
            error = {'error': 'Empleado no encontrado en el sistema.'}
            return Response(error ,status=status.HTTP_401_UNAUTHORIZED)

De todas maneras, se optó por elegir a los empleados como los usuarios con
capacidades de staff en la base de datos.

"""

class EmpleadoViews(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, info=None, pk=None,format=None):
        urlpath = request.path.replace("/api/empleados/", "")
        
        # Solo empleados registrados
        if not request.user.is_staff == 1:
                error = {'error': 'Empleado no encontrado en el sistema.'}
                return Response(error ,status=status.HTTP_401_UNAUTHORIZED)

        # Distinto queryset y serializer según URL
        if urlpath.startswith('tarjetas-cliente'):
            tarjetas = Tarjetas.objects.all().filter(cliente_id=pk)
            serializer = TarjetasSerializer(tarjetas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif urlpath.startswith('prestamos-sucursal'):
            prestamos = []

            clientes = Cliente.objects.filter(branch_id=pk)
            for cliente in clientes:
                prestamos += Prestamo.objects.all().filter(customer_id=cliente.customer_id)
                print(prestamos);
            if prestamos == []: 
                error = {"info": "La sucursal no ha emitido préstamos al día de la fecha."}
                return Response(error, status=status.HTTP_200_OK)
                pass

            serializer = PrestamoSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        urlpath = request.path.replace("/api/empleados/", "")
        
        # Solo empleados registrados
        if not request.user.is_staff == 1:
                error = {'error': 'Empleado no encontrado en el sistema.'}
                return Response(error ,status=status.HTTP_401_UNAUTHORIZED)

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


    def post(self, request, format=None):
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        if not request.user.is_staff == 1:
                error = {'error': 'Empleado no encontrado en el sistema.'}
                return Response(error ,status=status.HTTP_401_UNAUTHORIZED)
        
        # Verificar URL
        if urlpath.startswith('nuevo-prestamo/'):
            serializer = PrestamoSerializer(data=request.data)
            if serializer.is_valid():
                # Guardar prestamo
                serializer.save()

                # Actualizar cuenta de cliente
                cuenta = Cuenta.objects.all().filter(customer_id=serializer.data['customer_id']).first()
                cuenta.balance = calcularBalanceCuenta(cuenta, serializer.data['loan_total'], 'suma')
                cuenta.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        urlpath = request.path.replace("/api/empleados/", "")

        # Solo empleados registrados
        if not request.user.is_staff == 1:
                error = {'error': 'Empleado no encontrado en el sistema.'}
                return Response(error ,status=status.HTTP_401_UNAUTHORIZED)

        # Verificar URL
        if urlpath.startswith('anular-prestamo/'):
            prestamo = Prestamo.objects.all().get(loan_id=pk)
            # Anular prestamo
            prestamo.delete()

            # Actualizar cuenta de cliente
            cuenta = Cuenta.objects.all().filter(customer_id=prestamo.customer_id).first()
            cuenta.balance = calcularBalanceCuenta(cuenta, prestamo.loan_total, 'resta')
            cuenta.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

def convertirBalance(balance):
    balanceStr = str(balance)
    return float(balanceStr[:-2]+'.'+balanceStr[-2:])

def calcularBalanceCuenta(cuenta, monto, operacion):
    #Agregar el monto al saldo del cliente, con el formato requerido
    balance = str(cuenta.balance)
    monto = str(monto)

    balanceFloat = float(balance[:-2]+'.'+balance[-2:])
    montoFloat = float(monto[:-2]+'.'+monto[-2:])

    match operacion:
        case 'suma':
            balanceFloat += montoFloat
        case 'resta':
            balanceFloat -= montoFloat
    
    balanceConv = "{0:.2f}".format(balanceFloat).replace('.', '')
    return balanceConv