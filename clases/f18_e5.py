import random

def menu():
    print("\n ESTADISTICAS:")
    

def cargar_encuesta(v_numero,v_color,v_edad,v_preferencia,cant):
    colores = "Negro", "Blanco", "Azul"
    preferencia = "Cuero", "Tela"
    for i in range(cant):
        v_numero.append(random.randint(35,40))
        v_color.append(random.choice(colores))
        v_edad.append(random.randint(10,25))
        v_preferencia.append(random.choice(preferencia))
              
def mostrar_encuesta(v_numero,v_color,v_edad,v_preferencia,cant):
    pass

def main():
    v_numero = []
    v_color = []
    v_edad = []
    v_preferencia = []
    v_demanda = None
    opc = -1

    cargar_encuesta(v_numero,v_color,v_edad,v_preferencia)



if __name__ == "__main__":
    main()
