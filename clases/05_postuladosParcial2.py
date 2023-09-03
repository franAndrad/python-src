# Consignas
# 9 - Determinar la cantidad de palabras que tuvieron más de 3 caracteres.
# 3 - Determinar la cantidad de palabras que terminan con la primera letra de todo el texto.
# 8 - Determinar la cantidad de palabras que contienen 'h' pero dentro de la palabra es decir no puede ser ni la primera ni la última letra de la palabra.
# 10- Determinar la cantidad de palabras que contienen 'de' en la primera mitad de la palabra.

def es_caracter(car):
    return  'a' <= car.lower() <= 'z'

def test():
    
    # documento = open("doc.txt","rd")
    # contenido = documento.read()
    # documento.close()
    
    contenido = 'asda asdadad asd fhs hth ardefs defhn d1e ldeuhj deg dea.'
    # contenido = 'pepito roba bancop hohla hohlh ohl def fdsfde sdsdedasddsas.'
    cc = 0
    
    # Punto 1
    cl = cp3 = 0
    
    # Punto 2
    es_primera_texto = True
    primera_texto = cont_palabra_ultima_primera_del_texto = 0
    
    # Punto 3
    h_paso_primero = tiene_h = False
    cp_h = 0
    
    # Punto 3
    tiene_d = tiene_de = False
    cde = cde_primera_mitad = 0
    
    for car in contenido:
        if car == ' ' or car == '.':
            if cc > 3:
                cp3 += 1
        
            if primera_texto == ultima:
                cont_palabra_ultima_primera_del_texto += 1
                
            if not h_paso_primero and ultima != 'h' and tiene_h:
                cp_h += 1
        
            if tiene_de and 1 <= cde <= (cc//2):
                 cde_primera_mitad += 1
        
            # Reseteo
            cl = cc = 0
            
            h_paso_primero = tiene_h = False
            
            tiene_d = tiene_de = False
            
        else:
            
            cc += 1
            
            if es_caracter(car):
                if es_primera_texto:
                    primera_texto = car
                    es_primera_texto = False
                cl += 1
            
                if cc == 1 and car == 'h':
                    h_paso_primero = True
                if car == 'h':
                    tiene_h = True
                    
                if car == 'd':
                    tiene_d = True
                elif tiene_d and car == 'e':
                    tiene_de = True
                    cde = cc
                else:
                    tiene_d = False
                
                ultima = car

    print(cp3)
    print(cont_palabra_ultima_primera_del_texto)
    print(cp_h)
    print(cde_primera_mitad)
    
if __name__ == '__main__':
    test()