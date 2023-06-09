qcompetidores = int(input("Ingrese la cantidad de competidores: "))
tiempo_record = float(input('Ingrese el tiempo record: '))
nombre_ganador = 0
tiempo_total = 0

# a) Determinar nombre del ganador de la carrera
for competidor in range(competidores):
    nombre = input('Ingrese el nombre: ')
    tiempo_carrera = float(input('Ingrese el tiempo: '))
    if(competidor == 0):
        tiempo_ganador = tiempo_carrera
    if(tiempo_carrera <= tiempo_ganador):
        tiempo_ganador = tiempo_carrera
        nombre_ganador = nombre
    tiempo_total += tiempo_carrera   
print('El ganador es: ', nombre_ganador)

# b) Tiempo record
if(tiempo_ganador < tiempo_record):
    print('El ganador con el tiempo',tiempo_ganador,'supero el tiempo record de',tiempo_record)

# c) Calcular el tiempo promedio
if competidores != 0:
    tiempo_promedio = tiempo_total / competidores
    print('El tiempo promedio es:',tiempo_promedio)
else:
    print('No se cargaron competidores')