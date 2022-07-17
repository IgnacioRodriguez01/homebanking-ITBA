from Direccion import Direccion

class Cliente:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.numero = kwargs.get('numero')
        self.dni = kwargs.get('dni')
        self.direccion = Direccion
