from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class TiposCuenta(models.Model):
    tipo_id = models.IntegerField(primary_key=True)
    tipo_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cuenta'
