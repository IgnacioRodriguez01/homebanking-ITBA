from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tarjetas(models.Model):
    numero = models.TextField(primary_key=True, max_length=16)
    tipo = models.TextField()
    marca_id = models.ForeignKey('Tarjetas.MarcasTarjeta', on_delete=models.CASCADE, db_column='marca_id')
    cvv = models.TextField(validators=[MinLengthValidator(3)], max_length=3)
    fecha_emision = models.TextField()
    fecha_vto = models.TextField()
    cliente_id = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE, db_column='cliente_id')

    class Meta:
        managed = False
        db_table = 'tarjetas'

class MarcasTarjeta(models.Model):
    marca_id = models.IntegerField(primary_key=True)
    marca_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'