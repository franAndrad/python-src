import tickets
import validacion


######### OPCION 1 ########

def cargar_tickets(vector_tickets, docfile):
    archivo = open(docfile, 'rt')
    timestap = archivo.readline()

    while True:
        linea = archivo.readline()
        if linea == '' or linea == '\n':
            break
        
        id = int(linea[0:10])
        patente = linea[10:17]
        tipo_vehiculo = int(linea[17])
        forma_pago = int(linea[18])
        cabina_pais = int(linea[19])
        km_recorrido = int(linea[20:23])
        
        vector_tickets.append(tickets.Ticket(id,patente,tipo_vehiculo,forma_pago,cabina_pais,km_recorrido))
        
    archivo.close()




######### OPCION 2 ########

def cargar_nuevo_ticket(vector_tickets):
    
    id = int(input('\nIngrese una id: '))
    while validacion.id(id):
        print("\nIngrese una id valida\n")
        id = int(input('Ingrese una id: '))
    
    patente = input('\nIngrese la patente: ')
    while validacion.patente(patente):
        print("\nIngrese una patente valida\n")
        patente = input('Ingrese la patente: ')
        
    tipo_vehiculo = int(input('\nIngrese el tipo de vehiculo: '))
    while validacion.tipo_vehiculo(tipo_vehiculo):
        print("\nIngrese un tipo de vehiculo valido\n")
        tipo_vehiculo = int(input('Ingrese el tipo de vehiculo: '))
        
    forma_pago = int(input('\nIngrese la forma de pago: '))
    while validacion.forma_pago(forma_pago):
        print("\nIngrese una forma de pago valida\n")
        forma_pago = int(input('\nIngrese la forma de pago: '))
        
    cabina_pais = int(input('\nIngrese el pais de la cabina donde se hizo el cobro: '))
    while validacion.cabina_pais(cabina_pais):
        print("\Ingrese un pais de cobro valido\n")
        cabina_pais = int(input('\nIngrese el pais de la cabina donde se hizo el cobro: '))

    km_recorrido = int(input('\nIngrese la distancia en km desde la ultima cabina: '))
    while validacion.distancia(km_recorrido):
        print("\Ingrese una distancia en km valida")
        km_recorrido = int(input('\nIngrese la distancia en km desde la ultima cabina: '))

    vector_tickets.append(tickets.Ticket(id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido))




######### OPCION 3 ########

def ordenamiento_secuencial(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i].id > vector[j].id:
                vector[i], vector[j] = vector[j], vector[i]
# Funcion para mostrar el vector registro 

def mostrar_tickets(vector_tickets,ordenar=0): # mostrar(vector, 0:desordenado 1:ordenado mayor a menor, )
    print("\n\nRegistro de tickets\n")
    
    if ordenar == 1:
        ordenamiento_secuencial(vector_tickets)
    for ticket in vector_tickets:
        print(ticket)
        
       
       
        
######### OPCION 4 ########

def buscar(vector_tickets,patente,cabina_pais):
    for ticket in vector_tickets:
        if ticket.patente == patente.upper() and ticket.cabina_pais == cabina_pais:
            return ticket
    return '\nNo se encontro ninguna patente para esta cabina!\n'                
   
   
   
   
 ######### OPCION 5 ########

def modificar_forma_pago(vector_tickets,id):
    for ticket in vector_tickets:
        if ticket.id == id:
            print (ticket.forma_pago)
            if ticket.forma_pago == 1:
                ticket.forma_pago = 2
            else:
                ticket.forma_pago = 1
            return '\nSe cambio la forma de pago para la id '+ str(ticket.id)
    return '\nNo se encontro la id ingresada!\n'
         
         




 ######### OPCION 6 ######## 
def origen_patentes_pais(patente):
    is_c_vacio = False
    if patente[0] == ' ':
        is_c_vacio = True

    if len(patente) == 7:
        if patente[0].isnumeric() or patente[1].isnumeric():
            return 6
        elif patente[2].isnumeric() and not patente[5].isnumeric() and not patente[6].isnumeric():
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
        base, cabina_pais = cobro(ticket.cabina_pais)
        subtotal = importe_vehiculo(ticket.tipo_vehiculo, base)
        total = forma_pago(ticket.forma_pago, subtotal)
        # Acumulo en base al total calculador (cabina+tipo_vehiculo+forma_pago)
        vector_acumulador[ticket.tipo_vehiculo] += total
    return vector_acumulador



######### OPCION 9
def distancias_acumulada(vector_ticket):
    acum = 0
    for ticket in vector_ticket:
        acum += ticket.km_recorrido
    return acum

def cantidad_mayores(a,vector_ticket):
    cant = 0
    for ticket in vector_ticket:
        if ticket.km_recorrido > a:
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
            cabina_pais = int(input("\n Ingrese el pais de la cabina donde se hizo el cobro: "))
            mensaje = buscar(vector_tickets, patente ,cabina_pais)
            print(mensaje)
    
        if op == 5:
            id = int(input("\nIngrese el codigo de la patente a cambiar su forma de pago: "))
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
        
        
        
        # Desde aqui hacia abajo se puede optimizar        
        if op == 8:
            if len(vector_acumulador) > 0:
                mayor = max(vector_acumulador)
                for i in range(len(vector_acumulador)):
                    total += vector_acumulador[i]
                porcentaje = mayor * 100 // total
                
                print('\nMayor:',mayor)
                print('Porcentaje:',porcentaje + ' %')
            else:
                print('\nNescesita primero obtener el vector acumulador en la opcion 7')
                
        if op == 9:
            
            # Consultar sobre la consigna ¿Cual es la última cabina recorrida?
            acumulador_distancias = distancias_acumulada(vector_tickets)
            ultimo = vector_tickets[-1].km_recorrido
            
            if acumulador_distancias > 0:
                promedio = ultimo // acumulador_distancias    
                cant_may = cantidad_mayores(promedio,vector_tickets)
                print('\nEl promedio es de: ',promedio)
                print('La cantidad de valores mayores que el promedio son: ',cant_may)
            
            else:
                print('Debe ingresar valores de tickets!')
            
            
if __name__ == '__main__':
    main()
    
# Consultar si al mostrar el vector ordenado se tienen que ordenar el arreglo o hacer una copia del mismo