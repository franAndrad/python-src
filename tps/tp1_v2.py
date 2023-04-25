# Datos ingresados
patente = input('Ingrese la patente: ')
vehiculo = int(input('Ingrese el vehiculo (0:Motocicleta 1:Auto 2:Camion): '))
pago = int(input('Ingrese el metodo de pago (1:manual 2:telepeaje): '))
pais = int(input('Ingrese el pais (0:Argentina 1:Bolivia 2:Brasil 3:Paraguay 4:Uruguay): '))
distancia = float(input('Ingrese la distancia en km: '))

# Paices
paises = ('Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay','Otro')

# Proceso para determinar patente
if len(patente) == 7:
    if patente[0].isnumeric() or patente[1].isnumeric():
        patente_pais = paises[5]
    elif patente[2].isnumeric() and not patente[5].isnumeric() and not patente[6].isnumeric():
        patente_pais = paises[0]
    elif patente[2].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        patente_pais = paises[1]
    elif patente[3].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        if patente[4].isnumeric():
            patente_pais = paises[4]
        else:
            patente_pais = paises[2]
    elif patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        patente_pais = paises[3]
    else:
        patente_pais = paises[5]
else:
    patente_pais = paises[5]

# Cobro
if paises[pais] == 'Brasil':
    importe = 400
elif paises[pais] == 'Bolivia':
    importe = 200
else:
    importe = 300

# Descuento por vehiculo
if vehiculo == 0:
    importe_vehiculo = importe - (50*importe)/100
elif vehiculo == 1:
    importe_vehiculo = importe
elif vehiculo == 2:
    importe_vehiculo = importe + (60*importe)/100
else:
    importe_vehiculo = 0

# Descuento por pago de telepeage
if pago == 1:
    total = importe_vehiculo
elif pago == 2:
    total = importe_vehiculo - (10*importe_vehiculo)/100
else:
    total = 0

# Promedio de pago por kilometro: falta redondear
if distancia != 0:
    promedio = '$ ' + str(round(total/distancia,2))
else:
    promedio = 'Primer Ingreso'


print('\n')
print('-------------------------------------------')
print('                 TICKET                    ')
print('-------------------------------------------')
print(' Patente:\t\t', patente)
print(' Procedencia:\t\t', patente_pais)
print('-------------------------------------------')
print(' Importe basico:\t $', importe_vehiculo)
print(' Total:\t\t\t $', total)
print(' Promedio/km:\t\t', promedio)
print('-------------------------------------------')
