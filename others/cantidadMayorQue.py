# Cantidad de numeros mayores que 3

secuencia = (1,2,3,4,100,25,23)
cantidad_may3 = 0

for num in secuencia:
    if num > 3:
        cantidad_may3 += 1

print('La cantidad de numeros mayor que 3 son:',cantidad_may3)