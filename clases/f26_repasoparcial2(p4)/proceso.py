import random
from clase import *
import pickle
import os

def validar_n():
    n = int(input('Ingrese la cantidad de profesiones a cargar: '))
    while n <= 0:
        n = int(input('Ingrese la cantidad de profesiones a cargar: '))
    return n


def add_in_order(p, v):
    izq, der, pos = 0, len(v) - 1, 0
    while izq <= der:
        c = (izq + der) // 2
        if p.dni == v[c].dni:
            pos = c
            break
        elif p.dni <= v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [p]


def cargar_profesionales(n, v):
    nombres = 'martina', 'fran',  'ari', 'nico', 'lujan', 'ezequiel'
    for _ in range(n):
        dni = random.randint(16000000,50000000)
        nombre = random.choice(nombres)
        importe = round(random.uniform(1000,10000),2)
        tipo_afiliacion = random.randint(0,4)
        tipo_trabjo = random.randint(0,14)
        profesional = Profesional(dni, nombre, importe, tipo_afiliacion, tipo_trabjo)   
        add_in_order(profesional, v)    


def mostrar_profesionales(v):
    for p in v:
        print(p)


def buscar_dni(dni, v):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if dni == v[c].dni:
            return c
        elif dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return -1


def crear_binario(fd, v):
    m = open(fd, 'wb')
    for profesional in v:
        if 3 <= profesional.tipo_trabjo <= 5:
            pickle.dump(profesional, m)

def mostrar_binario(fd):
    if not os.path.exists(fd):
        print('El documento', fd,  'no existe!')
        return

    m = open(fd,'rb')
    while m.tell() < os.path.getsize(fd):
        print(pickle.load(m))


def busqueda_secuencial(nom ,v):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1

def crear_matriz_contadora_afiliado_trabajo(v):
    #     col               fila
    m = [[0] * 5  for _ in range(15)]

    for profesional in v:
        m[profesional.tipo_trabjo][profesional.tipo_afiliacion] += 1
    return m

def  mostrar_matriz_contadora(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > 0:
                print('para el tipo de afiliado', j, 'y el tipo de trabajo', i, 'hay', m[i][j], 'afiliados')
