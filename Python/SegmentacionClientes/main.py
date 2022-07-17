import json

from clases.Cliente import Cliente
from clases.Cuenta import Cuenta
from clases.Classic import ClienteClassic
from clases.Gold import ClienteGold
from clases.Black import ClienteBlack

with open('ejemplos_json/eventos_black.json') as archivo:
    data = json.load(archivo)
    
print(data['tipo'])

#unpacking de data, y pasar como argumentos a cliente.

nuevoCliente = Cliente()

match nuevoCliente.tipo:
    case 'CLASSIC':
        clienteTipo = ClienteClassic()
    case 'GOLD':
        clienteTipo = ClienteGold()
    case 'BLACK':
        clienteTipo = ClienteBlack()