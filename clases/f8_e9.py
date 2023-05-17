import random

N = 27000

cant_may_min_men_menoscincomil = 0
cant_may_menoscincomil_men_quincemil = 0
cant_may_quincemil_div_nueve = 0
cant_div_siete = 0
mayor = None
suma_may_mil_termin_cuatro_seis = 0
cant_may_mil_termin_cuatro_seis = 0


primer_mayor = True

random.seed(37)
for i in range(N):
    num = random.randint(-20000,30000)
    
    if num >= -20000 and num < -5000:
        cant_may_min_men_menoscincomil += 1
    if num >=- 5000 and num < 15000:
        cant_may_menoscincomil_men_quincemil += 1
    if num >= 15000 and num%9 == 0:
        cant_may_quincemil_div_nueve += 1
    
    if num >= 1000 and (num%10 == 4 or num%10 == 6):
        suma_may_mil_termin_cuatro_seis += num
        cant_may_mil_termin_cuatro_seis += 1
        
    if num > 0 and num%3 == 0 and num%10 != 1:
        if primer_mayor:
            mayor = num
            primer_mayor = False
        if num > mayor:
            mayor = num
    
    if num%7 == 0:
        cant_div_siete += 1
        
PROMEDIO = suma_may_mil_termin_cuatro_seis // cant_may_mil_termin_cuatro_seis
PORCENTAJE_SIETE = cant_div_siete*100 // N

print('1)\n a)Numeros mayor o igual -20000 y menores que -5000:',cant_may_min_men_menoscincomil)
print(' b)Numeros mayor o igual -5000 y menores que 15000:',cant_may_menoscincomil_men_quincemil)
print(' c)Numeros mayor o igual 15000 y divisibles por nueve:',cant_may_quincemil_div_nueve)
print('2)Promedio numeros mayor o igual 1000 con ultimo digito igual a 4 o 6:',PROMEDIO)
print('3)El mayor de los positivos impares con ultimo digito distinto de 1:',mayor)
print('4)El porcentaje de numeros divisibles por 7:',str(PORCENTAJE_SIETE)+'%')
        