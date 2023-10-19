import os
import pickle

def menu():
    print('1.')
    print('2.')
    print('3.')
    print('4.')
    print('5.')
    return int(input('Ingrese una opcion: '))


def mostrar_series(v):
    for serie in v:
        print(serie)


def cargar_registro(v, doc):
    if not os.path.exists(doc):
        print('El archivo', doc, 'no existe!')
        return

    fd = open(doc, 'rt')
    
    for linea in fd:
        linea = linea[:-1]
        campos = linea.split(",")
        
        print(campos[0], campos[1], campos[2], campos[3], campos[4])

    fd.close()


def test():

    vec_registro = []
    cargar_registro(vec_registro, 'series.csv')

    while True:
        op = menu()

        if op == 1:
            mostrar_series(vec_registro)
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass

if __name__ == '__main__':
    test()