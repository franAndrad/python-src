import soporte

vector = soporte.vector_known_range(300000)

#vector = [1,3,1,1,2,3,3,3,2,3,3,5,5,5,5,5,5,5]
moda = 0
c = 300000 * [0]
#c = 20 *[0]

# 1 Cargo los vectores num y cont
for num in vector:
    c[num] += 1

cont_disntitos_0 = 0
for cuenta in c:
    if cuenta != 0:
        cont_disntitos_0 += 1


frecuencia = max(c)
cont_num_f_max = 0

for frec in c:
    if frecuencia == frec:
        cont_num_f_max += 1

if cont_num_f_max == 1:
    moda = c.index(frecuencia)
    
print('Aparecieron', cont_disntitos_0, 'numeros diferentes!')
print('La moda es', moda, 'su freciencia de aparicion es', frecuencia)
# print(num)
# print(cont)