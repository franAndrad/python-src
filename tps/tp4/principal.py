from procesos import *


def menu():
    opciones = "0. Salir\n" \
                "1. Cargar los datos mediante un archivo CSV\n" \
                "2. Cargar nuevo ticket por teclado\n" \
                "3. Mostrar todos los datos grabados\n" \
                "4. Mostrar registros por patente\n" \
                "5. Buscar un código de ticket\n" \
                "6. Contar combinaciones entre tipo de vehículo y país de cabina\n" \
                "7. Contar por tipo y país\n" \
                "8. Calcular distancia promedio y mostrar registros filtrados\n"
    imprimir_con_cabecera(opciones, 'MENU DE OPCIONES')
    return input('Ingrese una opción: ')


def principal():
    documento = 'peajes-tp4.csv'
    documento_binario = 'ticket.dat'
    matriz_contadora = []

    while True:
        opcion = menu()
        if opcion == '0':
            break
        elif opcion == '1':
            cargar_datos_desde_csv(documento, documento_binario)
        elif opcion == '2':
            cargar_nuevo_ticket(documento_binario)
        elif opcion == '3':
            mostrar_registros(documento_binario)
        elif opcion == '4':
            p = input('\nIngresar la patente a buscar: ')
            mostrar_registros_por_patente(documento_binario, p)
        elif opcion == '5':
            c = int(input('\nIngresar código de ticket a buscar: '))
            imprimir_con_cabecera(buscar_ticket_por_codigo(documento_binario, c), 'REGISTRO ENCONTRADO')
        elif opcion == '6':
            matriz_contadora = generar_contador_por_tipo_y_pais(documento_binario)
            mostrar_contador_por_tipo_y_pais(matriz_contadora)
        elif opcion == '7':
            if len(matriz_contadora) != 0:
                mostrar_cantidad_totalizada(matriz_contadora, 'pais')
                mostrar_cantidad_totalizada(matriz_contadora, 'tipo')
            else:
                imprimir_con_cabecera('Primero debe contar combinaciones entre tipo de vehículo y país de cabina (opcion 6)', 'ERROR')
        # elif opcion == '8':
        #     distancia_promedio(documento_binario)
        else:
            print('¡Ingrese una opción válida!')


if __name__ == '__main__':
    principal()
