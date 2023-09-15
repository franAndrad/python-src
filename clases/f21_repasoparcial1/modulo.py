import random

class Trabajo:

    def __init__(self, id, nombre, tipo, importe_cobro, personal_afectado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.importe_cobro = importe_cobro
        self.personal_afectado = personal_afectado
    def __str__(self):
        r = ''
        r += ' id: '+ self.id
        r += ' nombre: '+ self.nombre 
        r += ' tipo: '+ self.tipo 
        r += ' importe_cobro: '+ self.importe_cobro
        r += ' personal_afectado: '+ self.personal_afectado 
        return r

def validar_id():
    msj_error = 'Ingrese una id valida!'
    while True:
        id = input('Ingrese la id: ')
        if id.isnumeric():
            if int(id) > 0:
                return id
            else:
                print(msj_error)
        else:
            print(msj_error)
    
def manual():
    vector_trabajo = []
    
    n = int(input('Ingrese la cantidad de trabajos a cargar: '))
    for i in range(n):
        id = validar_id()
        nombre = input('Ingrese la nombre o descripción: ')
        tipo = input('Ingrese el tipo de trabajo (0:interior, 1:exterior, 2:piletas, 3:tapizados): ')
        importe_cobro = input('Ingrese el monto a cobrar: ')
        personal_afectado = input('Ingrese la cantidad de personal afectado: ')
        
        vector_trabajo.append(Trabajo(id, nombre, tipo, importe_cobro, personal_afectado))   
    return vector_trabajo

def automatico():
    vector_trabajo = []
    descripciones = 'casa', 'empresa', 'negocio'
    tipos = '0','1','2','3'
    importes = '100','200','300'
    afectados = '1','2','3','4','5'
    
    n = int(input('Ingrese la cantidad de trabajos a cargar: '))
    for i in range(n):
        id = str(random.random())
        nombre = random.choice(descripciones)
        tipo = random.choice(tipos)
        importe_cobro = random.choice(importes)
        personal_afectado = random.choice(afectados)
        
        vector_trabajo.append(Trabajo(id,nombre,tipo,importe_cobro,personal_afectado))
    return vector_trabajo

def mostrar(vec):
    # Ordenar
    for i in range(len(vec)-1):
        for j in range(i+1 , len(vec)):
            if int(vec[i].importe_cobro) <= int(vec[j].importe_cobro):
                vec[i], vec[j] = vec[j], vec[i]
    
    for obj in vec:
        print(obj)


def mayor_afectado(vec):
    for i in range(len(vec)):
        if i == 0:
            max = vec[i]
        elif int(vec[i].personal_afectado) > int(max.personal_afectado):
            max = vec[i]
    return max

def buscar(descripcion, vec):
    for obj in vec:
        if obj.nombre == descripcion:
            return obj
    return 'No se encontro un trabajo con esa descripcion!'

def cantidad_por_tipo(vec):
    vec_cantidad = 4 * [0]
    for obj in vec:
        vec_cantidad[int(obj.tipo)] += 1
    return vec_cantidad
    