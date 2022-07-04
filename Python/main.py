import csv, sys, datetime

POS_NROCHEQUE = 0
POS_CODIGOBANCO = 1
POS_CODIGOSUCURSAL = 2
POS_NUMEROCUENTAORIGEN = 3
POS_NUMEROCUENTADESTINO = 4
POS_VALOR = 5
POS_FECHAORIGEN = 6
POS_FECHAPAGO = 7
POS_DNI = 8
POS_TIPO = 9
POS_ESTADO = 10

INPUTS_CSV = 1
INPUTS_DNI = 2
INPUTS_SALIDA = 3
INPUTS_TIPO = 4
INPUTS_ESTADO = 5
INPUTS_FECHA = 6

estado = ''
fecha = ''

#Lectura de parámetros
for i in range(0,len(sys.argv)):
    match i:
        case 1:
            archivo = sys.argv[INPUTS_CSV]
        case 2:    
            dni = sys.argv[INPUTS_DNI]
        case 3:    
            salida = sys.argv[INPUTS_SALIDA]
        case 4:    
            tipo = sys.argv[INPUTS_TIPO]
        case 5:    
            estado = sys.argv[INPUTS_ESTADO] #Opcional
        case 6:    
            fecha = sys.argv[INPUTS_FECHA] #Opcional  

with open(archivo) as File:
    #Lectura del CSV
    reader = csv.reader(File)
    cheques = list(reader)

    resultado = list(filter(lambda cheque: cheque[POS_DNI] == dni, cheques))

    #Comprobación de nro de cheques
    if len(resultado) > 0:
        cuenta = resultado[0][POS_NUMEROCUENTAORIGEN]
        listaNroCheques = []
        for cheque in cheques:
            if cheque[POS_NUMEROCUENTAORIGEN] == cuenta:
                listaNroCheques.append(cheque[POS_NROCHEQUE])
        setNroCheques = set(listaNroCheques)

        if len(listaNroCheques) != len(setNroCheques):
            print('Error! En la cuenta perteneciente a este DNI existen cheques repetidos')
            sys.exit()

    #Filtrados adicionales
    resultado = list(filter(lambda cheque: cheque[POS_TIPO] == tipo, resultado))
    
    if estado != '':
        resultado = list(filter(lambda cheque: cheque[POS_ESTADO] == estado, resultado))
    if fecha != '':
        #Slicing de las fechas en tuplas (año, mes, dia)
        fechaInicial = int(fecha[:10][6:]), int(fecha[:10][3:5]), int(fecha[:10][:2])
        fechaFinal = int(fecha[11:][6:]), int(fecha[11:][3:5]), int(fecha[11:][:2])
        
        #Unpacking y conversión a timestamp
        y, m, d = fechaInicial
        timestampInicial = datetime.datetime.timestamp(datetime.datetime(y, m, d))
        y, m, d = fechaFinal
        timestampFinal = datetime.datetime.timestamp(datetime.datetime(y, m, d))

        #Filtrado según fecha
        resultado = list(filter(lambda cheque: timestampInicial <= float(cheque[POS_FECHAORIGEN]) <= timestampFinal, resultado))

    #Salida
    if salida == 'PANTALLA':
        print(resultado)

    elif salida == 'CSV':
        timestampActual = datetime.datetime.timestamp(datetime.datetime.now())

        with open((dni + '_' + str(round(timestampActual))), 'w+', newline='') as NewFile:  
            NewFile = csv.writer(NewFile, lineterminator='\n')
            if len(resultado) > 0:
                NewFile.writerow(["FechaPago","FechaOrigen","Valor","NumeroCuentaOrigen"])
                for cheque in resultado:
                    NewFile.writerow([cheque[POS_FECHAPAGO],cheque[POS_FECHAORIGEN],cheque[POS_VALOR],cheque[POS_NUMEROCUENTAORIGEN]])
            else:
                NewFile.writerow(["No hay resultados."])
                