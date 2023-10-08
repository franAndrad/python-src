import os
import pickle
from clase import *
from validacion import *

def imprimir_con_cabecera(dato,cabecera):
    cant_caracteres = 130
    print('\n\n')
    print(cant_caracteres * '=')
    cabecera = "{:^{}}".format(cabecera, cant_caracteres)
    print(cabecera)
    print(cant_caracteres * '=')
    print(dato)
    print(cant_caracteres * '=')
    print('\n')


# Falta agregar advertencia si el fd existe
def cargar_datos_desde_csv(fd, fdb):
    validar_existencia_archivo(fd)
    
    if os.path.exists(fdb):
        while True:
            datos = '\nEl archivo ' + str(fdb) + ' existe. ¿Desea sobrescribirlo? \n0: Cancelar\n1: Aceptar\n'
            imprimir_con_cabecera(datos, 'MENSAJE')
            
            op = input('Ingrese una opción: ')
            if op == '0':
                imprimir_con_cabecera('El archivo no se sobrescribió', 'MENSAJE')
                return
            elif op == '1':
                break
            else:
                print('Ingrese una opción válida. Intenta de nuevo.')

    m = open(fd, 'rt')
    b = open(fdb, 'wb')

    timestap = m.readline()
    cabecera = m.readline()

    for linea in m:
        linea = linea[:-1]
        ticket = linea.split(',')

        id = int(ticket[0])
        patente = ticket[1]
        tipo_vehiculo = int(ticket[2])
        forma_pago = int(ticket[3])
        cabina_pais = int(ticket[4])
        km_recorrido = int(ticket[5])

        ticket = Ticket(id, patente, tipo_vehiculo,
                        forma_pago, cabina_pais, km_recorrido)
        pickle.dump(ticket, b)

    b.close()
    m.close()
    imprimir_con_cabecera('Se generó el archivo binario de tickets', 'MENSAJE')


def cargar_nuevo_ticket(fd):
    validar_existencia_archivo(fd)

    m = open(fd, 'ab')
    id = validaciones('\nIngrese el número identificador del ticket', 1)
    patente = validar_tamaño_mayor_0('Ingrese la patente: ').upper()
    tipo_vehiculo = validaciones('Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión)', 0, 2)
    forma_pago = validaciones('Ingrese la forma de pago (1: manual, 2: telepeaje)', 1, 2)
    cabina_pais = validaciones('Ingrese la cabina del país (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)', 0, 4)
    km_recorridos = validaciones('Ingrese los kilómetros recorridos', 0)
    pickle.dump(Ticket(id, patente, tipo_vehiculo,
                forma_pago, cabina_pais, km_recorridos), m)
    m.close()
    imprimir_con_cabecera('Se cargó un nuevo ticket al archivo binario.', 'MENSAJE')



def mostrar_registros(fd):
    validar_existencia_archivo(fd)

    t = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < t:
        ticket = pickle.load(m)
        print(ticket)
    print('\n\n')


def mostrar_registros_por_patente(fd, p):
    validar_existencia_archivo(fd)
    
    m = open(fd, 'rb')
    c = 0
    t = os.path.getsize(fd)
    respuesta = ''
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.patente == p.upper():
            respuesta += str(ticket) +'\n'
            c += 1
    m.close()
    
    respuesta += '\nLa cantidad de veces que aparece esta patente es: ' + str(c)
    imprimir_con_cabecera(respuesta, 'REGISTROS ECONTRADOS')

def buscar_ticket_por_codigo(fd, c):
    validar_existencia_archivo(fd)
    
    t = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.id == c:
            return ticket
    return 'Código no encontrado'


def generar_contador_por_tipo_y_pais(fd):
    pass


def mostrar_contador_por_tipo_y_pais(matriz):
    pass


def mostrar_cantidad_por_tipo_y_pais(matriz):
    pass


def distancia_promedio(fd):
    pass
