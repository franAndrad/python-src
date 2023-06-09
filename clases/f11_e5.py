def es_letra(c):
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        return True
    else:
        return False

def principal():
    separador = (' ', '.')
    cl = cp = cp3 = cpts = cpdre = 0
    
    es_d = es_dr = es_dre = False
    cl_d  = 0
    
    palabra = input('Ingrese la palabra: ')
    
    ultima_palabra = ''
    
    for car in palabra:
        # termina la palabra    
        if car in separador:
            # verificamos que se haya una primer palabra
            if cl > 0:
                # palabra con 3 letras
                if cl == 3:
                    cp3 += 1
                # palabras 
                cp += 1
            
            # quedo guardada la ultima palabra aqui
            if ultima_palabra == 's':
               cpts += 1 
            
            if es_dre:
                cpdre += 1
                
            cl = 0
            
            es_d = False
            es_dr = False
            es_dre = False
                
        # esta en la palabra
        else:
            if es_letra(car):
                cl += 1
            
            # te guarda las palabras 
            ultima_palabra = car   
        
            # encontre expresion 'dre'
            if car == 'd':
                cl_d = cl
                es_d = True
            elif es_d and car == 'r' and cl == cl_d + 1 :                
                es_dr = True
            elif es_dr and car == 'e' and cl == cl_d + 2:    
                es_dre = True
                
    porcentaje = cp3*100 // cp        
    
    print(cp3)
    print(porcentaje,'%')
    print(cpts)
    print(cpdre)
    
principal()