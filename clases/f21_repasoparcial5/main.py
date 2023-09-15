import modulo
import random

def menu():
    print('')
    print('1. Carga automatica de alumnos')
    print('2. Mostrar alumnos ordenados por apellido de menor a mayor')
    print('3. Cantidad de alumnos por nivel')
    print('4. Monto total a abonar a un tutor mediante dni')
    print('5. Descuento a alumno de 10% mediante apellido')
    print('')
    return input('Ingrese una opcion: ')

def cargar_n():
    while True:
        n = int(input('Ingrese la cantidad de alumnos a cargar: '))
        if n > 0:
            return n
        else:
            print('Ingrese un valor positivo')


def cargar_registro_alumnos(n,vec):
    nombres =  'Francisco', 'Martina', 'Ariana'
    apellidos = 'Andrade', 'Espinoza', 'Villalba'
     
    for i in range(n):
        dni = random.randint(10000000, 60000000)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        dni_tutor = random.randint(10000000, 60000000)
        importe = round(random.uniform(1000, 8000),2)
        nivel_cursado = random.randint(0, 12)
        vec.append(modulo.Alumno(dni, nombre, apellido, dni_tutor, importe, nivel_cursado))

def ordenar_vector(vec):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].apellido > vec[j].apellido:
                vec[i],vec[j] = vec[j], vec[i]

def mostrar_vector(vec):
    for alumno in vec:
        print(alumno)

def contar_alumnos_por_nivel(vec):
    vec_cont = 13 * [0]
    for alumno in vec:
        vec_cont[alumno.nivel_cursado] += 1
    return vec_cont

def mostrar_contador(vec_cont):
    for i in range(len(vec_cont)):
        if vec_cont[i] > 0:
            print('La cantidad de alumnos del nivel', i, 'es', vec_cont[i])

def importe_acumulado_tutor(dni_tutor, vec):
    importe = 0
    for alumno in vec:
        if alumno.dni_tutor == dni_tutor:
            importe += alumno.importe
    return importe

def buscar(apellido,vec):
    for alumno in vec:
        if alumno.apellido == apellido:
            alumno.importe = (alumno.importe*10) / 100
            return alumno
    return 'No existe un alumno con ese apellido!'

def principal():
    
    vec_alumnos = []

    while True:
        op = menu()

        if op == '0':
            break
        elif op == '1':
            n = cargar_n()
            print(n)
            cargar_registro_alumnos(n,vec_alumnos)
            print('Alumnos cargados!')
        elif op == '2':
            ordenar_vector(vec_alumnos)
            mostrar_vector(vec_alumnos)
        elif op == '3':
            vec_cont = contar_alumnos_por_nivel(vec_alumnos)
            mostrar_contador(vec_cont)
        elif op == '4':
            dni_tutor = int(input('Ingrese el dni del tutor: '))
            total = importe_acumulado_tutor(dni_tutor,vec_alumnos)
            print('El importe acumulado para el tutor con dni', dni_tutor, 'es', total)
        elif op == '5':
            apellido = input('Ingrese el apellido del alumno: ')
            encontrado = buscar(apellido,vec_alumnos)
            print(encontrado)
        else:
            print('Ingrese una opcion valida')
    

if __name__ == '__main__':
    principal()
