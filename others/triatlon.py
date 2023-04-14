# tiempo_natacion = input('Ingrese el tiempo en natacion (mm.ss): ')
# tiempo_ciclismo = input('Ingrese el tiempo en ciclismo (mm.ss): ')
# tiempo_pedestre = input('Ingrese el tiempo en pedestre (mm.ss): ')
tiempo_natacion = '22.22'
tiempo_ciclismo = '22.22'
tiempo_pedestre = '22.22'

t_nat_s = int(tiempo_natacion[0] + tiempo_natacion[1]) * 60 + int(tiempo_natacion[3] + tiempo_natacion[4])
t_cic_s = int(tiempo_ciclismo[0] + tiempo_ciclismo[1]) * 60 + int(tiempo_ciclismo[3] + tiempo_natacion[4])
t_pedes_s = int(tiempo_pedestre[0] + tiempo_pedestre[1]) * 60 + int(tiempo_pedestre[3] + tiempo_natacion[4])

t_total = t_nat_s + t_cic_s + t_pedes_s

cantidad_h = divmod(t_total, 3600)
total_h = cantidad_h[0] 
cantidad_min = divmod(cantidad_h[1], 60)
total_min = cantidad_min[0]
total_seg = cantidad_min[1]

t_max = max(t_nat_s,t_cic_s,t_pedes_s)
t_min = min(t_nat_s,t_cic_s,t_pedes_s)

promedio = (t_nat_s + t_cic_s + t_pedes_s) / 3
promedio = round(promedio,2)

print('El tiempo total es '+ str(total_h).rjust(2,'0') + ':' + str(total_min).rjust(2,'0') + ':' + str(total_seg).rjust(2,'0'))
print('El mayor tiempo en segundo es: ',t_max)
print('El menor tiempo en segundo es: ',t_min)
print('El promedio es: ',promedio)
