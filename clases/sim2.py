import random

random.seed(20220512)

N = 25000

verificacion = 0

cant_mult3 = 0
cant_mult5 = 0
cant_no_mult5_mult3 = 0
cant_pares_mult11 = 0
acum_pares_mult11 = 0

es_el_primer = True
mayor = 0

for i in range(N):
    num = random.randint(1, 45000)
    verificacion += num

    if num%3 == 0:
        cant_mult3 += 1
    if num%5 == 0 and not num%3 == 0:
        cant_mult5 += 1
    if not num%3 == 0 and not num%5 == 0:
        cant_no_mult5_mult3 += 1

    digitos = str(num)
    primer_digito = digitos[0]
    if primer_digito == '1':
        if es_el_primer:
            mayor = num
            es_el_primer = False
        elif num > mayor:
            mayor = num

    if num%2 == 0 and num%11 == 0:
        cant_pares_mult11 += 1
        acum_pares_mult11 += num

promedio_pares_mult11 = acum_pares_mult11 // cant_pares_mult11
porcentaje_mult3 = cant_mult3*100 // N
porcentaje_mult5 = cant_mult5*100 // N
porcentaje_no_mult3_mult5 = cant_no_mult5_mult3*100 // N

print('Verificacion',verificacion)
print('La cantidad de numeros multiplos de 3 son:', cant_mult3)
print('La cantidad de numeros multiplos de 5 son:', cant_mult5)
print('La cantidad de numeros no multiplos de 3 ni 5 son:', cant_no_mult5_mult3)
print('El mayor de todos los numeros que comienzan con digito 1 es:', mayor)
print('El promedio de los numeros pares multiplos de 11 son:', promedio_pares_mult11)
print('El porcentaje de los multiplos de 3 es:',porcentaje_mult3)
print('El porcentaje de los multiplos de 5 es:',porcentaje_mult5)
print('El porcentaje de los no multiplos de 3 ni 5 es:',porcentaje_no_mult3_mult5)
