#--------------------------------------------
#Codigo para generar una matriz binaria
#--------------------------------------------

import numpy as np
from prettytable import PrettyTable

row = 8
col = 3

#Generar un binario en un arreglo unidimension donde en cada posicion hay un binario de 3digitos
#---------------------------------------------------------------------
binary= np.array([np.binary_repr(i,width=col) for i in range (row)])
#print(binary)

#Unir todo el arreglo en una cadena de caracteres
#---------------------------------------------------------------
stringBinarios =''.join(binary)
#pirint(stringBinarios)

#Separar cada uno de los caracteresen un nuevo arrego unidimensional
#---------------------------------------------------------------------
arrayBinSeparate = []
for digit in stringBinarios:
    arrayBinSeparate.append(digit)
#print(arrayBinSeparate)

#Transformar el arrglo unidimesional en bidimensional
#-------------------------------------------------
arrayBinario = np.array(arrayBinSeparate)
tableBinario = arrayBinario.reshape((row,col))
#print(tableBinario)

#Mostrar en forma de tabla el numero binario
#------------------------------------------------
encabezados = ['b0','b1','b2']
tabla = PrettyTable()
tabla.field_names = encabezados  
for rowTable in tableBinario:
    tabla.add_row(rowTable)
print(tabla)
