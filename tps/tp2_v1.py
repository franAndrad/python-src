def cantidad_patentes_pais(patente, carg, cbol, cbra, cchi, cpar, curu, cotr):
    # falta tener en cuenta el primer espacio para que no lo tome en los otros paises
    if len(patente) == 7:
        if patente[0].isnumeric() or patente[1].isnumeric():
            cotr += 1
            pais = 'Otro'
        elif patente[2].isnumeric() and not patente[5].isnumeric() and not patente[6].isnumeric():
            carg += 1
            pais = 'Argentina'
        elif patente[2].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
            cbol += 1
            pais = 'Bolivia'
        elif patente[3].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
            if patente[4].isnumeric():
                curu += 1
                pais = 'Uruguay'
            else:
                cbra += 1
                pais = 'Brasil'
        elif patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
            cpar += 1
            pais = 'Paraguay'
        elif patente[5].isnumeric() and patente[6].isnumeric():
            cchi += 1
            pais = 'Chile'
        else:
            cotr += 1
            pais = 'Otro'
    else:
        cotr += 1    
        pais = 'Otro'
    return carg, cbol, cbra, cchi, cpar, curu, cotr, pais

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
    
def importe_vehiculo(vehiculo,importe):
    if vehiculo == 0:
        return importe - (50*importe)/100
    elif vehiculo == 1:
        return importe
    elif vehiculo == 2:
        return importe + (60*importe)/100
    else:
        return 0
    
def forma_pago(pago,importe):
    if pago == 1:
        return importe
    elif pago == 2:
        return importe - (10*importe)/100
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
        else:
            if caracteres == 'S' and sE:
                sES = True
            sE = False
        if caracteres == 'P':
            sP = True
        else:
            if caracteres == 'T' and sP:
                sPT = True
            sP = False
    if sES:
        return 'Español'
    elif sPT:
        return 'Portugues'

def porcentaje(cantidad,total):
    if total > 0:
        return round(cantidad*100 / total ,2)
    else:
        return 0

def promedio(cantidad,total):
    if cantidad > 0:
        return round(total/cantidad, 2)
    else:
        return 0
    
def datos_vehiculo(cant_caracteres, caracteres, patente, vehiculo, pago, pais, distancia):
    if 0 <= cant_caracteres - 1 <= 6:
        patente += caracteres
    elif cant_caracteres - 1 == 7:
        vehiculo = caracteres
    elif cant_caracteres - 1 == 8:
        pago = caracteres
    elif cant_caracteres - 1 == 9:
        pais = caracteres
    elif 10 <= cant_caracteres - 1 <= 12:
        distancia += caracteres
    return patente,vehiculo,pago,pais,distancia

def archivo_telepeaje(nombre,apertura):
    cant_caracteres = 0
    cant_palabra = 0
    cantidad_patentes = 0
    
    # Variables para el lenguaje
    primer_palabra = ''
    idioma = ''
    
    # Variables para saber la cantidad de patentes de los distintos paises y para saber la procedencia del pais junto con la cabina en la que ingreso
    carg, cbol, cbra, cchi, cpar, curu, cotr, procedencia = 0, 0, 0, 0, 0, 0, 0 ,''
    cabina_pais = 0
    
    # Variables para determinar los datos del vehiculo ingresado
    patente,vehiculo,pago,pais,distancia = '','','','',''
    
    # Variable para el importe total acumulado
    imp_acum_total = 0
    
    # Variables para deteccion de la primer patente y su frecuencia
    es_la_primer_patente = True
    primera = ''
    cpp = 1
    
    # Variables para la deteccion del mayor
    mayimp = 0
    maypat = 0

    # Variables para el promedio de los vehiculos Arg que pasan por la cabina Br
    cant_vehiculos_Arg_cabina_Br = 0
    suma_distancia_vehiculos_Arg_cabina_Br = 0
    
    archivo = open(nombre,apertura)
    for caracteres in archivo.read():
        cant_caracteres += 1
        if caracteres != '\n':
            if cant_palabra == 0:
                primer_palabra += caracteres
            elif cant_caracteres > 0: 
                # Deteccion de los datos del vehiculo
                patente, vehiculo, pago, pais, distancia = datos_vehiculo(cant_caracteres, caracteres, patente, vehiculo, pago, pais, distancia)
        elif cant_palabra > 0:
            # Deteccion del idioma
            idioma = lenguaje(primer_palabra)
            
            # Deteccion de la cantidad de patentes de los paises
            carg,cbol,cbra,cchi,cpar,curu,cotr,procedencia = cantidad_patentes_pais(patente,carg,cbol,cbra,cchi,cpar,curu,cotr)
            
            # Incremento del importe total
            base,cabina_pais = cobro(int(pais))
            subtotal = importe_vehiculo(int(vehiculo),base)
            total = forma_pago(int(pago),subtotal)
            imp_acum_total += total
            
            # Determinacion de la frencuencia de la primer patente, primer patente y el mayor importe de una patente
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
            
            # Cantidad total de patentes
            cantidad_patentes = carg + cbol + cbra + cchi + cpar + curu + cotr
            
            # Determinacion de vehiculos Argentinos que pasaron por una cabina brasilera
            if procedencia == 'Argentina' and cabina_pais == 'Brasil':
                cant_vehiculos_Arg_cabina_Br += 1
                suma_distancia_vehiculos_Arg_cabina_Br += float(distancia)
          
            patente,vehiculo,pago,pais,distancia = '', '', '', '', ''
            cant_caracteres = 0
            
        else:
            cant_palabra += 1
            cant_caracteres = 0
        
    archivo.close()
    
    porc = porcentaje(cotr, cantidad_patentes)
    prom = promedio(cant_vehiculos_Arg_cabina_Br,suma_distancia_vehiculos_Arg_cabina_Br)
    
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
    print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de:', cpp)
    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:',maypat)
    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')
    
# Determinar datos al pasar por el telepeaje mediante el documento
archivo_telepeaje ('telepeaje.txt','r')