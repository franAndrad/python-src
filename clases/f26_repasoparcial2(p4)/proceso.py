import random
from clase import *

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
        elif dni <= v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        return c
    return -1
    