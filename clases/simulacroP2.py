def es_digito(caracter):
    return caracter in '0123456789'

def es_minuscula(caracter): 
    return  'a'<= caracter <= 'z'

def es_vocal(caracter):
    return caracter.lower() in 'aeiou'

def es_consonante(caracter):
        return caracter.lower() in 'bcdfghjklmnñpqrstvwxyz'


def test():

    documento = open("./simulacroP2.txt","rt")
    contenido  = documento.read()
    documento.close()
    
    # contenido = '1alfaxy 3adeef 123dasd a1d2 aba edesbdri.'

    # Punto 1
    es_primero = paso_minuscula = True
    es_digito_impar_primero = False
    cont_digito_impar_primero = 0

    # Punto 2
    es_primer_mayor = True
    paso_b = es_primero_vocal = False
    mayor = None
    cc = 0

    # Punto 3
    cvoc = ccons = total_cvoc_ccons = 0
    cont_mas_cons_que_voc = 0
    paso_am = False

    # Punto 4
    es_d = False
    cont_dx = 0
    cont_dc_ultima_voc = 0

    for car in contenido:
        if car == ' ' or car == '.':
            
            if es_digito_impar_primero and paso_minuscula:
                cont_digito_impar_primero += 1
                
            if es_primero_vocal and paso_b:
                if es_primer_mayor:
                    mayor = cc
                    es_primer_mayor = False
                elif cc > mayor:
                    mayor = cc

            if ccons > cvoc and not paso_am:
                cont_mas_cons_que_voc += 1
                total_cvoc_ccons += (ccons + cvoc)
            
            if cont_dx >= 2 and es_vocal(ultima):
                cont_dc_ultima_voc += 1
            
            es_digito_impar_primero = False
            paso_minuscula = True
            es_primero = True
            es_primero_vocal = False
            paso_b = False
            paso_am = False
            cc = 0
            
            cvoc = 0
            ccons = 0
            paso_am = False
            
            es_d = False
            cont_dx = 0
        else:
            
            cc += 1
            
            if es_primero and es_digito(car) and int(car)%2 != 0:
                es_digito_impar_primero = True
            if not es_primero and not es_minuscula(car):
                paso_minuscula = False
            
            if es_primero and es_vocal(car):
                es_primero_vocal = True
            if not es_primero and car == 'b':
                paso_b = True
                
            es_primero = False

            if es_vocal(car):
                cvoc += 1
            if es_consonante(car):
                ccons += 1
            if car == 'a' or car == 'm':
                paso_am = True
                
            if car == 'd' or car == 'D':
                es_d = True
            elif es_d and es_vocal(car):
                cont_dx += 1
            else:
                es_d = False
            
            ultima = car
                
    if cont_mas_cons_que_voc != 0:
        promedio = total_cvoc_ccons // cont_mas_cons_que_voc
    else:
        promedio = 0
        
    print(cont_digito_impar_primero)
    print(mayor)
    print(promedio)
    print(cont_dc_ultima_voc)

    print(total_cvoc_ccons)
    
if __name__ == '__main__':
    test()
