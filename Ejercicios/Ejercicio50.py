'''Ejercicio 50. Queremos crear un diccionario de teléfono donde la clave sea el nombre de la persona y el valor su teléfono.
Apartado b) Creamos funcionalidad para crear contactos siendo el contacto una tupla(nombre,teléfono).
Apartado c) 3 agendas: Amigos, Familia, Trabajo
Apartado d) Vamos a crear una función que fusione las 3 agendas. Se le pasa una lista de agendas y devuelve una agenda. Esta función
debe detectar si hay duplicados. Si detecta usuarios duplicados generamos un diccionario inverso que la clave sea el tlf y valor la
lista de usuarios que contiene el tlf
Apartado e) hacer un diccionario por comprensión que genere los nombres de usuario de 4 letras al azar y num al azar'''

from tkinter import *
from threading import Thread
from abecedario import *
from random import *
import random

import time



class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)
        root.protocol("WM_DELETE_WINDOW", self.close)

        self.num = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, bd=0)
        self.label.pack()

        Thread(target=self.animate).start()

    def animate(self):
        while self.num >= 0:
            try:
                time.sleep(0.0004)
                img = PhotoImage(file="C:\\Users\\Oboe\\Desktop\\Alfonso\\Chopeos\\3.gif", format="gif - {}".format(self.num))

                self.label.config(image=img)
                self.label.image = img

                self.num += 1
            except:
                self.num = -1
                root.destroy()

    def close(self):
        Button(root, text="Quit", command=quit).pack()


root = Tk()

app = Application(root)


amigos = dict()
familia = dict()
trabajo = dict()
gogeta = dict()

amigos['Juan'] = 678122517
amigos['Echenique'] = 687455555
familia['Pepa'] = 666666666
trabajo['Luis'] = 654654654


def nomb():
    nombre = input('Introduce el nombre de quien quieras añadir:\n')
    telefono = int(input('Introduce el teléfono:\n'))
    respuesta = input('Pon A para amigos, F, para familia, T para trabajo:\n')
    respuesta = respuesta.lower()
    añadir_agenda(nombre, telefono, respuesta)


def añadir_agenda(respuesta, nombre, telefono):
    tupla_añadir = respuesta, nombre, telefono
    agenda(tupla_añadir)


def agenda(tupla_añadir):
    if tupla_añadir[0] == 'a':
        amigos[tupla_añadir[1]] = tupla_añadir[2]
    elif tupla_añadir[0] == 'f':
        familia[tupla_añadir[1]] = tupla_añadir[2]
    else:
        trabajo[tupla_añadir[1]] = tupla_añadir[2]


def fusion():
    for nombre in amigos.keys():
        gogeta[nombre] = amigos[nombre]
    for nombre in familia.keys():
        gogeta[nombre] = familia[nombre]
    for nombre in trabajo.keys():
        gogeta[nombre] = trabajo[nombre]
    print(gogeta)

    root.mainloop()




def generador_de_amigos():
    tupla_letras = ()
    name = ""
    for letra in range(4):
        pito = random.choice(MINUSCULA)
        name += pito



    num = 0
    for potencia_diez in range(9):
        randnum = randint(0, 9)
        num += randnum * (10 ** potencia_diez)

    opcion = random.choice('aft')

    añadir_agenda(opcion,name.capitalize(),num)


generador_de_amigos()
generador_de_amigos()
generador_de_amigos()
generador_de_amigos()
generador_de_amigos()
generador_de_amigos()
fusion()
