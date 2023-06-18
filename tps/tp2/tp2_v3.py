def patentes_pais(patente):
    is_c_vacio = False
    if patente[0] == ' ':
        is_c_vacio = True

    if len(patente) == 7:
        if patente[0].isnumeric() or patente[1].isnumeric():
            return 'Otro'
        elif not is_c_vacio and patente[2].isnumeric() and not patente[5:].isnumeric():
            return 'Argentina'
        elif not is_c_vacio and patente[2].isnumeric() and patente[5:].isnumeric():
            return 'Bolivia'
        elif not is_c_vacio and patente[3].isnumeric() and patente[5:].isnumeric():
            if patente[4].isnumeric():
                return 'Uruguay'
            else:
                return 'Brasil'
        elif patente[5:].isnumeric():
            if not is_c_vacio and patente[4].isnumeric():
                return 'Paraguay'
            elif is_c_vacio and not patente[2:4].isnumeric() and not patente[4].isnumeric():
                return 'Chile'
        return 'Otro'

def cobro(pais):
    paises_mercosur = ('Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay')
    if paises_mercosur[pais] == 'Brasil':
        return 400, 'Brasil'
    elif paises_mercosur[pais] == 'Bolivia':
        return 200, 'Bolivia'
    elif paises_mercosur[pais] == 'Argentina':
        return 300, 'Argentina'
    elif paises_mercosur[pais] == 'Paraguay':
        return 300, 'Paraguay'
    elif paises_mercosur[pais] == 'Uruguay':
        return 300, 'Uruguay'


def importe_vehiculo(vehiculo, importe):
    if vehiculo == 0:
        return importe - (50*importe)/100
    elif vehiculo == 1:
        return importe
    elif vehiculo == 2:
        return importe + (60*importe)/100
    else:
        return 0


def forma_pago(pago, importe):
    if pago == 1:
        return int(importe)
    elif pago == 2:
        return int(importe - (10*importe)/100)
    else:
        return 0


def lenguaje(palabra):
    sE = False
    sES = False
    sP = False
    sPT = False
    for caracteres in palabra:
        if caracteres == 'E':
            sE = True
        elif caracteres == 'S' and sE:
            sES = True
        else:
            sE = False
        if caracteres == 'P':
            sP = True
        elif caracteres == 'T' and sP:
            sPT = True
        else:
            sP = False
    if sES:
        return 'Español'
    elif sPT:
        return 'Portugués'


def porcentaje(cantidad, total):
    if total > 0:
        return round(cantidad*100 / total, 2)
    else:
        return 0


def promedio(cantidad, total):
    if cantidad > 0:
        return round(total/cantidad, 2)
    else:
        return 0


def principal():
    # Variable para el idioma
    idioma = ''

    # Variables cantidad de patentes paises ,procedencia del pais y cabina de ingreso
    carg = cbol = cbra = cchi = cpar = curu = cotr = 0 
    procedencia = ''

    # Variables para determinar los datos del vehiculo ingresado
    patente, vehiculo, pago, pais, distancia = '', '', '', '', ''

    # Variable para el importe total acumulado
    imp_acum_total = 0

    # Variables para deteccion de la primer patente y su frecuencia
    es_la_primer_patente = True
    primera = ''
    cpp = 1

    # Variables para el promedio de los vehiculos Arg que pasan por la cabina Br
    cant_vehiculos_arg_cabina_br = 0
    suma_distancia_vehiculos_arg_cabina_br = 0

    archivo = open('./peaje.txt', 'rt')
    primer_linea = archivo.readline().upper()
    idioma = lenguaje(primer_linea)

    while True:
        linea = archivo.readline()

        if linea == '':
            break

        patente = linea[0:7]
        vehiculo = int(linea[7])
        pago = int(linea[8])
        pais = int(linea[9])
        distancia = float(linea[10:13])

        # cantidad de patentes de los paises
        procedencia = patentes_pais(patente)
        if procedencia == 'Argentina':
            carg += 1
        elif procedencia == 'Bolivia':
            cbol += 1
        elif procedencia == 'Brasil':
            cbra += 1
        elif procedencia == 'Chile':
            cchi += 1
        elif procedencia == 'Otro':
            cotr += 1
        elif procedencia == 'Paraguay':
            cpar += 1
        elif procedencia == 'Uruguay':
            curu += 1

        base, cabina_pais = cobro(pais)
        subtotal = importe_vehiculo(vehiculo, base)
        total = forma_pago(pago, subtotal)
        imp_acum_total += total

        # frecuencia primer patente y mayor importe de una patente
        if primera == patente:
            cpp += 1
        if es_la_primer_patente:
            primera = patente
            mayimp = total
            maypat = patente
            es_la_primer_patente = False
        elif total > mayimp:
            mayimp = total
            maypat = patente

        # vehiculos Argentinos que pasaron por una cabina brasilera
        if procedencia == 'Argentina' and cabina_pais == 'Brasil':
            cant_vehiculos_arg_cabina_br += 1
            suma_distancia_vehiculos_arg_cabina_br += distancia
    
    archivo.close()

    # Cantidad total de patentes
    total_patentes = carg + cbol + cbra + cchi + cpar + curu + cotr

    # Calculo de porcentaje y promedio
    porc = porcentaje(cotr, total_patentes)
    prom = promedio(cant_vehiculos_arg_cabina_br,
                    suma_distancia_vehiculos_arg_cabina_br)

    # Visualicación de resultados...
    print()
    print('(r1) - Idioma a usar en los informes:', idioma)
    print()
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro país:', cotr)
    print()
    print('(r3) - Importe acumulado total de importes finales:', imp_acum_total)
    print()
    print('(r4) - Primera patente del archivo:',
          primera, '- Frecuencia de:', cpp)
    print()
    print('(r5) - Mayor importe final cobrado:', mayimp,
          '- Patente a la que se cobró ese importe:', maypat)
    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')


# Determinar datos al pasar por el telepeaje mediante el documento
principal()
