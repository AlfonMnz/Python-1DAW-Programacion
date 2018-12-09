import turtle
import time
import pyglet
c=1
# create a player and queue the song
player = pyglet.media.Player()
sound = pyglet.media.load('canciones//creditos.wav')
player.queue(sound)

# keep playing for as long as the app is running (or you tell it to stop):


player.play()
pantasha = turtle.Screen()
pantasha.setup(width=800, height=600, startx=0, starty=0)

lectura = turtle.Turtle()
lectura.hideturtle()
fichero = open("creditos.txt")
for i in fichero:
    lectura.write(i,font=("Comic Sans MS", 25, "normal"), align='center')
    time.sleep(3)
    pantasha.bgpic("creditos_imagenes//ensalada"+str(c)+".gif")
    c+=1
    if c == 9:
        c = 1
    lectura.clear()
fichero.close()
player.eos_action = pyglet.media.SourceGroup.loop
pantasha.mainloop()