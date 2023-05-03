primer_lluvia = float(input('\nIngrese la cantidad de ml en el primer mes: '))
segunda_lluvia = float(input('Ingrese la cantidad de ml en el segundo mes: '))
tercer_lluvia = float(input('Ingrese la cantidad de ml en el tercer mes: '))
cant_may = 0

promedio = (primer_lluvia + segunda_lluvia + tercer_lluvia)/3

if primer_lluvia > promedio:
    cant_may += 1
if segunda_lluvia > promedio:
    cant_may += 1
if tercer_lluvia > promedio:
    cant_may += 1

if(primer_lluvia < segunda_lluvia and primer_lluvia < tercer_lluvia):
    men = 'primero'
    v_men = primer_lluvia
elif(segunda_lluvia < tercer_lluvia):
    men = 'segundo'
    v_men = segunda_lluvia
else:
    men = 'tercer'
    v_men = tercer_lluvia

print('\nEl promedio es: ', promedio)
print('Meses mayor que el promedio:', cant_may)
print('El que tuvo menos lluvia fue el',men,'mes')
if(v_men == 0):
    print('El',men,'mes no llovio')
print('\n')