import os
from clase import *


def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('Archivo inexistente!')
        return
    v = []
    m = open(nombre_archivo, 'rt')
    for linea in m:
        if linea[-1] == '\n':
            linea = linea[:-1]
        campos = linea.split(',')
        r = Reserva(
            campos[0], campos[1], int(campos[2]),
            int(campos[3]), int(campos[4]),
            float(campos[5])
        )
        v.append(r)
    m.close()
    return v


def mostrar_vector(v):
    for r in v:
        print(r)


def acumular_edad_tipo(v):
    mat = [[0] * 4 for i in range(14)]

    for i in range(len(v)):
        ind_fila = v[i].edad
        ind_col = v[i].tipo_servicio
        mat[ind_fila][ind_col] += v[i].monto

    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print('Para la edad:', f,
                  'y el tipo:', c,
                  'se facturó: $', mat[f][c])


def principal():
    v = leer_archivo('reservas.csv')
    mostrar_vector(v)
    acumular_edad_tipo(v)


if __name__ == '__main__':
    principal()
