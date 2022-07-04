import csv, sys, datetime

date = datetime.datetime.now()
date = str(date.strftime("%Y-%m-%d_%H-%M-%S"))

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

for i in range(0,len(sys.argv)):
    match i:
        case 1:
            archivo = sys.argv[1]
        case 2:    
            dni = sys.argv[2]
        case 3:    
            salida = sys.argv[3]
        case 4:    
            tipo = sys.argv[4]
        case 5:    
            estado = sys.argv[5] #opcional
        case 6:    
            fecha = sys.argv[6] #opcional  


with open(archivo, newline='') as File:  
    reader = csv.reader(File)
    cheques = list(reader)
    columnas = cheques.pop(0)

    resultado = list(filter(lambda cheque: cheque[POS_DNI] == dni, cheques))
    resultado = list(filter(lambda cheque: cheque[POS_TIPO] == tipo, resultado))
    if estado != '':
        resultado = list(filter(lambda cheque: cheque[POS_ESTADO] == estado, resultado))

    #SALIDA
    if salida == 'PANTALLA':
        print(resultado)

    elif salida == 'CSV':
        print(resultado)
        with open((dni + '' + date), 'w+') as NewFile:  
            NewFile = csv.writer(NewFile)
            if len(resultado) > 0:
                NewFile.writerow(columnas)
                NewFile.writerows(resultado)
            else:
                NewFile.writerow('-')
                