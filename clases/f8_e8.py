import random

TAM = 45000

cant_multiplos_seis = 0
cant_multiplos_nueve = 0
cant_multiplos_ambos = 0
cant_menores_segundo = 0
mayor_multiplo_cuatro = 0
segundo_serie = 0

primer_multiplo_cuatro = True
sumar_menor_segundo = False

random.seed(95)
for i in range(TAM):
    num = random.randint(1,95000)
    if i == 0:
        primer_serie = num
    if i == 1:
        segundo_serie = num
    if i>1:
        if primer_serie<segundo_serie and not sumar_menor_segundo:
            cant_menores_segundo += 1
            sumar_menor_segundo = True
        elif num<segundo_serie:
            cant_menores_segundo += 1

    if num%6 == 0:
        cant_multiplos_seis += 1
    if num%9 == 0:
        cant_multiplos_nueve += 1
    if num%6 == 0 and num%9 == 0:
        cant_multiplos_ambos += 1
        
    if num%4 == 0:
        if primer_multiplo_cuatro:
            mayor_multiplo_cuatro = num
            primer_multiplo_cuatro = False
        elif num > mayor_multiplo_cuatro:
            mayor_multiplo_cuatro = num  

PORCENTAJE = cant_menores_segundo*100//TAM 

print("Cantidad de numeros que son menores al segundo leido de la secuencia:", cant_menores_segundo)
print("Cantidad de numeros multiplos de seis:", cant_multiplos_seis)
print("Cantidad de numeros multiplos de nueve:", cant_multiplos_nueve)
print("Cantidad de numeros multiplos de ambos:", cant_multiplos_ambos)
print("Mayor multiplo de cuatro:", mayor_multiplo_cuatro)
print("El porcentaje de numero menores al segundo de la secuencia:",PORCENTAJE)

        