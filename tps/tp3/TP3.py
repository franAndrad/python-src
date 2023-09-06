import tickets

######### OPCION 1 ########
def cargar_tickets(vector_tickets, docfile):
    archivo = open(docfile, 'rt')
    timestap = archivo.readline()

    while True:
        linea = archivo.readline()
        if linea == '' or linea == '\n':
            break
        
        id = linea[0:10]
        patente = linea[10:17]
        tipo_vehiculo = linea[17]
        forma_pago = linea[18]
        cabina_pais = linea[19]
        km_recorrido = linea[20:23]
        
        vector_tickets.append(tickets.Ticket(id,patente,tipo_vehiculo,forma_pago,cabina_pais,km_recorrido))
        
    archivo.close()

######### OPCION 2 ########
def validacion_rango(a, b, var):
    if a <= var <= b:
        return True
    return False
def validacion_solo_digitos(vector):
    tam = len(vector)
    cont_digit = 0
    for i in vector:
        if i.isdigit():
            cont_digit += 1
    if cont_digit == tam:
        return True
    return False
def cargar_nuevo_ticket(vector_tickets):
    
    # Validacion de que sean solo digitos y y este entre 1 y 9999999999 incluidos
    id = input('\nIngrese una id: ')
    while True:
        if validacion_solo_digitos(id): 
            if validacion_rango(1, 9999999999, int(id)):
                break
            else:
                print("\nIngrese una id valida\n")
                id = input('Ingrese una id: ')
        else:
            print("\nIngrese una id valida\n")
            id = input('Ingrese una id: ')
            

    # Valida que la patente tenga 7 digitos y si tiene 6 le agrega un espacio al comienzo
    patente = input('\nIngrese la patente: ').replace(' ', '')
    while True:
        if validacion_rango(6,7,len(patente)):
            break
        else: 
            print("\nIngrese una patente valida\n")
            patente = input('Ingrese la patente: ').replace(' ', '')
    if len(patente) == 6:
        patente = ' ' + patente
    
    # Valida que sean solo digitos y que este entre 0 y 2 incluidos
    tipo_vehiculo = input('Ingrese el tipo de vehiculo: ')
    while True:
        if validacion_solo_digitos(tipo_vehiculo):
            if validacion_rango(0,2,int(tipo_vehiculo)):
                break
            else:
                print("\nIngrese un tipo de vehiculo valido\n")
                tipo_vehiculo = input('Ingrese el tipo de vehiculo: ')
        else:
            print("\nIngrese un tipo de vehiculo valido\n")
            tipo_vehiculo = input('Ingrese el tipo de vehiculo: ')
            
    # Valida que sean solo digitos y que este entre 1 y 2 incluidos    
    forma_pago = input('Ingrese la forma de pago: ')
    while True:
        if validacion_solo_digitos(forma_pago):
            if validacion_rango(1,2,int(forma_pago)):
                break
            else:
                print("\nIngrese una forma de pago valida\n")
                forma_pago = input('Ingrese la forma de pago: ')
        else:
            print("\nIngrese una forma de pago valida\n")
            forma_pago = input('Ingrese la forma de pago: ')
    
    # Valida que sean solo digitos y que este entre 0 y 4 incluidos
    cabina_pais = input('Ingrese el pais de la cabina donde se hizo el cobro: ')
    while True:
        if validacion_solo_digitos(cabina_pais):
            if validacion_rango(0,4,int(cabina_pais)):
                break
            else:
                print("\nIngrese un pais de cobro valido\n")
                cabina_pais = input('Ingrese el pais de la cabina donde se hizo el cobro: ')
        else:
            print("\nIngrese un pais de cobro valido\n")
            cabina_pais = input('Ingrese el pais de la cabina donde se hizo el cobro: ')

    # Valida que sean solo numeros y si es menor que 100 agrega ceros a la izquierda y lo convierte en cadena
    km_recorrido = input('Ingrese la distancia en km desde la ultima cabina: ')
    while True:
        if validacion_solo_digitos(km_recorrido):
            if validacion_rango(0,999,int(km_recorrido)):
                break
            else:
                print("\nIngrese una distancia en km valida\n")
                km_recorrido = input('Ingrese la distancia en km desde la ultima cabina: ')
        else:
            print("\nIngrese una distancia en km valida\n")
            km_recorrido = input('Ingrese la distancia en km desde la ultima cabina: ')
            
    # Agrega los ceros a la izquierda si el numero es menor que 100
    km_recorrido_3_digitos = f"{int(km_recorrido):03}" 
    
    vector_tickets.append(tickets.Ticket(id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido_3_digitos))

