import objeto

def principal():
    e1 = objeto.Empleado(1, 'Fran', 'Bv Estacion 123', 50000, 1)
    
    # Visualzacion de los valores del objeto
    #print(e1.__str__()) -> Equivalente al de abajo
    print(e1)

if __name__ == "__main__":
    principal()
