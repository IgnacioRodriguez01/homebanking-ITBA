# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    direccion_id = models.AutoField()
    cliente_id = models.IntegerField(blank=True, null=True)
    empleado_id = models.IntegerField(blank=True, null=True)
    sucursal_id = models.IntegerField(unique=True, blank=True, null=True)
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcasTarjeta(models.Model):
    marca_id = models.AutoField(blank=True, null=True)
    marca_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjetas(models.Model):
    numero = models.TextField()
    tipo = models.TextField()
    marca_id = models.IntegerField()
    cvv = models.IntegerField()
    fecha_emision = models.TextField()
    fecha_vto = models.TextField()
    cliente_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjetas'


class TiposCliente(models.Model):
    tipo_id = models.AutoField(blank=True, null=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cliente'


class TiposCuenta(models.Model):
    tipo_id = models.AutoField(blank=True, null=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cuenta'
