# Generar 534 numeros que esten entre - 1532156111 y 2131516132 incluidos utilizando una semilla de 1 para el cual encontrar:

# Tener en cuenta que para encontrar los numeros que terminen en algun valor primero debemos convertir todos en positivos para poder usar el ('num%10 == 5'), siendo num el numero del que queremos encontrar el ultimo digito 5. Para convertir a positivos usamos el 'abs(num)' que nos devuelve el valor absoluto del numero

    # a) El mayor de todos los numeros que empiezen con 5 y sean pares
    # b) El menor de todos los numeros que terminen con 7
    # c) La cantidad de numeros menores que el segundo numero de la serie
    # d) La cantidad de numeros mayores que el tercer numero de la serie
    # e) La cantidad de numeros impares y que sean multiplos de 4 o 6
    # f) El porcentaje de el punto 'e'
    # g) El promedio redondeado a 2 decimales de el punto 'd'
    # h) El promedio truncado decimales de el punto 'd'
    # i) La cantidad de numeros multiplos de 3 que terminen en 6
    # j) Determinar si se genero el numero - 500000 en la serie

            
import random

random.seed(1)

N = 534

# mayor
es_el_primer_mayor = True
mayor = 0
# menor
es_el_primer_menor = True
menor = 0

cant_n_menores_segundo = 0
cant_n_mayores_tercer = 0
acum_n_mayores_tercer = 0
cant_n_impares_mult4o6 = 0
cant_n_mult3_term6 = 0

encontro_menos500k = False

for i in range(N):
    num = random.randint(-1532156111,2131516132)
    
    # convertimos los negativos en positivos para resolver para econtrar ultimo digito
    positivo = abs(num)
  
    # a)
    digit = str(num)
    primer_digit = digit[0]
    if primer_digit == '5' and num%2 == 0:
        if es_el_primer_mayor:
            mayor = num
            es_el_primer_mayor = False
        elif num > mayor:
            mayor = num
    # b)
    
    if positivo%10 == 7:
        if es_el_primer_menor:
            menor = num
            es_el_primer_menor = False
        elif num < menor:
            menor = num
    # c) d)
    if i == 0:
        primer_numero = num
    elif i == 1:
        segundo_numero = num
        if primer_numero < segundo_numero:
            cant_n_menores_segundo += 1      
    elif i == 2:
        tercer_numero = num
        if primer_numero > tercer_numero:
            cant_n_mayores_tercer += 1
            acum_n_mayores_tercer += num
        if segundo_numero > tercer_numero:
            cant_n_mayores_tercer += 1
            acum_n_mayores_tercer += num
    
    if i>1 and num < segundo_numero:
        cant_n_menores_segundo += 1
    
    if i>2 and num > tercer_numero:
        cant_n_mayores_tercer += 1
        acum_n_mayores_tercer += num
    
    # e)
    if positivo%2 == 1 and (num%4 == 0 or num%6 == 0):
        cant_n_impares_mult4o6 += 1
    
    # i)
    if num%3 == 0 and positivo%10 == 6:
        cant_n_mult3_term6 += 1
    
    # j)
    if num == -500000:
        encontro_menos500k = True
    
    
# f)
PORCENTAJE = cant_n_impares_mult4o6*100 // N 

# g)
PROMEDIO_R = round(acum_n_mayores_tercer / cant_n_mayores_tercer , 2)
    
# h)
PROMEDIO_T = acum_n_mayores_tercer // cant_n_mayores_tercer 

print('El mayor de los numeros que empiezan con 5 y es par es:', mayor)
print('El menor de los numeros que terminan con 7:', menor)
print('La cantidad de numeros menores que el segundo de la secuencia:',cant_n_menores_segundo)
print('La cantidad de numeros mayores que el tercer de la secuencia:',cant_n_mayores_tercer)
print('La cantidad de numeros impares multiplos de 4 o 6 son:', cant_n_impares_mult4o6)
print('El porcentaje de la cantidad de numeros impares multiplos de 4 o 6 son:', str(PORCENTAJE)+'%')
print('El promedio redondeado a dos decimales de la cantidad de numeros menores que el tercero de la secuencia:', PROMEDIO_R)
print('El promedio truncado de la cantidad de numeros menores que el tercero de la secuencia:', PROMEDIO_T)
print('La cantidad de multiplos de 3 que terminan en 6 son:', cant_n_mult3_term6)
if encontro_menos500k:
    print('Si se genero el numero -500000 en la serie')
else:
    print('No se genero el numero -500000 en la serie')