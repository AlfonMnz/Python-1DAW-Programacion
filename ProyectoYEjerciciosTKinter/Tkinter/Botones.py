"""
Vamos a hacer un botón sencillo que sea una etiqueta que cuando se pulse el boton aumente eso
Que vaya cambiando automáticamente de color
"""

from tkinter import *
vagina = 0
def supercolegasdelinfierno():
    global vagina
    global root
    vagina +=1
    u.config(text=vagina)
    if vagina%2 != 0:
        u.config(background="red")
    else:
        u.config(background="blue")

root = Tk()
u = Label(root, text=vagina)
u.pack()
pene = Button(root,text = 'hurfles', command=supercolegasdelinfierno)
pene.pack()

root.mainloop()