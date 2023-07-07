def es_vocal(car):
    return car.lower() in 'aeiou'

def es_consonante(car):
    return car.lower() in 'bcdfghjklmnñpqrstvwxyz'

def test():
    contenido = 'Hace falta coraje para saltar de ese punto Siempre aparece una clave como ax13zy o 123tz o 2tepa5w Siempre pasa que es pesado o que es salado Otra rara ocasion para esos tarados.'
    
    # Variables para alternar
    cc = anterior = cont_alternar = cont_p_a = cp = 0
    primera_alternar = False
    
    for car in contenido:
        if car == ' ' or car == '.':
            
            cp += 1
            # Si la cantidad de variables alternadas es igual a la cantidad de caracteres y no hay un solo caracter
            if cont_alternar+1 == cc and cc != 1:
                cont_p_a += 1

            primera_alternar = False
            cc = cont_alternar = anterior = 0 
        
        else:
            cc += 1
            
            # Ignoramos la primera por que queda en anterior y car es la actual
            if primera_alternar:
                if es_vocal(car) and es_consonante(anterior):
                    cont_alternar += 1
                elif es_consonante(car) and es_vocal(anterior):
                    cont_alternar += 1
            
            anterior = car
            primera_alternar = True
            
    print(cont_p_a)
    
if __name__ == '__main__':
    test()


