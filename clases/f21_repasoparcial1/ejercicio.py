import modulo

def main():
    
    trabajos = ''
    
    while True:
        print('')
        print('0.Salir')
        print('1.Cargar Pedidos')
        print('2.Mostrar datos de trabajos')
        print('3.Trabajo mayor cantidad de personal afectado')
        print('4.Buscar un trabajo por descripción o nombre')
        print('5.Mostrar la cantidad de trabajos por tipo')
        print('')
        
        op = input('Ingrese una opcion:')
        
        if op == '0':
            break
        
        if op == '1':    
            print('')
            print('1.Maual')
            print('2.Automatico')
            print('')
            
            modo = input('Ingrese el modo:')
            if modo == '1':
                trabajos = modulo.manual()
            if modo == '2':
                trabajos = modulo.automatico() 
        
        if op == '2':
            modulo.mostrar(trabajos)
        if op == '3':
            mayor = modulo.mayor_afectado(trabajos)
            print(mayor)
        if op == '4':
            descripcion = input('Ingresar el nombre o descripcion a buscar: ')
            respuesta = modulo.buscar(descripcion, trabajos)
            print(respuesta)
        if op == '5':
            tipos = 'interior', 'exterior', 'piletas', 'tapizados'
            respuesta = modulo.cantidad_por_tipo(trabajos)
            for i in range(len(respuesta)):
                print(tipos[i], respuesta[i])

if __name__ == '__main__':
    main()