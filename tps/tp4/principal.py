from procesos import *


def menu():
    print("\nMenu de opciones:")
    print("0. Salir")
    print("1. Cargar los datos mediante un archivo CSV")
    print("2. Cargar nuevo ticket por teclado")
    print("3. Mostrar todos los datos grabados")
    print("4. Mostrar registros por patente")
    print("5. Buscar un código de ticket")
    print("6. Contar combinaciones entre tipo de vehículo y país de cabina")
    print("7. Contar por tipo y país")
    print("8. Calcular distancia promedio y mostrar registros filtrados")
    return input('Ingrese una opcion: ')


def principal():
    DOCUMENTO = 'peajes-tp4.csv'
    DOCUMENTO_BINARIO = 'ticket.dat'

    while True:
        opcion = menu()
        if opcion == '0':
            break
        elif opcion == '1':
            cargar_datos_desde_csv(DOCUMENTO)
        elif opcion == '2':
            cargar_nuevo_ticket(DOCUMENTO)
        elif opcion == '3':
            mostrar_registros(DOCUMENTO_BINARIO)
        elif opcion == '4':
            mostrar_registros_por_patente(DOCUMENTO_BINARIO)
        elif opcion == '5':
            buscar_ticket_por_codigo(DOCUMENTO_BINARIO)
        elif opcion == '6':
            matriz_contadora = generar_contador_por_tipo_y_pais(DOCUMENTO_BINARIO)
            mostrar_contador_por_tipo_y_pais(matriz_contadora)
        elif opcion == '7':
            mostrar_cantidad_por_tipo_y_pais(matriz_contadora)
        elif opcion == '8':
            distancia_promedio(DOCUMENTO_BINARIO)
        else:
            print('Ingrese una opcion valida!')


if __name__ == '__main__':
    principal()
