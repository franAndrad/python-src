calificaciones = []

nota = int(input("Ingrese una nota: "))
while nota != 0:
    calificaciones.append(nota)
    nota = int(input("Ingrese una nota: "))

cont = 11 * [0]

for calificacion in calificaciones:
    cont[calificacion] += 1

for i in range(len(cont)):
    print(i,cont[i])

# print(calificaciones)
