# Tiene solamente una tarjeta de débito que se crea junto con el cliente.
# Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente.
# Como no tiene cuenta en dólares, no puede comprar y vender dólares.
# Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.
# No tienen acceso a tarjetas de crédito ni chequeras.
# La comisión por transferencias hechas es de 1%.
# No puede recibir transferencias mayores a $150.000 sin previo aviso.

import Cliente
from main import data

class ClienteClassic(Cliente):
    def __init__(self, **kwargs):
        maxRetiroDiario= 10000
        comisionTransfer = 0.01
        maximoTransferRecibida = 150000
        super().__init__(**kwargs)
    
    def puede_crear_chequera():
        return False

    def puede_comprar_dolar():
        return False

    def puede_crear_tarjeta_credito():
        return False