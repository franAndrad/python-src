def es_vocal(car):
    return car.lower() in 'aeiou'

def test():
    #contenido = 'aseadon asdon asdasd fsdfsgsfsdf10sdfson 10saadaon asd10asd asd10as as10ad10on.'
    contenido = 'aei lalelon ajjajjjjjjjjajajaj asd10asd.'
    
    cc = 0
    # Punto 1
    cant_palabras_3_vocales = cv = 0
    
    # Punto 2
    posicion_o = ultimo = cont_ultimo_on = 0 
    
    # Punto 3
    posicion_palabra_mas_larga = palabra_mas_larga = cp = 0
    
    # Punto 3
    tiene_1 = False
    posicion_10 = cont_10_despues_mitad = 0
    
    for car in contenido:
        if car == ' ' or car == '.':
            
            cp += 1
            
            if cv == 3:
                cant_palabras_3_vocales += 1
            
            if posicion_o == cc-1 and ultimo == 'n':
                cont_ultimo_on += 1
            
            if cp == 1:
                posicion_palabra_mas_larga = cp
                palabra_mas_larga = cc 
            elif cc > palabra_mas_larga: 
                palabra_mas_larga = cc
                posicion_palabra_mas_larga = cp  
            
            if posicion_10 > (cc//2)+1:
                cont_10_despues_mitad += 1
            
            cv = cc = posicion_o = 0
            
            tiene_1 = False
            posicion_10 = 0
                        
        else:
            
            cc += 1
            
            if es_vocal(car):
                cv += 1

            if car == 'o':
                posicion_o = cc

            if car == '1':
                tiene_1 = True
            elif tiene_1 and car == '0':
                posicion_10 = cc
            else:
                tiene_1 = False
                
            ultimo = car
    
    porcentaje = cont_ultimo_on * 100 // cp
    
    print(cant_palabras_3_vocales)
    print(porcentaje)
    print(posicion_palabra_mas_larga)
    print(cont_10_despues_mitad)

if __name__ == '__main__':
    test()