######### OPCION 3 ########

def origen_patentes_pais(patente):
    is_c_vacio = False
    if patente[0] == ' ':
        is_c_vacio = True

    if len(patente) == 7:
        if patente[0].isnumeric() or patente[1].isnumeric():
            return 6
        elif patente[2].isnumeric() and patente[3].isnumeric() and not patente[5].isnumeric() and not patente[6].isnumeric():
            return 0
        elif not is_c_vacio and patente[2].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
            return 1
        elif not is_c_vacio and patente[3].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
            if patente[4].isnumeric():
                return 5
            else:
                return 2
        elif patente[5].isnumeric() and patente[6].isnumeric():
            if not is_c_vacio and patente[4].isnumeric():
                return 4
            elif is_c_vacio and not patente[2].isnumeric() and not patente[3].isnumeric() and not patente[4].isnumeric():
                return 3
            else:
                return 6
        else:
            return 6
    else:
        return 6
def ordenamiento_secuencial(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if int(vector[i].id) > int(vector[j].id):
                vector[i], vector[j] = vector[j], vector[i]
# Funcion para mostrar el vector registro 
def mostrar_tickets(vector_tickets,ordenar=0): # mostrar(vector, 0:desordenado 1:ordenado mayor a menor, )
    print("\n\nRegistro de tickets\n")
    paises = 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro'
    if ordenar == 1:
        ordenamiento_secuencial(vector_tickets)
    for ticket in vector_tickets: 
        print(tickets.Ticket.__str__(ticket) + ' {:<20}'.format(
            'origen patente: ' + paises[origen_patentes_pais(ticket.patente)]))
        
######### OPCION 4 ########
def buscar(vector_tickets,patente,cabina_pais):
    for ticket in vector_tickets:
        if ticket.patente.replace(' ','') == patente.upper().replace(' ','') and ticket.cabina_pais == cabina_pais:
            return ticket
    return '\nNo se encontro ninguna patente para esta cabina!\n'                
   
######### OPCION 5 ########
def modificar_forma_pago(vector_tickets,id):
    for ticket in vector_tickets:
        if ticket.id == id:
            if ticket.forma_pago == 1:
                ticket.forma_pago = 2
            else:
                ticket.forma_pago = 1
            return '\nSe cambio la forma de pago para la id '+ ticket.id
    return '\nNo se encontro la id ingresada!\n'
         
######### OPCION 6 ######## 
# def origen_patentes_pais(patente):
    # is_c_vacio = False
    # if patente[0] == ' ':
    #     is_c_vacio = True
        
    # if len(patente) == 7:
    #     if patente[0].isnumeric() or patente[1].isnumeric():
    #         return 6
    #     elif patente[2].isnumeric() and patente[3].isnumeric() and not patente[5].isnumeric() and not patente[6].isnumeric():
    #         return 0
    #     elif not is_c_vacio and patente[2].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
    #         return 1
    #     elif not is_c_vacio and patente[3].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
    #         if patente[4].isnumeric():
    #             return 5
    #         else:
    #             return 2
    #     elif patente[5].isnumeric() and patente[6].isnumeric():
    #         if not is_c_vacio and patente[4].isnumeric():
    #             return 4
    #         elif is_c_vacio and not patente[2].isnumeric() and not patente[3].isnumeric() and not patente[4].isnumeric():
    #             return 3
    #         else:
    #             return 6
    #     else:
    #         return 6
    # else:
    #     return 6   
def vehiculos_por_cabina_pais(vector_tickets):
    vector_conteo = 7*[0]
    for ticket in vector_tickets:
        vector_conteo[origen_patentes_pais(ticket.patente)] += 1
    return vector_conteo
          
######### OPCION 7 ########
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
        return importe
    elif pago == 2:
        return importe - (10*importe)/100
    else:
        return 0
def importe_acumulado_por_pagos(vector_tickets):
    vector_acumulador = 3*[0]
    for ticket in vector_tickets:
        base, cabina_pais = cobro(int(ticket.cabina_pais))
        subtotal = importe_vehiculo(int(ticket.tipo_vehiculo), base)
        total = forma_pago(int(ticket.forma_pago), subtotal)
        # Acumulo en base al total calculador (cabina+tipo_vehiculo+forma_pago)
        vector_acumulador[int(ticket.tipo_vehiculo)] += total
    return vector_acumulador

######### OPCION 9
def distancias_acumulada(vector_ticket):
    acum = 0
    for ticket in vector_ticket:
        acum += int(ticket.km_recorrido)
    return acum
def cantidad_mayores(a,vector_ticket):
    cant = 0
    for ticket in vector_ticket:
        if int(ticket.km_recorrido) > a:
            cant += 1
    return cant
    
    
def main():

    op = None
    vector_tickets = []
    vector_acumulador = []
    mayor = None
    total = 0
    
    while op != 0:
        print('')
        print('0.Salir')
        print('1.Crear el arreglo de registros')
        print('2.Cargar por teclado los datos de un ticket')
        print('3.Mostrar todos los registros del arreglo, ordenados por código de ticket, de menor a mayor')
        print('4.Buscar una patente que haya pasado por una determinada cabina de un pais')
        print('5.Cambiar la forma de pago mediante un codigo de ticket')
        print('6.Cantidad de vehiculos de cada pais que pasaron por las cabinas')
        print('7.Importe acumulado por pagos de tickets por cada uno de los posibles vehiculos')
        print('8.Vehiculo con mayor monto acumulado y su porcentaje con respecto al total')
        print('9.Distancia promedio desde la ultima cabina recorrida entre todos los vehiculos y los que recorrieron una distancia mayor al promedio')
        op = int(input('\nIngrese una opcion: '))
        
        # ¿Mantenemos las opciones asi o las separamos por funciones?
        if op == 1:
            if len(vector_tickets) > 0:
                
                desicion = None
                while desicion != 1 and desicion != 0: 
                    print('')
                    print('El registro de tickets ya tiene valores, ¿Desea continuar? ')
                    print('0.Cancelar, 1.Aceptar')
                    desicion = int(input('Opcion: '))
                    
                if desicion == 0:
                    continue
                else:
                    cargar_tickets(vector_tickets, 'peajes-tp3.txt')
            else:    
                cargar_tickets(vector_tickets, 'peajes-tp3.txt') 
                
        if op == 2:
            cargar_nuevo_ticket(vector_tickets)
        
        if op == 3:
            mostrar_tickets(vector_tickets,1)
            
        if op == 4:
            patente = input("\nIngrese la patente a buscar: ")
            cabina_pais = input("\nIngrese el pais de la cabina donde se hizo el cobro: ")
            mensaje = buscar(vector_tickets, patente ,cabina_pais)
            print(mensaje)
    
        if op == 5:
            id = input("\nIngrese el codigo de ticket a cambiar su forma de pago: ")
            mensaje = modificar_forma_pago(vector_tickets,id)
            print(mensaje)
        
        if op == 6:
            vector_conteo = vehiculos_por_cabina_pais(vector_tickets)
            paises = 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro'
            print('\nCantidad de vehiculos de cada pais que pasaron por las cabinas:')
            for i in range(len(vector_conteo)):
                print(paises[i],vector_conteo[i])
        
        if op == 7:
            vector_acumulador = importe_acumulado_por_pagos(vector_tickets)
            vehiculos = 'Motocicleta', 'Automóvil', 'Camión'
            print('\nImporte acumulado por tipo de vehiculo:')
            for i in range(len(vector_acumulador)):
                print(vehiculos[i], vector_acumulador[i])
               
        if op == 8:
            if len(vector_acumulador) > 0:
                mayor = max(vector_acumulador)
                for i in range(len(vector_acumulador)):
                    total += vector_acumulador[i]
                porcentaje = mayor * 100 // total
                
                print('\nMayor:',mayor)
                print('Porcentaje:', str(porcentaje) + ' %')
            else:
                print('\nNescesita primero obtener el vector acumulador en la opcion 7')
                
        if op == 9:
            acumulador_distancias = distancias_acumulada(vector_tickets)
            total_vehiculos = len(vector_tickets)
            
            if acumulador_distancias > 0:
                promedio = acumulador_distancias // total_vehiculos    
                cant_may = cantidad_mayores(promedio,vector_tickets)
                print('\nEl promedio es de: ',promedio)
                print('La cantidad de autos con una distancia mayor al promedio son: ',cant_may)           
            else:
                print('\nDebe ingresar valores de tickets!\n')
            
            
if __name__ == '__main__':
    main()