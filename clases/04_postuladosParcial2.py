def test():
    contenido = 'asd ased asdasde ajvdjaseda adse llave aulo heullo.'
    
    # Punto 1
    tiene_e = False
    cont_palabra_tiene_e = 0 
    
    # Punto 2
    tiene_d = tiene_de = False
    cont_palabra_tiene_de = 0 
    
    # Punto 3
    cc = cont_comienza_ll = 0
    tiene_l = comienza_ll = False
    
    # Punto 4
    tiene_u = False 
    ultimo = cont_palabras_tiene_u_term_lo = esta_l = 0
    
    
    for car in contenido:
        if car == ' ' or car == '.':
            
            # Punto 1
            if tiene_e:
                cont_palabra_tiene_e += 1
            
            # Punto 2
            if tiene_de:
                cont_palabra_tiene_de += 1
            
            # Punto 3    
            if comienza_ll:
                cont_comienza_ll += 1
            
            # Punto 4
            if tiene_u and esta_l == cc-1 and ultimo == 'o':
                cont_palabras_tiene_u_term_lo += 1
            
            # Volver al inicio despues de la palabra 
            
            # Punto 1
            tiene_e = False
            
            # Punto 2
            tiene_d = tiene_de = False
            
            #Punto 3
            tiene_l = comienza_ll = False
            cc = 0
            
            # Punto 4
            tiene_u = False
            esta_l = ultimo = 0
            
        else:
            
            cc += 1
            
            # Punto 1
            if car == 'e' or car == 'E':
                tiene_e = True
                
            # Punto 2
            if car == 'd':
                tiene_d = True
            elif tiene_d and car == 'e':
                tiene_de = True
            else:
                tiene_d = False
            
            # Punto 3
            if car == 'l' and cc == 1:
                tiene_l = True
            if tiene_l and car == 'l' and cc == 2:
                comienza_ll = True 
            
            # Punto 4
            if car == 'u':
                tiene_u = True
            
            if car == 'l':
                esta_l = cc
                
            ultimo = car
            
    print(cont_palabra_tiene_e)  
    print(cont_palabra_tiene_de)
    print(cont_comienza_ll)
    print(cont_palabras_tiene_u_term_lo)
    
if __name__ == '__main__':
    test()
