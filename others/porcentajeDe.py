# Porcentaje de numeros mayores que 3 de una secuencia
secuencia = (1, 2, 3, 4, 5)

cant_mayor3 = 0

for num in secuencia:
    if num > 3:
        cant_mayor3 += 1       

PORCENTAJE = cant_mayor3*100 // len(secuencia)

print('El porcentaje entero de los numeros mayor que 3 es de:', str(PORCENTAJE) + '%')