# Tiene solamente una tarjeta de débito que se crea junto con el cliente.
# Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente.
# Como no tiene cuenta en dólares, no puede comprar y vender dólares.
# Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.
# No tienen acceso a tarjetas de crédito ni chequeras.
# La comisión por transferencias hechas es de 1%.
# No puede recibir transferencias mayores a $150.000 sin previo aviso.

from . import Cliente

class ClienteClassic(Cliente.Cliente):
    def __init__(self, **kwargs):
        self.maxNegativoCorriente = 0
        self.maxRetiroDiario= 10000
        self.comisionTransfer = 0.01
        self.maximoTransferRecibida = 150000
        self.cuentas = ['ahorro_pesos']
        super().__init__(**kwargs)
    
    def puede_crear_chequera(self, datos):
        return 'No puede tener chequeras.'

    def puede_comprar_dolar(self):
        return 'No puede comprar dólares.'

    def puede_crear_tarjeta_credito(self, datos):
        return 'No puede tener tarjetas de crédito.'
