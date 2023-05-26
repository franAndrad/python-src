import random

N = 20000

random.seed(49)

cant_mult5 = 0
cant_mult7 = 0
cant_mult9 = 0

es_el_primer = True
mayor = 0

cant_par_men15k = 0

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
        if es_el_primer:
            mayor = num
            es_el_primer = False
        elif num > mayor:
            mayor = num

    if num%2 == 0 and num < 15000:
        cant_par_men15k += 1

porcentaje = cant_par_men15k*100 // N

print('La cantidad de num multiplos de 5 son:', cant_mult5)
print('La cantidad de num multiplos de 7 son:', cant_mult7)
print('La cantidad de num multiplos de 9 son:', cant_mult9)
print('El mayor de los numero cuyo ultimo digito es >= 5 y <= 8 es:',mayor)
print('La cantidad de numeros pares menores a 15K:', cant_par_men15k)
print('El porcentaje truncado de pares menores a 15K es:',str(porcentaje) + '%')
