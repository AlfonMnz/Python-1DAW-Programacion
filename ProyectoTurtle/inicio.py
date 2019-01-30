import turtle
import time
import os
import pyglet

# create a player and queue the song
player = pyglet.media.Player()
sound = pyglet.media.load('canciones//intro.wav')
player.queue(sound)

# keep playing for as long as the app is running (or you tell it to stop):


player.play()
pantalla = turtle.Screen()
pantalla.setup(width=410, height=550, startx=0, starty=0)


# pantalla.register_shape("menu.gif")
def inicia(x, y):
    player.pause()
    iniciar.shape("Botones//iniciarp.gif")
    time.sleep(0.25)
    iniciar.shape("Botones//iniciar.gif")
    os.system('py ConSumo.py')
    pantalla.bye()
    time.sleep(2)


def credito(x, y):
    player.pause()
    creditos.shape("Botones//creditosp.gif")
    time.sleep(0.25)
    creditos.shape("Botones//creditos.gif")
    pantalla.bye()
    os.system('py lectura_creditos.py')

    time.sleep(2)

def adios(x,y):
    salir.shape("Botones//salirp.gif")
    time.sleep(0.25)
    salir.shape("Botones//salir.gif")
    pantalla.bye()
pantalla.register_shape("Botones//iniciar.gif")
pantalla.register_shape("Botones//iniciarp.gif")
pantalla.register_shape("Botones//creditos.gif")
pantalla.register_shape("Botones//creditosp.gif")
pantalla.register_shape("Botones//salir.gif")
pantalla.register_shape("Botones//salirp.gif")
pantalla.bgpic("menu.gif")
iniciar = turtle.Turtle()
iniciar.speed(0)
iniciar.shape("Botones//iniciar.gif")
iniciar.up()
iniciar.goto(0, 100)
creditos = turtle.Turtle()
creditos.up()
creditos.shape("Botones//creditos.gif")
creditos.speed(0)
salir = turtle.Turtle()
salir.up()
salir.speed(0)
salir.goto(0, -100)
salir.shape("Botones//salir.gif")
iniciar.onclick(fun=inicia, btn=1, add=None)
creditos.onclick(credito)
salir.onclick(adios)
pantalla.mainloop()
