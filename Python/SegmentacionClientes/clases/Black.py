# Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dólares.
# Pueden tener un descubierto en su cuenta corriente de hasta $10.000.
# Pueden tener hasta 5 tarjetas de crédito.
# Pueden extraer hasta $100.000 por día
# Pueden tener hasta dos chequeras.
# No se aplican comisiones a las transferencias.
# Pueden recibir transferencias por cualquier monto sin previa autorización

import Cliente
from main import data


class ClienteGold(Cliente):
    def __init__(self, **kwargs):
        maxNegativoDiario = -10000
        maxRetiroDiario= 100000
        super().__init__(**kwargs)
    
    def puede_crear_chequera():
        if data.get['totalChequerasActualmente'] > 2:
            return False
        else:
            return True

    def puede_comprar_dolar():
        return True
    
    def puede_crear_tarjeta_credito():
        if data.get['totalTarjetasDeCreditoActualmente'] > 5:
            return False
        else:
            return True