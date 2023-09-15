# Creacion de matriz

n = 3 # Filas
m = 2 # Columnas

# Alternativa 1
#m1 = []
#for i in range(n):
#    m1.append([])
#    for j in range(m):
        

# Alternativa 2
# Creamos filas
m2 = [None]*n
# Creamos columnas
for f in range(n):
    m2[f] = [None]*m

# Alternativa 3
# Expresion por comprension: Con el for tenemos las vueltas de ciclo donde en cada vuelta crea [None]*m
m3 = [[None]*m for f in range(n)]



# Acceso individual

# El primer [] representa la fila y el segundo las columnas
m1[0][1] = 10


