def es_consonante(car):
    return car.lower() in 'bcdfghjklmnñpqrstvwxyz'

def es_vocal(car):
    return car.lower() in 'aeiou'
    
def test():
    # contenido = "algjdkf sk4sk asdkjst sadjst dfjskst ajajma jaaaaa ajska4 asjdfktdkfjs askjtfs."
    documento = open("f14_enunciadotipoparcial2_texto.txt", "rt")
    contenido = documento.read()
    documento.close()
    
    
    cl = 0
    # Punto 1
    tiene_consonante_3_o_5 = False
    cp_tienen_consonante_3_o_5_terminan_vocal = 0
    
    # Punto 2
    cp_tiene_digitos_es_impar = 0
    tiene_digito = False
    
    # Punto 3
    tiene_t = tiene_s_despues_de_t = False
    posicion_t = cp_tiene_t_despues_s = acum_cc_tiene_t_despues_s = 0
    
    # Punto 4
    tiene_m = tiene_primera_letra_texto = False
    primer_letra_texto = posicion_ma = cp_tiene_ma_primer_letra_texto =  0
    es_primera_texto = True
    
    for car in contenido:
        if car == ' ' or car == '.':
            
            if tiene_consonante_3_o_5 and es_vocal(ultima):
                cp_tienen_consonante_3_o_5_terminan_vocal += 1
                
            if tiene_digito and cl%2 == 1:
                cp_tiene_digitos_es_impar += 1
            
            
            if tiene_t and tiene_s_despues_de_t:
                cp_tiene_t_despues_s += 1
                acum_cc_tiene_t_despues_s += cl
            
            if posicion_ma > 4 and tiene_primera_letra_texto:
                cp_tiene_ma_primer_letra_texto += 1
            
            cl = 0
            tiene_consonante_3_o_5 = False
            
            tiene_digito = False
            
            tiene_t = tiene_s_despues_de_t = False
            
            tiene_m = tiene_primera_letra_texto = False
            posicion_ma = 0 
            
        else:
            cl += 1
            
            if (cl == 3 or cl == 5) and es_consonante(car):
                tiene_consonante_3_o_5 = True
            
            if car.isdigit():
                tiene_digito = True
            
            if car == 't':
                tiene_t = True
                posicion_t = cl
            
            if tiene_t and car == 's' and cl > posicion_t:
                tiene_s_despues_de_t = True
            
            
            
            if es_primera_texto:
                primer_letra_texto = car
                es_primera_texto = False
            
            if car == primer_letra_texto:   
                tiene_primera_letra_texto = True
                
            if car == 'm':
                tiene_m = True
            elif tiene_m and car == 'a':
                posicion_ma = cl
            else:
                tiene_m = False
            
            ultima = car    
    
    promedio = acum_cc_tiene_t_despues_s // cp_tiene_t_despues_s
    
    print(cp_tienen_consonante_3_o_5_terminan_vocal)
    print(cp_tiene_digitos_es_impar)
    print(promedio)
    print(cp_tiene_ma_primer_letra_texto)
        
if __name__ == '__main__':
    test()