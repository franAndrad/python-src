import random

VUELTAS = 10000
cant_positivos = 0
mayor = 0
primero = True

for i in range(VUELTAS):
    num = random.randint(-100000,100000)
    if primero or num > mayor:
        mayor = num
    primero = False
    if num > 0:
        cant_positivos += 1

porcentaje = round((cant_positivos/VUELTAS)*100,2)    
print('El mayor es: ',mayor)
print('El porcentaje de numero positivos son:' + str(porcentaje) + '%' )