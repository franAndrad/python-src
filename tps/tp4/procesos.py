import pickle
from clase import *
from validacion import *
import io


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
    """
    Genera un contador de vehículos por tipo y país a partir de un archivo binario.

    Parámetros:
        fd (str): Ruta del archivo binario.

    Retorno:
        list: Una matriz de contadores por tipo y país.
    """
    
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
    """
    Muestra el contador de vehículos por tipo y país.

    Parámetros:
        matriz (list): Una matriz de contadores por tipo y país.

    Retorno:
        None
    """
    
    r = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            r += 'Para el tipo de vehículo ' + str(j)
            r += ' y para el país de cabina ' + str(i)
            r += ' hay un total de ' + str(matriz[i][j]) + ' vehículos\n'
    imprimir_con_cabecera(r, 'CANTIDAD DE VEHÍCULOS POR TIPO Y PAÍS DE CABINA')


def mostrar_cantidad_totalizada(matriz, recorrer): 
    """
    Muestra la cantidad totalizada de vehículos por país o tipo y genera un informe.

    Parámetros:
        matriz (list): Una matriz de contadores por tipo y país.
        recorrer (str): La opción para recorrer la matriz. Puede ser 'pais' o 'tipo'.

    Retorno:
        None
    """
    
    tipos = 'Motocicleta', 'Auto', 'Camión'
    paises = 'Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay'
    r = ''
    a, b = 0, 0

    if recorrer == 'pais':
        a, b = len(matriz), len(matriz[0])
    elif recorrer == 'tipo':
        a, b = len(matriz[0]), len(matriz)
    
    ac = 0
    if recorrer == 'pais':
        for i in range(a):
            for j in range(b):
                ac += matriz[i][j]
            r += 'Para el país de la cabina ' + paises[i] + ' hay un total de ' + str(ac) + ' vehículos\n'
    elif recorrer == 'tipo':
        for i in range(a):
            for j in range(b):
                ac += matriz[j][i]
            r += 'Para el tipo de vehículo ' + tipos[i] + ' hay un total de ' + str(ac) + ' vehículos\n'    
    
    imprimir_con_cabecera(r, 'TOTAL DE VEHICULOS')


def ordenamiento_shell_sort(v):
    """
    Ordena la lista de objetos v utilizando el algoritmo de Shell Sort.

    Parametros:
        v (list): Lista de objetos a ordenar.

    Retorno:
        None
    """
    
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
        
    while h > 0:
        for j in range(h, n):
            y = v[j].km_recorrido
            atributo = v[j]
            k = j - h
            while k >= 0 and y < v[k].km_recorrido:
                v[k+h] = v[k]
                k -= h
            v[k+h] = atributo
        h //= 3    


def distancia_promedio(fdb):
    """
    Calcula la distancia promedio de los registros en un archivo y devuelve una lista
    de registros cuya distancia es mayor que el promedio y el valor promedio.

    Parametros:
        fdb (str): Nombre del archivo de base de datos.

    Retorno:
        tuple: Una tupla que contiene una lista de registros con distancias mayores al promedio
               y el valor del promedio.
        int: Un numero entero con el valor promedio de las distancias recorridas
    """
    
    validar_existencia_archivo(fdb)
    
    v = []
    cantidad, suma = 0, 0
    
    m = open(fdb, 'rb')
    t = os.path.getsize(fdb)
    while m.tell() < t:
        ticket = pickle.load(m)
        suma += ticket.km_recorrido
        cantidad += 1
    
    promedio = suma // cantidad 
    m.seek(0, io.SEEK_SET)
    
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.km_recorrido > promedio:
            v.append(ticket)
    
    m.close()
    return v, promedio


def mostrar_registros_mayores_distancia_promedio(v, promedio):
    """
    Muestra los registros cuya distancia es mayor que el promedio.

    Parametros:
        v (list): Lista de registros a mostrar.
        promedio (int): Valor de la distancia promedio.

    Retorno:
        None
    """
    
    ordenamiento_shell_sort(v) 
    
    r = ''
    for ticket in v:
        r += str(ticket) + '\n'
    r += '\nLa distancia promedio del registro fue de ' + str(promedio) + ' km\n'

    imprimir_con_cabecera(r, 'REGISTROS MAYORES AL PROMEDIO')
   
