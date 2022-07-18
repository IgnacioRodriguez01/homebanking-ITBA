#Tiene una tarjeta de débito que se crea con el cliente.
# Tiene una cuenta corriente con un descubierto de $10.000.
## Hay que tener presente que como tiene cuenta corriente el saldo en la cuenta podría ser
## negativo y hasta -$10.000 si tiene cupo diario para la operación que se quiera realizar.
# Tiene una caja de ahorro en dólares, por lo que puede comprar dólares.
# Puede tener solo una tarjeta de crédito.
# Las extracciones de efectivo tienen un máximo de $20.000 por día.
# Pueden tener una chequera.
# La comisión por transferencias hechas es de 0,5%.
# No puede recibir transferencias mayores a $500.000 sin previo aviso.

from . import Cliente

class ClienteGold(Cliente.Cliente):
    def __init__(self, **kwargs):
        self.maxNegativoCorriente = 10000
        self.maxRetiroDiario= 20000
        self.comisionTransfer = 0.005
        self.maximoTransferRecibida = 500000
        self.cuentas = ['ahorro_pesos', 'ahorro_dolar', 'corriente'] 
        super().__init__(**kwargs)
    
    def puede_crear_chequera(self, datos):
        if datos['totalChequerasActualmente'] < 1:
            return True
        else:
            return 'No puede hacer tener más de una chequera.'

    def puede_comprar_dolar(self):
        return True
    
    def puede_crear_tarjeta_credito(self, datos):
        if datos['totalTarjetasDeCreditoActualmente'] < 1:
            return True
        else:
            return 'No puede hacer tener más de una tarjeta de crédito.'
    

