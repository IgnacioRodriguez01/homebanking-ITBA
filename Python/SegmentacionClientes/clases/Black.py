# Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dólares.
# Pueden tener un descubierto en su cuenta corriente de hasta $10.000.
# Pueden tener hasta 5 tarjetas de crédito.
# Pueden extraer hasta $100.000 por día
# Pueden tener hasta dos chequeras.
# No se aplican comisiones a las transferencias.
# Pueden recibir transferencias por cualquier monto sin previa autorización

from . import Cliente

class ClienteBlack(Cliente.Cliente):
    def __init__(self, **kwargs):
        self.maxNegativoCorriente = 10000
        self.maxRetiroDiario= 100000
        self.comisionTransfer = 0
        self.maximoTransferRecibida = float('inf')
        self.cuentas = ['ahorro_pesos', 'ahorro_dolar', 'corriente'] 
        super().__init__(**kwargs)
    
    def puede_crear_chequera(self, datos):
        if datos['totalChequerasActualmente'] < 2:
            return True
        else:
            return 'No puede hacer tener más de dos chequeras.'

    def puede_comprar_dolar(self):
        return True
    
    def puede_crear_tarjeta_credito(self, datos):
        if datos['totalTarjetasDeCreditoActualmente'] < 5:
            return True
        else:
            return 'No puede hacer tener más de cinco tarjetas de crédito.'