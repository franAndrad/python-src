import numpy as np
from prettytable import PrettyTable
#exp = input('Ingrese la expresion: ')
proposition = ['p','q','r']
operators = ['^','v','w','>']
cantPropositions = 0
cantOperators = 0
encabezados = []
operations = []
resOperation = []

print('\nPrograma para calcular un operacion logica de dos proposiciones\n')
print('- operaciones:\n  tor"v"\n  and"^"\n  xor"w""\n  si">"\n')
print('- proposiciones:\n  p\n  q\n  ')
exp = input('Ingrese la operacion logica: ')
print('\n')
#Verificamos la cantidad de elementos
#for i in range(len(exp))

for i in exp:
    for j in proposition:
        if i == j:
            cantPropositions += 1
            encabezados.append(i)

#Verificamos la cantidad de operadores y guardamos las operaciones
for i in exp:
    for j in operators:
        if i == j:
            cantOperators += 1
            operations.append(i)


#Cantidad de filas y columans a procesar
cantRow = 2 ** cantPropositions
cantCol = cantPropositions

#Generar un binario en un arreglo unidimension donde en cada posicion hay un binario de 3digitos
#---------------------------------------------------------------------
binary= np.array([np.binary_repr(i,width=cantCol) for i in range (cantRow)])
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
tableBinario = arrayBinario.reshape((cantRow,cantCol))
#Intercambiar 1 por 0 y 0 por 1
tableOpuesta = np.array(tableBinario)
tableOpuesta = np.where(tableOpuesta == 1, 0, np.where(tableOpuesta == 0, 1, tableOpuesta))
tableTrue = tableOpuesta

#Intercabiar columnas (inverso)
#tableTrue = tableOpuesta[:,::-1]
#print(tableBinario)


#Mostrar en forma de tabla de verdad
#-----------------------------------------------

#transforma los 1 en V y los falsos en F
tablePrepare = np.where(tableTrue == 1, 'V',np.where(tableTrue == 0, 'F',tableTrue))
tableImprimir = PrettyTable()
tableImprimir.field_names = encabezados  
for rowTable in tablePrepare:
   tableImprimir.add_row(rowTable)
#print(tableImprimir)


#Continuar con tableTrue que es la que tien valore binarios
for op in operations:   

    if cantPropositions == 2:
        #Si tiene ^  and
        if op == operators[0]: 
            for i in range(cantRow):
                resOperation.append(tableTrue[i][encabezados.index('p')] and tableTrue[i][encabezados.index('q')])

        #Si tiene v or inclusiva
        if op == operators[1]: 
            for i in range(cantRow):
                resOperation.append(tableTrue[i][encabezados.index('p')] or tableTrue[i][encabezados.index('q')])

        #Si tiene w or explusiva
        if op == operators[2]: 
            for i in range(cantRow):
                resOperation.append(tableTrue[i][encabezados.index('p')]^tableTrue[i][encabezados.index('q')])
        
        #Si tiene > si entonces
                resOperation.append(not(tableTrue[i][encabezados.index('p')]) or tableTrue[i][encabezados.index('q')])
        if op == operators[3]: 
            for i in range(cantRow):
                resOperation.append(not(tableTrue[i][encabezados.index('p')]) or tableTrue[i][encabezados.index('q')])


encabezados.append(exp)
#Mostramos el resultado
resProductNp = np.array(resOperation)
solution = np.insert(tableTrue,cantCol,resOperation,axis=1)
tablePrepare = np.where(solution == 1, 'V',np.where(solution == 0, 'F',solution))
tableResult = PrettyTable()
tableResult.field_names = encabezados

for rowTable in tablePrepare:
    tableResult.add_row(rowTable)
print(tableResult,'\n')
