import random 

random.seed(20220512)

N = 25000

cant_mult3 = 0
cant_mult5 = 0
cant_mult_ni_5_3 = 0
cant_par_mult11 = 0
acum_pares_mult_11 = 0

es_el_primero = True
mayor = 0

for i in range(N):
    num = random.randint(1, 45000)
    
    if num%3 == 0:
        cant_mult3 += 1
    elif num%5 == 0:
        cant_mult5 += 1
    else:
        cant_mult_ni_5_3 += 1

    if (num == 1 or (10 <= num < 20) or (100 <= num < 200) or (1000 <= num < 2000) or (10000 <= num < 20000)):
        if es_el_primero:
            mayor = num
            es_el_primero = False
        elif num > mayor:
            mayor = num
    
    if num%2 == 0 and num%11 == 0:
        acum_pares_mult_11 += num
        cant_par_mult11 += 1
    
PROMEDIO = acum_pares_mult_11 // cant_par_mult11
PORCENTAJE_MULT3 = cant_mult3*100 // N        
PORCENTAJE_MULT5 = cant_mult5*100 // N        
PORCENTAJE_MULT_NI_5_3 = cant_mult_ni_5_3*100 // N        

print('La cantidad de mulitplos de 3 son:', cant_mult3, 'y su porcentaje es de:',str(PORCENTAJE_MULT3)+'%')
print('La cantidad de mulitplos de 5 son:', cant_mult5,
      'y su porcentaje es de:', str(PORCENTAJE_MULT5)+'%')
print('La cantidad que no son mulitplos de 3 ni de 5 son:',
      cant_mult_ni_5_3, 'y su porcentaje es de:', str(PORCENTAJE_MULT_NI_5_3)+'%')
print('El mayor de los numeros que comienzan con el digito 1 es:',mayor)
print('El promedio de los numeros pares y multiplos de 11 es de:',PROMEDIO)