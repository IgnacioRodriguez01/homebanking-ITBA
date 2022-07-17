class Direccion:
    def __init__(self, **kwargs):
        self.calle = kwargs.get('calle')
        self.numero = kwargs.get('numero')
        self.ciudad = kwargs.get('ciudad')
        self.provincia = kwargs.get('provincias')
        self.pais = kwargs.get('pais')