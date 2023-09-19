import soporte

vector = soporte.vector_unknown_range(300000)

# vector = [1,3,1,1,2,3,3,3,2,3,3,5,5,5,5,5,5,5]

num  = []
cont = []
moda = 0

# 1 Cargo los vectores num y cont
for i in range(len(vector)):
    if vector[i] not in num:
        num.append(vector[i])
        cont.append(1) 
    else:
        indice = num.index(vector[i])
        cont[indice] += 1

# 2 y 3 Calcular moda
frecuencia = max(cont)
cont_num_f_max = 0

for frec in cont:
    if frecuencia == frec:
        cont_num_f_max += 1

if cont_num_f_max == 1:
    indice_frecuencia = cont.index(frecuencia)
    moda = num[indice_frecuencia]


print('Aparecieron', len(num), 'numeros diferentes!')
print('La moda es', moda, 'su freciencia de aparicion es', frecuencia)
# print(num)
# print(cont)