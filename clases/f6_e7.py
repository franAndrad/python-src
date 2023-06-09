num = int(input('Ingrese un numero:'))
sum_cyc = 0
cant_pares = 0
cant_impares = 0
es_par = False
es_impar = False
paso_cero = False

while num>=0:
    if num >= 50 and num<=100:
        num_anterior = num
        num+= num_anterior
    if num%2 == 0:
        cant_pares += 1
        es_par = True
    else:
        cant_impares += 1
        es_impar = True
    if num == 0:
        paso_cero = True
    num = int(input('Ingrese un numero:'))

if paso_cero:
    mensaje_cero = 'Ingreso al menos un cero'
else:
    mensaje_cero = 'No ingreso ningun cero'
if es_par and es_impar:
    mensaje_paridad = 'Contiene numero pares e impares alternados'
else:
    mensaje_paridad = 'No tiene numeros pares e impares alternados'

print('\nLa sumatoria de los numeros comprendidos entre 50 y 100 es:', sum_cyc)
print('Cantidad de valores pares: ',cant_pares)
print('Cantidad de valores impares: ',cant_impares)
print(mensaje_cero)
print(mensaje_paridad)