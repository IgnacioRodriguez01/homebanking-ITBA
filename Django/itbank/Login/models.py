from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClienteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE)