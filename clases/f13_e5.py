
def es_num(car):
    return car in '0123456789'

def test():
    
    # Punto 1
    # contenido = 'Argentina ganó 2 mundiales en 1978 y en 1986 y un2o3 un2.'
    cd = 0
    p_dos_d = 0

    # Punto 2
    # contenido = 'Las laderas de las montañas están labradas.'
    es_primera = True
    es_l = False
    es_la = False
    p_com_la = 0
    
    #Punto 3
    promedio = 0
    cd_con_la = 0
    cl = 0

    # Punto 4
    contenido = 'Las lluvias se llevaron los llantos.'
    es_ll = False
    es_v = False
    p_com_ll_t_v = 0

    for car in contenido:
        if car == ' ' or car == '.':
      
            if cd >= 2:
                p_dos_d += 1
            
            if es_la:
                p_com_la += 1
                cd_con_la += cl

            if es_ll and es_v:
                p_com_ll_t_v += 1

            es_primera = True
            es_la = False
            es_ll = False
            es_l = False
            es_v = False
            cd = 0
            cl = 0

        else:

            if es_num(car):
                cd += 1
            
            print(cd)

            if es_primera and (car == 'l' or car == 'L'):
                es_l = True
                es_primera = False
            elif es_l and car == 'a':
                es_la = True
                es_l = False
            elif es_l and car == 'l':
                es_ll = True
                es_l = False

            if car == 'v':
                es_v = True

            cl += 1

    
    print('La cantidad de palabras con al menos dos digiros son: ', p_dos_d)
    print('La cantidad de palabras que comienzan con la son: ', p_com_la)
    if p_com_la != 0:
        print('El promedio de las letras de las palabras que cumplieron el comenzar con la: ',cd_con_la/p_com_la)
    print('La cantidad de palabras que comenzaron con ll:', p_com_ll_t_v) 

if __name__ == '__main__':
    test()


