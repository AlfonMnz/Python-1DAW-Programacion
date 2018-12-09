'''Ejercicio 51. Crear un diccionario cuya clave sea el número de matrícula y los datos del alumno será una tupla de nombre
dirección, teléfono y email. En el sistema existe una serie de cursos, cada curso tendrá un identificador y una descripción.
Necesitamos crear una estructura de enlace entre alumno y curso de tal forma que sepamos qué alumnos están matriculados en cada curso.
El ejercicio nos pide que de forma interactiva podramos listar los alumnos.'''

from tkinter import *
from threading import Thread
from abecedario import *
from random import *
import random

import time
import os

'''class Application(Frame):
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
        while True:
            try:
                time.sleep(0.00001)
                img = PhotoImage(file="C:\dildo.gif", format="gif - {}".format(self.num))

                self.label.config(image=img)
                self.label.image = img

                self.num += 1
            except:
                #self.close()
                self.num = 0

    def close(self):
        os._exit(0)
root = Tk()

app = Application(root)'''

base_alumnos = dict()
cursos = dict()
matriculados = dict()


def añadir_alumno(clave, nombre, tel, email):
    base_alumnos[clave] = (nombre, tel, email)
    return base_alumnos


def generar_alumno():
    name = ""
    for letra_nombre in range(6):
        pito = random.choice(MINUSCULA)
        name += pito
    num = 0
    for potencia_diez in range(9):
        randnum = randint(0, 9)
        num += randnum * (10 ** potencia_diez)
    email = ''
    for letra_nombre in range(9):
        pito = random.choice(MINUSCULA)
        email += pito
    email = email + random.choice(('@gmail.com', '@hotmail.com'))
    clave = 0
    for potencia_diez in range(5):
        randnum = randint(0, 9)
        clave += randnum * (10 ** potencia_diez)

    añadir_alumno(clave, name, num, email)
    return (clave, name, num, email)


def añadir_cursos(clave, descripcion):
    cursos[clave] = descripcion
    return cursos


def generar_curso():
    clave = 0

    for potencia_diez in range(6):
        numero = randint(0, 9)
        clave += numero * (10 ** potencia_diez)
    letra = random.choice(MAYUSCULA)
    str(clave) + str(letra)
    descripcion = random.choice(
        ('Dildo', 'Consiste en lanzar aros', 'Aros consiste lanzar en', 'Primerizos Anales', 'La masturbación y tú',
         'Podemos', 'Eres podemita y quieres solucionarlo.', 'Cuando te tiras un pedo y te cagas un poquito',
         '¿Mi Python me es infiel?',
         'Hago un tutorial y pasa esto', 'Hago un ejercicio en python y pasa esto.'))
    añadir_cursos(clave, descripcion)
    return (clave, descripcion)


def matricular():
    datos_alum = generar_alumno()
    datos_curs = generar_curso()
    matriculados[datos_curs[0]] = datos_alum
    print(matriculados)


def listado():
    id_curso = input('Introduce el id del curso:\n')
    matriculados


matricular()
