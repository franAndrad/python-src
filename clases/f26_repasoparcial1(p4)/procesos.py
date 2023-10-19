import random
from clase import *
import os
import pickle

def validar_n(msj):
    n = int(input(msj))
    while n <= 0:
        n = int(input(msj))
    return n


def add_in_order(p, v):
    izq, der, pos = 0, len(v) - 1, 0
    while izq <= der:
        c = (izq + der) // 2
        if p.titulo == v[c].titulo :
            pos = c
            break
        elif p.titulo <= v[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [p]
            

def cargar_pelicula(n,v):
    # tipos = 'accion', 'comedia', 'drama', 'terror' #4
    # paises = 'Argentina', 'Brasil', 'Peru', 'Portugal', 'Fracia' #5
    titulos = 'Tit1', 'Tit2', 'Tit3', 'Tit4' #4
    
    for _ in range(n):
        id = random.randint(0, n)
        titulo = random.choice(titulos)
        importe_invertido = round(random.uniform(1,10000),2)
        tipo = random.randint(0, 9)
        pais = random.randint(0, 19)
        pelicula = Pelicula(id, titulo, importe_invertido, tipo, pais)
        
        add_in_order(pelicula, v)
        

def mostrar_peliculas(v):
    for pelicula in v:
        print(pelicula)
    print()
    

def buscar_por_titulo(t,v):
    izq, der = 0,  len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if t == v[c].titulo:
            return c
        elif t < v[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    return -1


def crear_binario(fd, i, v):
    m = open(fd, 'wb')
    for p in v:
        if p.pais != 10 and p.importe_invertido < i:
            pickle.dump(p, m)     
    
def mostrar_binario(fd):
    if not os.path.exists(fd):
        print('No existe el archivo con el nombre', fd)
        return
    
    m = open(fd, 'rb')
    while m.tell() < os.path.getsize(fd):
        print(pickle.load(m))
    print()

def buscar_por_id(id, v):
    for i in range(len(v)):
        if v[i].id == id:
            return i
    return -1 

def crear_matriz_tipo_pais(v):
    #     columnas           filas
    m = [[0] * 10 for _ in range(20)]
    for p in v:
        m[p.pais][p.tipo] += 1
    return m

def mostrar_matriz_conteo(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                print('Para el tipo', i, 'y el pais', j, 'hay', m[i][j], 'peliculas')
    print()