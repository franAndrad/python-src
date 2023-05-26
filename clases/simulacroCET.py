# En este simulacro de parcial, deberan resolver el siguiente problema en Python y luego informar los resultados
# del mismo en los puntos consiguientes. Luego deberan de responder algunas preguntas sobre el desarrollo del programa.
# Se pide desarrollar un programa completo en Python que permita generar una sucesión de 35000 números usando una
# semilla con el valor generador 19 (random.seed(19)). Los valores de esos 35000 números deben de estar comprendidos entre -15000 y 45000 (ambos números incluidos), para ello debe utilizar random.randint(-15000, 45000).

# En base a esta sucesión, el programa debe:
# 1)
#   a) Determinar cuántos de esos números son mayores o iguales que 0 (cero) pero menores o iguales que 40000;
#   b) también determine la cantidad de números que pertenezcan al intervalo (-10000, 2500] y
#   c) cuántos números son mayores que 0 (cero) y además sean divisibles por 7.
# 2) Determinar el mayor de los números pares en el rango [10000, 45000], y que además su tercer dígito sea 4 o 9.
# 3) Determinar el promedio entero de los números mayores que -5000 pero menores o iguales que 25000, pero que además su último dígito sea igual a 7. (No debe redondear el promedio, sino que debe truncar el mismo)
# 4) Determinar el porcentaje entero que la cantidad de los números comprendidos entre 1000 y 10000 (ambos incluidos) representan sobre la cantidad de números positivos. Aclaración: Debe de realizar primero la multiplicación correspondiente, y luego la división.
# 5) Determinar el menor de todos los números negativos.

import random

random.seed(19)

N = 35000

cant_0_40k = 0
cant_men10k_2k5 = 0
cant_0_div7 = 0
cant_men5k_25k_term7 = 0
acum_men5k_25k_term7 = 0
cant_1k_10k = 0
cant_positivos = 0

es_el_primer_mayor= True
mayor = 0
es_el_primer_menor= True
menor = 0

for i in range(N):
    num = random.randint(-15000, 45000)

    if num >= 0 and num <= 40000:
        cant_0_40k += 1
    if num > -10000 and num <= 2500:
        cant_men10k_2k5 += 1
    if num > 0 and num%7 == 0:
        cant_0_div7 += 1



    if num%2 == 0 and (10000 <= num <= 45000):
        digito = str(num)
        tercer_digito = digito[2]
        if (tercer_digito == '4' or tercer_digito == '9'):
            if es_el_primer_mayor:
                mayor = num
                es_el_primer_mayor = False
            elif num > mayor:
                mayor = num

    if num > -5000 and num <= 25000 and abs(num)%10 == 7:
        cant_men5k_25k_term7 += 1
        acum_men5k_25k_term7 += num

    if (1000 <= num <= 10000):
        cant_1k_10k += 1

    if num>0:
        cant_positivos += 1

    if num<0:
        if es_el_primer_menor:
            menor = num
            es_el_primer_menor = False
        elif num < menor:
            menor = num

prom_men5k_25k_term7 = acum_men5k_25k_term7 // cant_men5k_25k_term7
porc_1k_10k = cant_1k_10k*100 // cant_positivos

print('La cantidad de numeros entre [0,40k] son:', cant_0_40k)
print('La cantidad de numeros entre (-10k,2k5] son:', cant_men10k_2k5)
print('La cantidad de numeros entre mayore que 0 y divisibles por 7 son:', cant_0_div7)
print('El mayor del rango [10k,45k] y su tercer digito es 4 o 9 es:',mayor)
print('El promedio de los numeros (-5k,25k] y que terminan en 7 es de:', prom_men5k_25k_term7)
print('El porcentaje de los numeros comprendidos entre [1k,10k] sobre los positivos es de:',str(porc_1k_10k)+'%')
print('El menor de los numeros negativos es:',menor)
