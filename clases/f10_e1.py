cant_4letras = 0
cl = cp = cmo = cp4 = cplx = 0
lm = False
lmo = False
lxy = False
palabra = 'el mono momoxy toca el xilofon.'
acum_ult_palabra = 0

for l in palabra:
    # Se ejecuta una vez por cada palabra
    if l == ' ' or l == '.':
        if cl > 0:
            cp += 1
            if cl > 4:
                cp4 += 1
            
            if lmo:
                cmo += 1
                lm = False
                lmo = False
            elif lxy:
                cplx += 1
                lxy = False
            
            acum_ult_palabra += cl
            # Me cuenta la cantidad de letras de la ultima palabra  
            cl = 0

    # Se ejecuta una vez por cada letra
    else:
        if l == 'm':
            lm = True
        if lm and lmo == 'o':
            lmo = True       

        if l == 'x' or l == 'y':
            lxy = True    
        
        cl += 1

promedio = acum_ult_palabra / cp

print(cp4)
print(cplx)
print(promedio)
print(cp)
print(cmo)
