import math
import os
from clase import *


def distancia(p, otro):
    return math.sqrt(pow(p.x - otro.x, 2) + pow(p.y - otro.y, 2))


def cargar_puntos(fd, vec):
    if not os.path.exists(fd):
        print('El docuemento', fd, 'no existe!')
        return
    m = open(fd, 'rt')
    for linea in m:
        linea = linea[:-1]
        coordenadas = linea.split(',')
        vec.append(Point(int(coordenadas[0]), int(coordenadas[1])))
    m.close()
    
    
def principal():
    vec_puntos = []
    cargar_puntos('puntos.csv', vec_puntos)
    dmax, dmin = 0 , distancia(vec_puntos[0], vec_puntos[1])
    
    for i in range(len(vec_puntos)-1):
        for j in range(i+1, len(vec_puntos)):
            d = distancia(vec_puntos[i], vec_puntos[j])
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d

            
    print('Distancia maxima:', int(dmax))
    print('Distancia minima:', int(dmin))
    
if __name__ == '__main__':
    principal()

