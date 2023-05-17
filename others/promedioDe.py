# Promedio de una secuencia
secuencia = (1,2,3,4,5)

contador = 0
acumulador = 0

for num in secuencia:
    contador += 1
    acumulador += num

PROMEDIO_ENTERO = acumulador // contador
PROMEDIO_REDONDEADO = round(acumulador/contador,2)

print('El promedio entero de la secuencia es:', PROMEDIO_ENTERO)
print('El promedio redondeado de la secuencia es:', PROMEDIO_REDONDEADO)
