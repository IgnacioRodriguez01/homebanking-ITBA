# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinLengthValidator

#foreign?
class Cliente(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'

#foreign?
class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'

#foreign
class Direcciones(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    cliente_id = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE, blank=True, null=True, db_column='cliente_id')
    empleado_id = models.ForeignKey('Clientes.Empleado', on_delete=models.CASCADE, blank=True, null=True, db_column='empleado_id')
    sucursal_id = models.ForeignKey('Clientes.Sucursal', on_delete=models.CASCADE, unique=True, blank=True, null=True, db_column='sucursal_id')
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'

#foreign?
class Empleado(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'

#listo
class MarcasTarjeta(models.Model):
    marca_id = models.IntegerField(primary_key=True)
    marca_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'

#foreign?
class Prestamo(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

#listo
class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'

#foreign
class Tarjetas(models.Model):
    numero = models.TextField(primary_key=True, max_length=16)
    tipo = models.TextField()
    marca_id = models.ForeignKey('Tarjetas.MarcasTarjeta', on_delete=models.CASCADE)
    cvv = models.TextField(validators=[MinLengthValidator(3)], max_length=3)
    fecha_emision = models.TextField()
    fecha_vto = models.TextField()
    cliente_id = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'tarjetas'

#listo
class TiposCliente(models.Model):
    tipo_id = models.IntegerField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cliente'

#listo
class TiposCuenta(models.Model):
    tipo_id = models.IntegerField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cuenta'
