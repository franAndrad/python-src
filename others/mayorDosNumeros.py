import random

a = random.randint(1,10)
b = random.randint(1,10)
print('Entre los valores',a,'y',b)

if(a>b):
    print('El mayor es: ',a)
else:
    if(a<b):
        print('El mayor es: ',b)
    else:
        print('Los dos son iguales')

