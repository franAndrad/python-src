# Cantidad de numeros multiplos de 3

secuencia = (1,2,3,4,100,25,23)
cantidad_mult3 = 0

for num in secuencia:
    if num%3 == 0:
        cantidad_mult3 += 1

print('La cantidad de numeros multiplos de 3 son:',cantidad_mult3)