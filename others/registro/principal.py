import registro

class Empleado:
    pass

def principal():
    e1 = registro.init(1988, 'Maria', 'Alvear 340', 600000, 3)
    registro.write(e1)

if __name__ == "__main__":
    principal()
