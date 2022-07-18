import json, sys, webbrowser

from clases.Cliente import Cliente

from clases.Classic import ClienteClassic
from clases.Gold import ClienteGold
from clases.Black import ClienteBlack

with open('ejemplos_json/eventos_gold.json') as archivo:
    try:
        data = json.load(archivo)    
    except:
        print('Archivo JSON incorrecto.')
        sys.exit()
    
print(data['direccion']['numero'])

#unpacking de data, y pasar como argumentos a cliente.

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

print(nuevoCliente.direccion.pais)

match data['tipo']:
    case 'CLASSIC':
        clienteTipo = ClienteClassic()
    case 'GOLD':
        clienteTipo = ClienteGold()
    case 'BLACK':
        clienteTipo = ClienteBlack()

with open('index.html', 'w') as html_file:
    
    html_file.writelines('<html>')
    html_file.writelines('<h1> Reporte de transacciones </h1>')
    html_content = f'<p> Nombre: {clienteTipo.nombre} {clienteTipo.apellido} Nro. Cliente: {clienteTipo.numero} DNI: {clienteTipo.dni}</p>'
    html_file.writelines(html_content)
    html_content = f'<p> Dirección: {clienteTipo.direccion.calle} {clienteTipo.direccion.numero}, {clienteTipo.direccion.ciudad}, {clienteTipo.direccion.provincia}, {clienteTipo.direccion.pais}</p>'
    html_file.writelines(html_content)

    
    for transaccion in data['transacciones']:
    
        match transaccion['tipo']:
            case 'ALTA_TARJETA_CREDITO':
                if (clienteTipo.puede_crear_tarjeta_credito(transaccion) == True):
                    razon = 'SIN_ERROR'
                else:
                    razon = clienteTipo.puede_crear_tarjeta_credito(transaccion)
                    
            case 'ALTA_CHEQUERA':
                if (clienteTipo.puede_crear_chequera(transaccion) == True):
                    razon = 'SIN_ERROR'
                else:
                    razon = clienteTipo.puede_crear_chequera(transaccion)

            case 'COMPRA_DOLAR':
                if (clienteTipo.puede_comprar_dolar() == True):
                    if transaccion['monto'] > transaccion['cupoDiarioRestante']:
                        razon = 'Superaste el cupo diario permitido'
                    elif transaccion['monto'] > (transaccion['saldoEnCuenta'] + clienteTipo.maxNegativoCorriente):
                        razon = 'Saldo insuficiente'
                    else:
                        razon = 'SIN_ERROR'
                else:
                    razon = clienteTipo.puede_comprar_dolar()
            
            case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if transaccion['monto'] > transaccion['cupoDiarioRestante']:
                    razon = 'Superaste el cupo diario permitido'
                elif transaccion['monto'] > (transaccion['saldoEnCuenta'] + clienteTipo.maxNegativoCorriente):
                    razon = 'Saldo insuficiente'
                else:
                    razon = 'SIN_ERROR'
            
            case 'TRANSFERENCIA_ENVIADA':
                montoComision = transaccion['monto'] + clienteTipo.comisionTransfer * transaccion['monto']
                
                if montoComision > transaccion['cupoDiarioRestante']:
                    razon = 'Superaste el cupo diario permitido'
                elif montoComision > (transaccion['saldoEnCuenta'] + clienteTipo.maxNegativoCorriente):
                    razon = 'Saldo insuficiente'
                else:
                    razon = 'SIN_ERROR'
            
            case 'TRANSFERENCIA_RECIBIDA':
                if transaccion['monto'] > clienteTipo.maximoTransferRecibida:
                    razon = 'El monto de la transferencia supera el límite permitido'
                else:
                    razon = 'SIN_ERROR'
        variable = transaccion['numero']
        print(transaccion['tipo'], transaccion['estado'], razon)
        html_content = f'<p> {variable} {razon} </p>'
        html_file.writelines(html_content)

    
    html_file.writelines('</html>')
    print('Se ha creado un archivo .HTML con el reporte')

webbrowser.open_new_tab('index.html')
