#--------------------------------------------
#Codigo para calcular el producto de numeros binarios con 3bits
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
    arrayBinSeparate.append(int(digit))
#print(arrayBinSeparate)

#Transformar el arrglo unidimesional en bidimensional
#-------------------------------------------------
arrayBinario = np.array(arrayBinSeparate)
tableBinario = arrayBinario.reshape((row,col))
#print(tableBinario)

#Mostrar en forma de tabla el numero binario
#------------------------------------------------
encabezados = ['b0','b1','b2']
tablaBin = PrettyTable()
tablaBin.field_names = encabezados  
for rowTable in tableBinario:
   tablaBin.add_row(rowTable)
#print(tabla)

#Interfaz grafica
#-----------------------------------------------------------
#
print('\nPrograma para calcular el producto de numeros binarios\n');
print(tablaBin)
print('\nLos datos a ingresar son b0,b2,b2')

bit1 = ''
bit2 = ''

while True:
    bit1 = input('Ingrese el primer bit: ')
    temp = False
    for i in encabezados:
        if bit1 == i:
            temp = True
    if(temp==True):
        break


while True:
    bit2 = input('Ingrese el segundo bit: ')
    temp = False
    for i in encabezados: 
        if bit2 == i:
            temp = True
    if(temp==True):
        break

print('\n')

#Encontrar posicion bit2
pos0 = encabezados.index(bit1)
pos1= encabezados.index(bit2)

#Producto entre b0 y b1
resProduct = np.zeros(row) #Se creo un arreglo de 8 variables que empiezen con 0
for i in range(row):
    resProduct[i] = tableBinario[i][pos0] * tableBinario[i][pos1] 

#Agregamos un encabezado
encabezados.append('b0*b1')

#----------------------------------------------------------------

#Agregamos la columa de solucion para Mostrar
resProductNp = np.array(resProduct)
solucion = np.insert(tableBinario,col, resProductNp, axis=1)

#Mostramos en otra tabla el resultado
tablaResult = PrettyTable()
tablaResult.field_names = encabezados
for rowTable in solucion:
    tablaResul.add_row(rowTable)
print(tablaResult) 
