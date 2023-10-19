from proceso import *


def menu():
    opciones = '0. Salir \n'\
               '1. \n'\
               '2. \n'\
               '3. \n'\
               '4. \n'\
               '5. \n'\
               '6. \n'\
               '7. \n' 
    print(opciones)
    return int(input('Ingrese la opcion: '))


def main():
    vec_profesionales = []
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            n = validar_n()
            cargar_profesionales(n, vec_profesionales)
        elif op == 2:
            mostrar_profesionales(vec_profesionales)
        elif op == 3:
            dni = int(input('Ingrese el dni a buscar: '))
            indice = buscar_dni(dni, vec_profesionales)
            if indice != -1:
                print(vec_profesionales[indice])
                imp = float(input('Ingrese el importe: '))
                if vec_profesionales[indice].importe < imp:
                    print('El importe esta desactualizado') 
            else:
                print('No existe ningun profesional con ese dni')
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        

if __name__ == '__main__':
    main()