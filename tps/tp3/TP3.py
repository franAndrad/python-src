import tickets
import validacion

def cargar_tickets(registro_tickets,docfile):
    
    cont_lineas = 0
    archivo = open(docfile, 'rt')
    timestap = archivo.readline()

    while True:
        linea = archivo.readline()
        if linea == '' or linea == '\n':
            break
        # Este contador me sirve para saber la cantidad de registros
        
        id = int(linea[0:10])
        patente = linea[10:17]
        tipo_vehiculo = int(linea[17])
        forma_pago = int(linea[18])
        cabina_pais = int(linea[19])
        km_recorrido = int(linea[20:23])
        
        registro_tickets.append(tickets.Ticket(id,patente,tipo_vehiculo,forma_pago,cabina_pais,km_recorrido))
        
    archivo.close()

def cargar_nuevo_ticket(vector_tickets):
    
    
    
    id = int(input('Ingrese una id: '))
    # patente = input('Ingrese la patente: ')
    # tipo_vehiculo = int(input('Ingrese el tipo de vehiculo: '))
    # forma_pago = int(input('Ingrese la forma de pago: '))
    # cabina_pais = int(input('Ingrese una la cabina del pais: '))
    # km_recorrido = int(input('Ingrese la cantidad de kilometros recorridos: '))
    
    while validacion.id(id):
        id = int(input('Ingrese una id: '))
        
    
# Funcion para mostrar el vector registro 
def mostrar_tickets(vector_tickets,ordenar=0,tipo=0): # mostrar(vector, 0:desordenado 1:ordenado, 0:mayor-menor 1:menor-mayor)
    if ordenar == 0 and tipo == 0:
        for ticket in vector_tickets:
            print(ticket)
    
    
def main():
   
    op = None
    vector_tickets = []
    
    while op != 0:
        print('')
        print('0.Salir')
        print('1.Crear el arreglo de registros')
        print('2.Cargar por teclado los datos de un ticket')
        print('3.Mostrar todos los registros del arreglo, ordenados por código de ticket, de menor a mayor')
        op = int(input('\nIngrese una opcion: '))

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
            mostrar_tickets(vector_tickets)
    
if __name__ == '__main__':
    main()
    
