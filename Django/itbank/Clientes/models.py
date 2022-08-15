from django.db import models

# Create your models here.
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

class TiposCliente(models.Model):
    tipo_id = models.IntegerField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cliente'

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

class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'

class Direcciones(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    cliente_id = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE, blank=True, null=True, db_column='cliente_id')
    empleado_id = models.ForeignKey('Clientes.Empleado', on_delete=models.CASCADE, blank=True, null=True, db_column='empleado_id')
    sucursal_id = models.ForeignKey('Clientes.Sucursal', on_delete=models.CASCADE, unique=True, blank=True, null=True, db_column='sucursal_id') #onetoone
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'