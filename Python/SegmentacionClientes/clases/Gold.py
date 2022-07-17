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

import Cliente
from main import data

class ClienteGold(Cliente):
    def __init__(self, **kwargs):
        maxNegativoDiario = -10000
        maxRetiroDiario= 20000
        comisionTransfer = 0.005
        maximoTransferRecibida = 500000
        super().__init__(**kwargs)
    
    def puede_crear_chequera():
        if data.get['totalChequerasActualmente'] > 1:
            return False
        else:
            return True

    def puede_comprar_dolar():
        return True
    
    def puede_crear_tarjeta_credito():
        if data.get['totalTarjetasDeCreditoActualmente'] > 1:
            return False
        else:
            return True

