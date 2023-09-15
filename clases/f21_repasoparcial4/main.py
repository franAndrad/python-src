import random
import registro

def menu():
    print('')
    print('0. Salir')
    print('1. Cargar ventas automaticamente')
    print('2. Mostrar ventas ordenadas de mayor a menor por monto')
    print('3. Mostrar la clase con mayor recaudacion')
    print('4. Buscar pasajes vendidos de la clase 3 con un monto superior')
    print('5. Buscar pasajero por pasaporte')
    print('')
    return input('Ingrese una opcion: ')

def carga_automatica(vec):
    n = int(input('Ingrese la cantidad de ventas: '))
    
    for i in range(n):
        pasaportes = '1DA4f', '1ACSA' , 'ASDFE' , 'FDSFA'
        nombres = 'Francisco', 'Julian', 'Martin'
        
        pasaporte = random.choice(pasaportes)
        nombre = random.choice(nombres)
        codigo_destino = random.randint(100,103)
        codigo_clase = random.randint(1, 10)
        monto = random.uniform(1, 10000)

        vec.append(registro.Venta(pasaporte, nombre, codigo_destino, codigo_clase, monto))

def ordenar_vector(vec):
    for i in range(len(vec)-1):
        for j in range(i+1,len(vec)):
            if vec[i].monto < vec[j].monto:
                vec[i],vec[j] = vec[j], vec[i]

def mostrar(vec):
    destinos = 'Bahamas', 'Bermudas', 'Puerto Rico', 'Republica dominicana'
    for venta in vec:
        r = ''
        r += ' Pasaporte:' + str(venta.pasaporte)
        r += ' Nombre: ' + str(venta.nombre)
        r += ' Destino: ' + str(destinos[venta.codigo_destino - 100])
        r += ' Monto: ' + str(venta.monto)
        print(r)

def recaudacion_acumulada(vec):
    vec_acum = [0] * 10
    for i in range(len(vec)):
        vec_acum[vec[i].codigo_clase - 1 ] += vec[i].monto
    return vec_acum

def mostrar_recaudaciones(vec):
    for i in range(len(vec)):
        print('Para la clase',i,'el monto es',vec[i])

def determinar_recaudacion_mayor(vec):
    for i in range(len(vec)):
        if i == 0:
            maximo = vec[i]
            pos = i
        elif vec[i] > maximo:
            maximo = vec[i]
            pos = i
    print('El mayor monto es para la clase', pos, 'con: ',maximo)


def promedio_clase_3(vec):
    vec_acum = recaudacion_acumulada(vec)
    cont_clase_3 = 0
    for venta in vec:
        if venta.codigo_clase == 3:
            cont_clase_3 += 1
    
    return vec_acum[2] / cont_clase_3

def mostrar_clase_3_mayor_promedio(prom,vec):
    for venta in vec:
        if venta.monto > prom and venta.codigo_clase == 3:
            print(venta)

def buscar_pasajero(pas,vec):
    for venta in vec:
        if venta.pasaporte == pas:
            return 'Pasajero '+str(venta.nombre)+' por favor concurrir a atencion al cliente'
    return 'No se encontro un pasaje con ese pasaporte'

def principal():
    vec_ventas = []

    while True:

        op = menu()

        if op == '0':
            break
        elif op == '1':
            carga_automatica(vec_ventas)
            print('Datos cargados! \n')
        elif op == '2':
            ordenar_vector(vec_ventas)
            mostrar(vec_ventas)
        elif op == '3':
            vec_recaudacion = recaudacion_acumulada(vec_ventas)
            mostrar_recaudaciones(vec_recaudacion)
            determinar_recaudacion_mayor(vec_recaudacion)
        elif op == '4':
            promedio = promedio_clase_3(vec_ventas)
            mostrar_clase_3_mayor_promedio(promedio,vec_ventas)
        elif op == '5':
            pasaporte = input('Ingrese el pasaporte a buscar: ')
            encontrado = buscar_pasajero(pasaporte,vec_ventas)
            print(encontrado)
        else:
            print('Ingrese una opcion correcta!')

if __name__ == '__main__':
    principal()
