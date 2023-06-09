import random
pares_mult_seis = contador_mayor_primero = contador_segundo_millar = 0
random.seed(76)
for i in range(5000):
    num = random.randint(1, 65000)
    if num%2 == 0 and num%6 == 0:
        pares_mult_seis += 1
    if i == 0:
        primer_numero = num
    elif num > primer_numero:
        contador_mayor_primero += 1
    if 1000 < num < 2000:
        contador_segundo_millar += 1

porcentaje = contador_mayor_primero * 100 / 5000 

print('La cantidad de numeros pares y multiplos de seis:', pares_mult_seis)
print('La cantidad de numeros mayores que el primero de la sucesion:', contador_mayor_primero)
print('La cantidad de numeros entre el segundo millar:', contador_segundo_millar)
print('El porcentaje es:', porcentaje)
    
