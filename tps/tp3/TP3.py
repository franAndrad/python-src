from tickets import *
def main():

    op = None
    vector_tickets = []
    
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
        op = input('\nIngrese una opcion: ')
        
        if validacion_solo_digitos(op):
            if validacion_rango(1, 9, int(op)):
                if op == '1':
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

                if op == '2':
                    cargar_nuevo_ticket(vector_tickets)

                if op == '3':
                    mostrar_tickets(vector_tickets, 1)

                if op == '4':
                    patente = input("\nIngrese la patente a buscar: ")
                    cabina_pais = input(
                        "\nIngrese el pais de la cabina donde se hizo el cobro: ")
                    mensaje = buscar(vector_tickets, patente, cabina_pais)
                    print(mensaje)

                if op == '5':
                    id = input(
                        "\nIngrese el codigo de ticket a cambiar su forma de pago: ")
                    mensaje = modificar_forma_pago(vector_tickets, id)
                    print(mensaje)

                if op == '6':
                    vector_conteo = vehiculos_por_cabina_pais(vector_tickets)
                    paises = 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro'
                    print('\nCantidad de vehiculos de cada pais que pasaron por las cabinas:')
                    for i in range(len(vector_conteo)):
                        print("{:<{}}".format(
                            str(paises[i]), 10) + ':', vector_conteo[i])

                if op == '7':
                    vector_acumulador = []
                    vector_acumulador = importe_acumulado_por_pagos(vector_tickets)
                    vehiculos = 'Motocicleta', 'Automóvil', 'Camión'
                    print('\nImporte acumulado por tipo de vehiculo:')
                    for i in range(len(vector_acumulador)):
                        print("{:<{}}".format(
                            str(vehiculos[i]), 12), ':', vector_acumulador[i])

                if op == '8':
                    mensaje = obtener_porcentaje_mayor(vector_tickets)
                    print(mensaje)

                if op == '9':
                    mensaje = obtener_promedio_distancia_mayor_promedio(vector_tickets)
                    print(mensaje)
            
            else:
                print('\nIngrese una opcion valida!')
                continue
        else:
            print('\nIngrese una opcion valida!')
            continue
            
if __name__ == '__main__':
    main()