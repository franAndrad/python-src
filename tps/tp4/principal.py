from procesos import *

def menu():
    opciones = "0. Salir\n"
    opciones += "1. Cargar los datos mediante un archivo CSV\n"
    opciones += "2. Cargar nuevo ticket por teclado\n"
    opciones += "3. Mostrar todos los datos grabados\n"
    opciones += "4. Mostrar registros por patente\n"
    opciones += "5. Buscar un código de ticket\n"
    opciones += "6. Contar combinaciones entre tipo de vehículo y país de cabina\n"
    opciones += "7. Contar por tipo y país\n"
    opciones += "8. Calcular distancia promedio y mostrar registros filtrados\n"
    imprimir_con_cabecera(opciones, 'MENU DE OPCIONES')
    return input('Ingrese una opción: ')


def principal():
    DOCUMENTO = 'peajes-tp4.csv'
    DOCUMENTO_BINARIO = 'ticket.dat'

    while True:
        opcion = menu()
        if opcion == '0':
            break
        elif opcion == '1':
            cargar_datos_desde_csv(DOCUMENTO, DOCUMENTO_BINARIO)
        elif opcion == '2':
            cargar_nuevo_ticket(DOCUMENTO_BINARIO)
        elif opcion == '3':
            mostrar_registros(DOCUMENTO_BINARIO)
        elif opcion == '4':
            p = input('\nIngresar la patente a buscar: ')
            mostrar_registros_por_patente(DOCUMENTO_BINARIO, p)
        elif opcion == '5':
            c = int(input('\nIngresar código de ticket a buscar: '))
            imprimir_con_cabecera(buscar_ticket_por_codigo(DOCUMENTO_BINARIO, c), 'REGISTRO ENCONTRADO')
        elif opcion == '6':
            matriz_contadora = generar_contador_por_tipo_y_pais(DOCUMENTO_BINARIO)
            mostrar_contador_por_tipo_y_pais(matriz_contadora)
        elif opcion == '7':
            mostrar_cantidad_por_tipo_y_pais(matriz_contadora)
        elif opcion == '8':
            distancia_promedio(DOCUMENTO_BINARIO)
        else:
            print('¡Ingrese una opción válida!')


if __name__ == '__main__':
    principal()
