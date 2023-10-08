import pickle
from clase import *
from validacion import *


def imprimir_con_cabecera(dato, cabecera):
    """
    Imprime un mensaje con una cabecera decorativa.

    Parametros:
    dato (str): El contenido del mensaje.
    cabecera (str): El título de la cabecera.

    Retorno:
    None
    """

    cant_caracteres = 130
    print('\n\n')
    print(cant_caracteres * '=')
    cabecera = "{:^{}}".format(cabecera, cant_caracteres)
    print(cabecera)
    print(cant_caracteres * '=')
    print(dato)
    print(cant_caracteres * '=')
    print('\n')


def cargar_datos_desde_csv(fd, fdb):
    """
    Carga datos desde un archivo CSV a un archivo binario.

    Parametros:
    fd (str): Ruta del archivo CSV de entrada.
    fdb (str): Ruta del archivo binario de salida.

    Retorno:
    None
    """

    validar_existencia_archivo(fd)

    if os.path.exists(fdb):
        while True:
            datos = '\nEl archivo ' + \
                str(fdb) + ' existe. ¿Desea sobrescribirlo? \n0: Cancelar\n1: Aceptar\n'
            imprimir_con_cabecera(datos, 'MENSAJE')

            op = input('Ingrese una opción: ')
            if op == '0':
                imprimir_con_cabecera(
                    'El archivo no se sobrescribió', 'MENSAJE')
                return
            elif op == '1':
                break
            else:
                print('Ingrese una opción válida. Intenta de nuevo.')

    m = open(fd, 'rt')
    b = open(fdb, 'wb')

    m.readline()  # Ignorar timestap
    m.readline()  # Ignorar cabecera

    for linea in m:
        linea = linea[:-1]
        ticket = linea.split(',')

        codigo = int(ticket[0])
        patente = ticket[1]
        tipo_vehiculo = int(ticket[2])
        forma_pago = int(ticket[3])
        cabina_pais = int(ticket[4])
        km_recorrido = int(ticket[5])

        ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido)
        pickle.dump(ticket, b)

    b.close()
    m.close()
    imprimir_con_cabecera('Se generó el archivo binario de tickets', 'MENSAJE')


def cargar_nuevo_ticket(fd):
    """
    Carga un nuevo ticket al archivo binario.

    Parameters:
    fd (str): Ruta del archivo binario.
    validar_existencia_archivo(fd)

    Retorno:
    None
    """
    validar_existencia_archivo(fd)

    m = open(fd, 'ab')
    codigo = validaciones('\nIngrese el número identificador del ticket', 1)
    patente = validar_cadena('Ingrese la patente: ').upper()
    tipo_vehiculo = validaciones('Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión)', 0, 2)
    forma_pago = validaciones('Ingrese la forma de pago (1: manual, 2: telepeaje)', 1, 2)
    cabina_pais = validaciones('Ingrese la cabina del país (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)', 0, 4)
    km_recorridos = validaciones('Ingrese los kilómetros recorridos', 0)
    pickle.dump(Ticket(codigo, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorridos), m)
    m.close()
    imprimir_con_cabecera(
        'Se cargó un nuevo ticket al archivo binario.', 'MENSAJE')


def mostrar_registros(fd):
    """
    Muestra todos los registros del archivo binario.

    Parametros:
    fd (str): Ruta del archivo binario.

    Retorno:
    None
    """

    validar_existencia_archivo(fd)

    t = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < t:
        ticket = pickle.load(m)
        print(ticket)
    print('\n\n')


def mostrar_registros_por_patente(fd, p):
    """
    Muestra los registros de un archivo binario con una patente específica.

    Parametros:
    fd (str): Ruta del archivo binario.
    p (str): Patente a buscar.

    Retorno:
    None
    """

    validar_existencia_archivo(fd)

    m = open(fd, 'rb')
    c = 0
    t = os.path.getsize(fd)
    respuesta = ''
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.patente == p.upper():
            respuesta += str(ticket) + '\n'
            c += 1
    m.close()

    respuesta += '\nLa cantidad de veces que aparece esta patente es: ' + str(c)
    imprimir_con_cabecera(respuesta, 'REGISTROS ECONTRADOS')


def buscar_ticket_por_codigo(fd, c):
    """
    Busca un ticket por su código en el archivo binario.

    Parametros:
    fd (str): Ruta del archivo binario.
    c (int): Código del ticket a buscar.

    Retorno:
    Ticket o str: El ticket si se encuentra, o un mensaje de error si no.
    """

    validar_existencia_archivo(fd)

    t = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.codigo == c:
            return ticket
    return 'Código no encontrado'


def generar_contador_por_tipo_y_pais(fd):
    validar_existencia_archivo(fd)

    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    mat = [[0] * 3 for _ in range(5)]
    while m.tell() < t:
        ticket = pickle.load(m)
        ind_fila = ticket.cabina_pais
        ind_columna = ticket.tipo_vehiculo
        mat[ind_fila][ind_columna] += 1
    m.close()
    return mat


def mostrar_contador_por_tipo_y_pais(matriz):
    r = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            r += 'Para el tipo de vehículo ' + str(j)
            r += ' y para el país de cabina ' + str(i)
            r += ' hay un total de ' + str(matriz[i][j]) + ' vehículos\n'
    imprimir_con_cabecera(r, 'CANTIDAD DE VEHÍCULOS POR TIPO Y PAÍS DE CABINA')


def mostrar_cantidad_totalizada(matriz, a, b):
    tipos = 'Motocicleta', 'Auto', 'Camión'
    paises = 'Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay'
    r = ''
    
    ac = 0
    if a == len(matriz):
        for i in range(a):
            for j in range(b):
                ac += matriz[i][j]
            r += 'Para el país de la cabina ' + paises[i] + ' hay un total de ' + str(ac) + ' vehículos\n'
    else:
        for i in range(a):
            for j in range(b):
                ac += matriz[j][i]
            r += 'Para el tipo de vehículo ' + tipos[i] + ' hay un total de ' + str(ac) + ' vehículos\n'    
    
    imprimir_con_cabecera(r, 'TOTAL DE VEHICULOS')


# def distancia_promedio(fd):
#     pass
