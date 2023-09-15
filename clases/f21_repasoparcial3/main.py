import random
import registro

def validar_n():
    while True:
        n = int(input('Ingrese la cantidad de ventas: '))
        if n > 0:
            return n
        else:
            print('Ingrese un valor positivo! \n')

def carga_automatica(vec):
    n = validar_n()
    tipo_facturas = 'A', 'B', 'C', 'E' 
    apellidos = 'Andrade', 'Villalba', 'Bottero'
    
    for i in range(n):
        numero = random.randint(1, n)
        importe = random.randint(0, 199999)
        tipo_factura = random.choice(tipo_facturas)
        apellido = random.choice(apellidos)
        tipo_perfume = random.randint(1,17)
        vec.append(registro.Factura(numero, importe, tipo_factura, apellido, tipo_perfume)) 

def ordenar_mayor_a_menor(vec):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].apellido_persona < vec[j].apellido_persona:
                vec[i],vec[j] = vec[j],vec[i] 

def mostrar_tickets(num,tipo,vec):
    for ticket in vec:
        if ticket.importe > num and ticket.tipo_factura != tipo:
            print(ticket)
   
def importe_acumulado(vec):
    vec_acum = 17 * [0]
    for ticket in vec:
        vec_acum[ticket.tipo_perfume-1] += ticket.importe
    return vec_acum

def mostrar_tickets_por_rango_y_tipo(min, max, tipo_factura, vec_ticket):
   
    encontro = False
    for ticket in vec_ticket:
        if min < ticket.tipo_perfume < max and ticket.tipo_factura != tipo_factura:
            print(' Numero:',ticket.numero,'  Apellido:',ticket.apellido_persona,'  Importe:',ticket.importe)
            encontro = True  
    if not encontro:
        print('No hubo ninguna factura entre esos rangos de importe, ni tipo de factura!')


def buscar_por_numero_y_un_minimo_importe(vec,n,p):
    econtro = False
    for ticket in vec:
        if ticket.numero == n and ticket.importe < p:
            print(ticket)
            econtro = True
    if not econtro:
        print('No hubo ninguna factura con ese numero, ni un valor menor al ingresado!')
            
            
def principal():
    
    vec_ticket = []
    
    random.seed(1)
    
    while True:
        
        print('')
        print('0. Salir')
        print('1. Cargar facturas automaticamente')
        print('2. Mostrar facturas con un importe mayor y un tipo distinto al ingresar')
        print('3. Mostrar el importe total de un tipo de perfume')
        print('4. Mostrar una factura con tipo de perfume entre 5 y 12, que no sea de factura C')
        print('5. Buscar factura mediante su numero y un importe maximo')
        print('')
        
        op = input('Ingrese una opcion: ')
        
        if op == '0':
            break
        
        elif op == '1':
            carga_automatica(vec_ticket)
            print('Carga realizada con exito!')
            
        elif op == '2':
            importe = int(input('Ingrese el importe de factura desde el que se desea mostrar: '))
            tipo = input('Ingrese el tipo de factura que no se desea mostrar: ')
            ordenar_mayor_a_menor(vec_ticket)
            mostrar_tickets(importe,tipo,vec_ticket) 
            
        elif op == '3':
            z = int(input('Ingrese el tipo de perfume a calcular su importe acumulado (1 a 17): '))
            vec_importe_acumulado = importe_acumulado(vec_ticket)
            print('El importe acumulado para el tipo de perfume',z,'es',vec_importe_acumulado[z-1])
        
        elif op == '4':
            mostrar_tickets_por_rango_y_tipo(5,12,'C',vec_ticket)
            
        elif op == '5':
            num = int(input('Ingrese el numero de factura a buscar: '))
            max_importe = int(input('Ingrese el valor maximo de importe a mostrar: '))
            buscar_por_numero_y_un_minimo_importe(vec_ticket, num, max_importe)

        else:
            print('Ingrese un valor correcto!')

if __name__ == '__main__':
    principal()