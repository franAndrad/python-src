def is_num(dato):
    return dato in '0123456789'

def is_letra(dato):
    return 'A' <= dato <= 'z' 

#palabra = input('Ingrese la palabra(separada por espacios en blanco y termina con .):')
palabra = "En el 2020 hubo 130 alumnos en el 1k07."

cpn=cl=cn=cc=cp=0
acum_c_n=0

#Punto 2
ultimo_c=0
c_palabras_td_y_l = 0

#Punto 3
es_Primero = True
long_palabra_corta = 0
pos_palabra_corta = 0

#Punto 4
c_palabras_ch_pos_4 = 0
es_c = False
es_ch = False

for c in palabra:
    if c == ' ' or c =='.':
        
        if cl > 0 or cn > 0:
            cp += 1

        if cn == cc:
            cpn += 1


        if is_num(ultimo_c) and cl > 0:
            c_palabras_td_y_l += 1
        
        if es_Primero:
            long_palabra_corta = cc
            es_Primero = False
        elif cc < long_palabra_corta:
            long_palabra_corta = cc
            pos_palabra_corta = cp

        if es_ch:
            c_palabras_ch_pos_4 += 1

        acum_c_n += 1
        
        cn = 0
        cc = 0
        cl = 0
        es_c = False
        es_ch = False

    else:    
        ultimo_c = c
        cc += 1
        if is_num(c):
            cn += 1
        
        if is_letra(c):
            cl += 1
    
        if cl >= 4:
            if c == 'c':
                es_c = True
            elif c == 'h' and es_c:
                es_ch = True
                

if cpn > 0:
  print("promedio palabras formadas por solo digitos",acum_c_n/cpn)

print("cantidad de palabra que terminan en digito y tienen al menos una letra",c_palabras_td_y_l)
print("longitud de la palabra mas corta",long_palabra_corta,"su posicion es",pos_palabra_corta)
print("cantidad de palabras que tienen ch a partir del 4 caracter",c_palabras_ch_pos_4)
