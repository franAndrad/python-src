
# 0 - Acumular por fila  
# 1 - Acumular por columna 
# def mostrar_matriz_por_dato(matriz, dato):
#     """
#     Muestra la suma de cada fila o columna de una matriz.

#     Parametros:
#     matriz (list): Una lista de listas que representa la matriz.
#     dato (int): Indica si se debe mostrar por fila (0) o por columna (1).
    
#     Retorno:
#     None
#     """
    
#     if dato == 0:
#         acum = [0] * len(matriz)
#         for fila in range(len(matriz)):
#             for columna in range(len(matriz[0])):
#                 acum[fila] += matriz[fila][columna]
#             print('En la fila',fila,'hay', acum[fila] )
            
#     elif dato == 1:
#         acum = [0] * len(matriz[0])
#         for columna in range(len(matriz[0])):
#             for fila in range(len(matriz)):
#                 acum[columna] += matriz[fila][columna]
#             print('En la columna',columna,'hay', acum[columna] )

# def mostrar_cantidad_totalizada(matriz,a,b):
    
#     tipos = 'Motocicleta', 'Auto', 'Camion'
#     paises = 'Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay'
#     r = ''
#     for i in range(a):
#         ac = 0
#         for j in range(b):
#             if a == len(matriz):
#                 ac += matriz[i][j]
#             else:
#                 ac += matriz[j][i]
                
#         if a == len(matriz):
#             r += 'Para el pais de la cabina ' + paises[i] + ' hay un total de ' + str(ac) + ' vehiculos\n'
#         else:
#             r += 'Para el tipo de vehiculo ' + tipos[i] + ' hay un total de ' + str(ac) + ' vehiculos\n'
            
#     print(r)
    
def mostrar_cantidad_totalizada(matriz,a,b):
    tipos = 'Motocicleta', 'Auto', 'Camion'
    paises = 'Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay'
    r = ''
    
    ac = 0
    if a == len(matriz):
        for i in range(a):
            for j in range(b):
                ac += matriz[i][j]
            r += 'Para el pais de la cabina ' + paises[i] + ' hay un total de ' + str(ac) + ' vehiculos\n'
    else:
        for i in range(a):
            for j in range(b):
                ac += matriz[j][i]
            r += 'Para el tipo de vehiculo ' + tipos[i] + ' hay un total de ' + str(ac) + ' vehiculos\n'    
    
    print(r)

matriz = [0,1,2],[3,4,5]


pais = len(matriz)
tipo = len(matriz[0])

mostrar_cantidad_totalizada(matriz, pais, tipo)
mostrar_cantidad_totalizada(matriz, tipo, pais)


   