import json, sys, webbrowser

from modulos.calculos import analizarTransaccion

from clases.Cliente import Cliente
from clases.Classic import ClienteClassic
from clases.Gold import ClienteGold
from clases.Black import ClienteBlack

ARCHIVO_JSON = 'ejemplos_json/eventos_black.json'
# Apertura del JSON

with open(ARCHIVO_JSON) as archivo:
    try:
        data = json.load(archivo)    
    except:
        print('Archivo JSON incorrecto.')
        sys.exit()

# Instanciación de la clase Cliente

nuevoCliente = Cliente(
    nombre=data['nombre'],
    apellido=data['apellido'],
    numero=data['numero'],
    dni=data['dni'],
    calle= data['direccion']['calle'],
    dirnumero= data['direccion']['numero'],
    ciudad= data['direccion']['ciudad'],
    provincia= data['direccion']['provincia'],
    pais= data['direccion']['pais']
)

#Instanciación de la clase Black, Gold o Classic

match data['tipo']:
    case 'CLASSIC':
        clienteTipo = ClienteClassic()
    case 'GOLD':
        clienteTipo = ClienteGold()
    case 'BLACK':
        clienteTipo = ClienteBlack()

# Creación del archivo HTML

with open('index.html', 'w') as html_file:
    
    html_file.writelines('<html>')
    html_file.writelines('<h1> Reporte de transacciones </h1>')
    html_content = f'<p> Nombre: {nuevoCliente.nombre} {nuevoCliente.apellido} Nro. Cliente: {nuevoCliente.numero} DNI: {nuevoCliente.dni}</p>'
    html_file.writelines(html_content)
    html_content = f'<p> Dirección: {nuevoCliente.direccion.calle} {nuevoCliente.direccion.numero}, {nuevoCliente.direccion.ciudad}, {nuevoCliente.direccion.provincia}, {nuevoCliente.direccion.pais}</p>'
    html_file.writelines(html_content)

    for transaccion in data['transacciones']:
        razon = analizarTransaccion(transaccion, clienteTipo)

        # print(transaccion['tipo'], transaccion['estado'], razon)
        html_file.writelines(f'<h3> Transaccion {transaccion["numero"]}</h3>')
        html_file.writelines(f'<p> Fecha: {transaccion["fecha"]}</p>')
        html_file.writelines(f'<p> Tipo: {transaccion["tipo"]}</p>')
        html_file.writelines(f'<p> Monto: {transaccion["monto"]}</p>')
        html_file.writelines(f'<p> Estado: {transaccion["estado"]}</p>')
        if razon != 'SIN_ERROR':
            html_file.writelines(f'<p> Razón: {razon}</p>')

    html_file.writelines('</html>')
    print('Se ha creado un archivo .HTML con el reporte')

webbrowser.open_new_tab('index.html')
