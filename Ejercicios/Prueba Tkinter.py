import time
from tkinter import *

from colorsys import *



def Cronometroo():
    suma = 0
    time.sleep(1)
    suma = suma + 1
    pintar_texto(suma)


def pintar_texto(segundo):
    ventana.canvas.delete("texto")
    ventana.canvas.create_text("Llevamos" + str(segundo), tags="texto")


ventana = Tk()
ventana.canvas = Canvas(width=500, height=60)
ventana.canvas.pack()
ventana.mainloop()
