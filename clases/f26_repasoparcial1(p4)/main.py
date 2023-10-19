from clase import *
from procesos import *

def menu():
    print('0. Salir   \n \
           1.   \n \
           2.   \n \
           3.   \n \
           4.   \n \
           5.   \n \
           6.   \n \
           7.   \n \
               ')
    return int(input('Ingrese una opcion: '))


def main():
    op = -1
    vec_p = []
    
    while op != 0:
        op = menu()
        
        if op == 1:
            n = validar_n('Ingrese la catidad de objetos a cargar: ')
            cargar_pelicula(n, vec_p)
        if op == 2:
            mostrar_peliculas(vec_p)
        if op == 3:
            titulo = input('Ingrese el titulo a buscar: ')
            indice = buscar_por_titulo(titulo, vec_p)
            if indice != -1:
                importe = float(input('Ingrese el importe a modificar: '))
                vec_p[indice].importe_invertido = importe
                print(vec_p[indice])
            else:
                print('No se encontro la pelicula')
        if op == 4:
            importe = float(input('Ingrese el importe a modificar: '))
            crear_binario('distintos10.dat', importe, vec_p)
            print('Se creo el archivo binario')
        if op == 5:
            mostrar_binario('distintos10.dat')
        if op == 6:
            id = int(input('Ingrese la id de la pelicula a buscar'))
            indice = buscar_por_id(id, vec_p)
            if indice != -1:
                print(vec_p[indice])
            else:
                print('No se encontro ninguna pelicula con el id:', id)
        if op == 7:
            m = crear_matriz_tipo_pais(vec_p)
            mostrar_matriz_conteo(m)

if __name__ == '__main__':
    main()