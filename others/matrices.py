def carga_matriz(matriz):
    for i in range(len(matriz)): # Obtenemos la cantidad de filas
        for j in range(len(matriz[0])): # Ponemos el 0 por que todas las filas tienen la misma cantidad de col
            matriz[i][j] = input('Ingrese la cantidad vendida de articulos para el vendedor ' + str(i) + ' y el articulo ' +str(j) + ': ')
    print('Fin de proceso de carga')


def mostrar_por_fila(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print('La cantidad vendida por el vendedor ' + str(i) + ' y articulo ' + str(j) + ': ' +matriz[i][j])

def mostrar_por_columnas(matriz):
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            print('La cantidad vendida por el vendedor ' + str(i) + ' y articulo ' + str(j) + ': ' +matriz[i][j])

def totalizar_cantidades(matriz):
    acum = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            acum += int(matriz[i][j])
    return acum

def totalizar_por_vendedor(matriz):
    vec_acum = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            vec_acum[i] += int(matriz[i][j])
    return vec_acum

def principal():
    cant_filas = int(input('Ingresa la cantidad de filas: '))
    cant_col = int(input('Ingresa la cantidad de columnas: '))

    # Creacion de la matriz
    mat = [[None]*cant_col for f in range(cant_filas)]

    # Carga de la matriz
    carga_matriz(mat)

    # Diferentes formas de visualizacion
    print('Mostrar por fila')
    mostrar_por_fila(mat)

    print('Mostrar por columna')
    mostrar_por_columnas(mat)
    
    # Totalizar cantidades de unidades vendidas
    cantidad = totalizar_cantidades(mat)

    # Totalizar cantidades por vendedor
    cant_por_vendedor = totalizar_por_vendedor(mat)
    print(cant_por_vendedor)

if __name__ == '__main__':
    principal()
