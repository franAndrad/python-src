import os
import clase
import pickle


def cargar_datos_desde_csv(fd, fdb):

    if not os.path.exists(fd):
        print('El documento', fd, 'no existe!')
    else:
        # Se puede abrir dos documentos asi?
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

            ticket = clase.Ticket(id, patente, tipo_vehiculo, forma_pago, cabina_pais, km_recorrido)
            pickle.dump(ticket, b)
        
        b.close()
        m.close()
        print('Se generó el archivo binario de tickets\n')

def cargar_nuevo_ticket(fd):
    pass


def mostrar_registros(fd):
    m = open(fd, 'rb')
    while m.tell() < os.path.getsize(fd):
        ticket = pickle.load(m)
        print(ticket)


def mostrar_registros_por_patente(fd):
    pass


# Preguntar si hay que mostrar al encontrar o en una funcion aparte
def buscar_ticket_por_codigo(fd):
    pass


def generar_contador_por_tipo_y_pais(fd):
    pass


def mostrar_contador_por_tipo_y_pais(matriz):
    pass


def mostrar_cantidad_por_tipo_y_pais(matriz):
    pass


def distancia_promedio(fd):
    pass
