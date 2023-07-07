def es_vocal(car):
    return car.lower() in 'aeiou'

def es_consonante(car):
    return car.lower() in 'bcdfghjklmnñpqrstvwxyz'
    
def test():
    # contenido = 'Hace falta coraje para saltar de ese punto.'
    # contenido = 'Siempre aparece una clave como ax13zy o 123tz o 2tepa5w.'
    # contenido = 'Siempre pasa que es pesado o que es salado.'
    # contenido = 'Otra rara ocasion para esos tarados.'
    
    documento = open('./02_simulacroP2.txt', 'rt')
    contenido = documento.read()
    documento.close()
    
    # Punto 1
    cvocal = ccons = cont_igual_voc_cons_par = 0
   
    # Punto 2
    tiene_p = tiene_digito = False
    primer_no_p_digito = True 
    mayor = cc = 0
    
    # Punto 3
    tiene_s = False
    cont_dos_digitos_si_s = sum_carac_dos_digitos_si_s = 0
     
    # Punto 4
    tiene_r = tiene_ra = tiene_vocal_dos_primeras = False
    cont_dos_primera_vocal_si_ra = 0
    
    for car in contenido:
        if car == ' ' or car == '.':
            if ccons == cvocal and (ccons+cvocal)%2 == 0:
                cont_igual_voc_cons_par += 1
                
            if not tiene_p and tiene_digito:
                if primer_no_p_digito:
                    mayor = cc
                    primer_no_p_digito = False
                elif cc > mayor:
                    mayor = cc
                    
            if tiene_s and cc > 2:
                cont_dos_digitos_si_s += 1
                sum_carac_dos_digitos_si_s += cc
                
            if tiene_ra and tiene_vocal_dos_primeras:
                cont_dos_primera_vocal_si_ra += 1
                
            cvocal = ccons = 0
            
            tiene_p = tiene_digito = False
            cc = 0
            
            tiene_s = False
            
            tiene_r = tiene_ra = tiene_vocal_dos_primeras = False
        else:
            if es_vocal(car):
                cvocal += 1
            if es_consonante(car):
                ccons += 1
            
            if car.lower() == 'p':
                tiene_p = True
            if car.isdigit():
                tiene_digito = True
            
            if car.lower() == 's':
                tiene_s = True
    
            if car.lower() == 'r':
                tiene_r = True
            elif tiene_r and car.lower() == 'a':
                tiene_ra = True
            
            if 0 <= cc <= 1:
                if es_vocal(car):
                    tiene_vocal_dos_primeras = True
                    
            cc += 1
            
    if cont_dos_digitos_si_s > 0:
        promedio = sum_carac_dos_digitos_si_s // cont_dos_digitos_si_s            
    else:
        promedio = 0
        
    print(cont_igual_voc_cons_par)
    print(mayor)
    print(promedio)
    print(cont_dos_primera_vocal_si_ra)
    
if __name__ == '__main__':
    test()