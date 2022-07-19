#Modulo para funciones de cálculo

# Cosas a verificar:
# Cupo Diario
# Monto disponible en cuenta (teniendo en cuenta negativo)
# Limite transferencia

def analizarTransaccion(transaccion, cliente):
    match transaccion['tipo']:
            case 'ALTA_TARJETA_CREDITO':
                if (cliente.puede_crear_tarjeta_credito(transaccion) == True):
                    return 'SIN_ERROR'
                else:
                    return cliente.puede_crear_tarjeta_credito(transaccion)
                    
            case 'ALTA_CHEQUERA':
                if (cliente.puede_crear_chequera(transaccion) == True):
                    return 'SIN_ERROR'
                else:
                    return cliente.puede_crear_chequera(transaccion)

            case 'COMPRA_DOLAR':
                if (cliente.puede_comprar_dolar() == True):
                    if transaccion['monto'] > transaccion['cupoDiarioRestante']:
                        return 'Superaste el cupo diario permitido'
                    elif transaccion['monto'] > (transaccion['saldoEnCuenta'] + cliente.maxNegativoCorriente):
                        return 'Saldo insuficiente'
                    else:
                        return 'SIN_ERROR'
                else:
                    return cliente.puede_comprar_dolar()
            
            case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if transaccion['monto'] > transaccion['cupoDiarioRestante']:
                    return 'Superaste el cupo diario permitido'
                elif transaccion['monto'] > (transaccion['saldoEnCuenta'] + cliente.maxNegativoCorriente):
                    return 'Saldo insuficiente'
                else:
                    return 'SIN_ERROR'
            
            case 'TRANSFERENCIA_ENVIADA':
                montoComision = transaccion['monto'] + cliente.comisionTransfer * transaccion['monto']
                
                if montoComision > transaccion['cupoDiarioRestante']:
                    return 'Superaste el cupo diario permitido'
                elif montoComision > (transaccion['saldoEnCuenta'] + cliente.maxNegativoCorriente):
                    return 'Saldo insuficiente'
                else:
                    return 'SIN_ERROR'
            
            case 'TRANSFERENCIA_RECIBIDA':
                if transaccion['monto'] > cliente.maximoTransferRecibida:
                    return 'El monto de la transferencia supera el límite permitido'
                else:
                    return 'SIN_ERROR'
        