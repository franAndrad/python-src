import random 

random.seed(37)

N = 27000

cant_entre_men20k_men5k = 0
cant_entre_men5k_15k = 0
cant_mayor_15k_div9 = 0

cant_mayor_1k_term_4_6 = 0
acumulador_mayor_1k_term_4_6 = 0

mayor_impares_disntitos_1 = 0
primer_impar_disntito_1 = True

cant_div7 = 0

for i in range(N):
    num = random.randint(-20000, 30000)
    # num = int(input('a:'))
    
    # if num == 0:
    #     break
    # 1)
    if num >= -20000 and num < -5000:
        cant_entre_men20k_men5k += 1
    if num >= -5000 and num < 15000:
        cant_entre_men5k_15k += 1
    if num >= 15000 and num%9 == 0:
        cant_mayor_15k_div9 += 1
    
    # 2)
    if num >= 1000 and (num%10 == 4 or num%10 == 6):
        cant_mayor_1k_term_4_6 += 1
        acumulador_mayor_1k_term_4_6 += num

    # 3)
    if num > 0 and num%2 != 0 and num%10 != 1:
        if primer_impar_disntito_1:
            mayor_impares_disntitos_1 = num
            primer_impar_disntito_1 = False
        if not primer_impar_disntito_1 and num > mayor_impares_disntitos_1:
            mayor_impares_disntitos_1 = num
                            
    # 4)
    if num%7 == 0:
        cant_div7 += 1        

PORCENTAJE = cant_div7*100 // N

print('Los numeros mayor o iguales a -20k pero menores a -5k son:',cant_entre_men20k_men5k)
print('Los numeros mayor o iguales a -5k pero menores a 15k son:',cant_entre_men5k_15k)
print('Los numeros mayor o iguales a 15k pero divisibles por 9 son:',cant_mayor_15k_div9)
if cant_mayor_1k_term_4_6 != 0:     
    PROMEDIO = acumulador_mayor_1k_term_4_6 // cant_mayor_1k_term_4_6
    print('El promedio de los numeros mayor o igual a 1k y terminados en 4 o 6 son:', PROMEDIO)
else:
    print('No se ingreso ningun numero mayo que 1k y que termine en 4 o 6')
print('El mayor de los numeros positivos impares y con su ultimo digito distinto de 1 es:',mayor_impares_disntitos_1)
print('El porcentaje entero de los numeros divisibles por 7 es de:', str(PORCENTAJE) + '%')