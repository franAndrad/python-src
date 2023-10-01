import os
import pickle
from registro_c import *
DEPORTE = 'Natacion', 'Basquet', 'Karate', 'Futbol', 'Patin'  


def menu():
    print('')
    print('1.')
    print('2.')
    print('3.')
    print('4.')
    print('')
    return int(input('Ingrese una opcion: '))


def obtener_vector(fd):
    if not os.path.exists(fd):
        print('No existe el archivo!')
        return
    
    vec_socios = []
    m = open( fd, 'rb')
    while m.tell() < os.path.getsize(fd):
        vec_socios.append(pickle.load(m)) 
    m.close()
    
    return vec_socios
    

def mostrar_vector(v):
    for socio in v:
        print(socio)


def buscar_socio(v, socio, deporte):
    for i in range(len(v)):
        if v[i].socio == socio and v[i].deporte == deporte:
            return i
    return -1


def generar_morosos(v,fd):    
    m = open(fd, 'wt')
    for socio in v:
        if socio.dia == 0:
            m.write(socio.a_csv() + "\n")
    m.close()

def modificar_agregar_socio(v, i, socio, deporte):  
    dia = int(input('Ingrese el dia: '))
    pago = int(input('Ingrese el valor de pago: '))
    if i != -1:
        v[i].dia = dia
        v[i].pago = pago
        return 'Se modifico el dia a ' + str(dia) +  ' y el valor de pago a ' + str(pago)
     
    else:
        posicion = DEPORTE.index(deporte)
        v.append(Cuota(socio,posicion,dia,pago))
        return 'Se agrego un nuevo socio al registro'


def determinar_total_por_deporte(v):
    vec_acum = 5*[0]
    
    for socio in v:
        vec_acum[socio.deporte] += socio.valor_cuota

    print('\nEl total por deporte es: ')
    for i in range(len(vec_acum)):
        print(DEPORTE[i] + ': $' + str(vec_acum[i]))


def determinar_participante_por_deporte(v):
    vec_cont = 5*[0]
    
    for socio in v:
        vec_cont[socio.deporte] += 1
    
    mayor = max(vec_cont)
    indice = vec_cont.index(mayor)
    
    print('El deporte con mas participantes es', DEPORTE[indice], 'con', mayor, 'participantes')


def grabar_vector(vec, fd):

    m = open(fd, 'wb')
    for registro in vec:
        pickle.dump(registro, m)
    m.close
    
    

def principal():
    while True:
        op = menu()
        
        if op == 1:
            vec = obtener_vector('cuotas.dat')
            mostrar_vector(vec)
            
        elif op == 2:
            socio = int(input('Ingrese el socio a buscar:'))
            deporte = input('Ingrese el deporte a buscar:')
            indice = buscar_socio(vec, socio, deporte)
            respuesta = modificar_agregar_socio(vec, indice, socio, deporte)
            print(respuesta)
            
        elif op == 3:
            generar_morosos(vec, 'morosos.csv')
            print('Se genero un documento con los morosos!')
        elif op == 4:
            determinar_total_por_deporte(vec)
            determinar_participante_por_deporte(vec)
        elif op == 5:
            grabar_vector(vec, 'cuotas.dat')
            print('Se guardaron los cambios en cuotas.dat')
            


if __name__ == '__main__':
    principal()