total_v = 0
cant_v = 0
cant_v_ct = 0
cant_v_cqs = 0
cant_v_mc = False

num = int(input('\nIngrese las unidades vendidas: '))
while num >= 0 :
    total_v += num
    cant_v+=1
    if(num >= 100 and num <=300):
        cant_v_ct += 1
    elif(num == 400 or num == 500 or num==600):
        cant_v_cqs += 1
    elif(num < 50):
        cant_v_mc = True
    num = int(input('Ingrese las unidades vendidas: '))

print('\nLas unidades vendidas son: \n')
print(' Cantidad: ', cant_v)
print(' Total: ', total_v)
print(' Entre 100 y 300: ',cant_v_ct)
print(' De 400, 500 o 600 unidades son: ', cant_v_cqs)
if(cant_v_mc == True):
    print(' Hubo una venta menor a 50') 
print('\n')