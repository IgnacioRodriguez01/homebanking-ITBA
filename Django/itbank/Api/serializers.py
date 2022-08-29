from django.contrib.auth.models import User
from Clientes.models import Cliente, Sucursal, Direcciones
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjetas
from Login.models import ClienteUser
from rest_framework import serializers


#Serializar usuario, clienteuser, cliente, prestamo, tarjetas, cuenta, sucursal  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ClienteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteUser
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CuentaSerializer(serializers.ModelSerializer):
    tipo_cuenta = serializers.CharField()
    balance = serializers.FloatField()
    class Meta:
        model = Cuenta
        fields = ['tipo_cuenta', 'balance']

class PrestamoMeta:
    model = Prestamo
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta(PrestamoMeta):
        fields = ['loan_type', 'loan_date', 'loan_total', 'customer_id']

class PrestamoInfoSerializer(serializers.ModelSerializer):
    loan_total = serializers.FloatField()
    class Meta(PrestamoMeta):
        fields = ['loan_type', 'loan_total']

class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = ['calle', 'numero', 'ciudad', 'provincia', 'pais']

