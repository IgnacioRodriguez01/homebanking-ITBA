class Direccion:
    def __init__(self, datos):
        self.calle = datos.get('calle')
        self.numero = datos.get('dirnumero')
        self.ciudad = datos.get('ciudad')
        self.provincia = datos.get('provincia')
        self.pais = datos.get('pais')