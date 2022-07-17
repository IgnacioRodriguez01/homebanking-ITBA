from main import data

# Diferentes tipos de tarjetas de credito y operaciones segun su tipo
# caja ahorro pesos, cuenta ahorro dolar, cuenta corriente 

class Cuenta:
    def __init__(self, **kwargs):
        self.tipo = kwargs.get('tipo')
        self.limite_ext_diario
