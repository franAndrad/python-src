import random
random.seed(76)
cantidad_pares_multiplos_seis = cantidad_mayores_primero =  cantidad_segundo_millar = 0
for i in range(5000):
    num = random.randint(1,65000)
    if i == 0:
        primero = num
    if(num%2 == 0 and num%6 == 0):
        cantidad_pares_multiplos_seis += 1
    if(num > primero):
        cantidad_mayores_primero += 1
    if(num >= 2000 and num < 3000):
        cantidad_segundo_millar += 1

porcentaje = cantidad_mayores_primero * 100 // 5000

print('La cantidad de numeros pares multiplos de seis son:',cantidad_pares_multiplos_seis)
print('La cantidad de numeros mayores que el primer numero:',cantidad_mayores_primero)
print('La cantidad de numeros que pertenecesn al segundo millar son', cantidad_segundo_millar)
print('El porcentaje que representan los mayores que el primer numero es de:',str(porcentaje) + str('%'))
