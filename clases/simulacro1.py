import random

random.seed(49)

N = 20000

cant_mult5= 0
cant_mult7= 0
cant_mult9= 0
cant_pares_menor_15k = 0

es_el_primero = True
mayor = 0


for i in range(N):
    num = random.randint(1,45000)
    
    if num%5 == 0:
        cant_mult5 += 1
    if num%7 == 0:
        cant_mult7 += 1
    if num%9 == 0:
        cant_mult9 += 1
    
    ult_digit = num%10
    if ult_digit >= 5 and ult_digit <= 8:
        if es_el_primero:
            mayor = num
            es_el_primero = False
        elif num > mayor:
            mayor = num
    
    if num%2 == 0 and num < 15000:
        cant_pares_menor_15k += 1        

PORCENTAJE = cant_pares_menor_15k*100 // N

print('La cantidad de numeros multiplos de 5 es:', cant_mult5)
print('La cantidad de numeros multiplos de 7 es:', cant_mult7)
print('La cantidad de numeros multiplos de 9 es:', cant_mult9)
print('El mayor de los numeros cuyo ultimo digito sea >= 5 y <= 8 es:',mayor)
print('La cantidad de numeros pares menores a 15000 son:',cant_pares_menor_15k)
print('El porcentaje de la cantidad de numeros pares menores a 15000 es de:', str(PORCENTAJE)+'%')