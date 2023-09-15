
import random
import registro

def carga_automatica(vec, n):
    descripciones = 'descripcion1', 'descripcion2', 'descripcion3'
     
    for i in range(n):
        id = random.randint(1,n)
        descripcion = random.choice(descripciones)
        tipo = random.randint(0,19)
        importe = random.randint(1000,2000) 
        cant_personal = random.randint(1,10)
        vec.append(registro.Trabajo(id, descripcion, tipo, importe,cant_personal))
    
    
def ordenar_mayor_a_menor(vec):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].id < vec[j].id:
                vec[i],vec[j] = vec[j],vec[i]

def acumular_importes_mayor_3_personal(vec):
    acum = 0
    for trabajo in vec:
        if trabajo.cant_personal > 3:
            acum += trabajo.importe
    return acum

def mostrar_trabajos(vec):   
    importe_acumulado = acumular_importes_mayor_3_personal(vec)
    for trabajo in vec:
        if trabajo.cant_personal > 3:
            print(trabajo)
    print(' La suma de los importes acumulados: $' + str(importe_acumulado))    

def cant_trabajos(vec):
    vec_cont = 20 * [0]
    for i in range(len(vec)):
        vec_cont[vec[i].tipo] += 1
    return vec_cont

def mostrar_cont_trabajos(vec):
    for i in range(len(vec)):
        if vec[i] > 0:
            print('Para el tipo',i,'hubieron', vec[i],'trabajos')


def acumular_importes(vec):
    acum = 0
    for trabajo in vec:
        acum += trabajo.importe
    return acum
            
def prom_trabajos(vec):
    importe_total = acumular_importes(vec)
    cant_total = len(vec)
    if cant_total > 0:
        return importe_total / cant_total
    else:
        return 0
    
def mostrar_mayores_al_promedio(vec,promedio):
    for trabajo in vec:
        if trabajo.importe > promedio:
            print(trabajo)
    
def buscar(id,tipo,vec):
    for trabajo in vec:
        if trabajo.id == id and trabajo.tipo == tipo:
            return trabajo
    return 'Trabajo no encontrado! \n'

def principal():
    vec_trabajos = []
    cargados = False
    random.seed(1)

    while True:
        
        print('')
        print('1. Carga automatica de trabajos')
        print('2. Mostrar trabajos con mas de 3 personal y ordenado de mayor a menor')
        print('3. Cantidad de trabajos mayores a 0 por tipo')
        print('4. Trabajos cuyo importe sea mayor al promedio')
        print('5. Buscar trabajo por identificador y tipo')
        print('')
        
        op = input('Ingrese una opcion: ')
        
        if not cargados:
            if op == '1':
                n = int(input('Ingrese la cantidad de trabajos: '))
                carga_automatica(vec_trabajos,n)
                print('Trabajos cargados!') 
            else:
                print('Ingrese una opcion correcta! \n')
            cargados = True      
        else:
            if op == '2':
                ordenar_mayor_a_menor(vec_trabajos)
                mostrar_trabajos(vec_trabajos)
                
            elif op == '3':
                vec_cont_trabajos = cant_trabajos(vec_trabajos)
                mostrar_cont_trabajos(vec_cont_trabajos)
                
            elif op == '4':
                promedio = prom_trabajos(vec_trabajos)
                mostrar_mayores_al_promedio(vec_trabajos,promedio)
                
            elif op == '5':
                id = int(input('Ingrese la id a buscar:'))
                tipo = int(input('Ingrse el tipo a buscar:'))
                encontrado = buscar(id,tipo,vec_trabajos)  
                print(encontrado)              
                
            else:
                print('Ingrese una opcion correcta! \n')

if __name__ == "__main__":
    principal()