def es_letra(car):
    if 'a' <= car <= 'z':
        return True
    elif 'A' <= car <= 'Z':
        return True
    else:
        return False

def es_vocal(car):
    if car in "aeiou":
        return True
    else:
        return False

def principal():
    cl = 0
    clp = 0
    cp = 0
    separador = (' ','.')

    primera = ''
    ultima = ''
    caracter_primero = True

    cont_palabra_c_consonante_t_vocal = 0

    es_l = False
    es_li = False
    cont_li = 0

    cont_lp4 = 0

    palabra = input('Ingrese una palabra: ')
    
    for car in palabra:
        cl += 1
        if car in separador:
            if cl > 0:
                cp += 1
            
            #Contar que la primera es consonante y la ultima vocal
            if not es_vocal(primera) and es_vocal(ultima):
                cont_palabra_c_consonante_t_vocal += 1
            
            caracter_primero = False
            
            #Contar las palabras con li
            if es_li:
                cont_li += 1
                es_l = False
                es_li = False
            
            #Contar palabras menores a 4 letras
            if clp < 4:
                cont_lp4 += 1
           
            clp = 0

        else:
            clp += 1     
            
            # Para el contador de li
            if car == 'l':
                es_l = True
            elif es_l and car == 'i':
                es_li = True 
            else:
                es_l = False

        # Encontrar la primera y la ultima
        if caracter_primero:
            primera = car
            caracter_primero = False
        else:
            ultima = car 
    
    print('pablabras que comienza con consonante y termina con vocal: ',cont_palabra_c_consonante_t_vocal) 
    print('palabras que tienen li:',cont_li)
    print('palabra con menos de 4 caracteres:', cont_lp4)

principal()
