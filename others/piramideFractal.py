from tkinter import *

def square(canvas, x, y, r):
    left = x - r
    top = y - r

    right = x + r
    down = y + r
    print(f"{left} {top} {right} {down}")
    canvas.create_rectangle((left,top,right,down), outline="yellow", fill="blue")


def iniciar():
    root = Tk()
    root.title ("Semana 14")
    
    ancho = root.winfo_screenwidth() //2
    alto = root.winfo_screenheight()

    # Ancho alto margen_izq margen_der
    root.geometry(f"{ancho}x{alto}+0+0")
    
    # Lienzo
    canvas = Canvas(root,width=ancho,height=alto)
    canvas.grid(row=0, column=0) 
    # tupla -> (x,y,ancho,alto)
#    canvas.grid(column=0,row=0)
#    canvas.create_line((0,0,ancho,alto))
#    canvas.create_line((0,0,500,500))
#   
#    for i in range(20):
#        canvas.create_line((40,i*30,ancho-40,i*30))
#
    canvas.create_rectangle((0,0,500,500), outline="red", fill="white")
    square(canvas, ancho//2, alto//2, 50)

    # Muestra la ventana
    root.mainloop()

if __name__ == "__main__":
    iniciar()
