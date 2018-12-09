# Importaciones
import turtle
import random
import pyglet

# create a player and queue the song
player = pyglet.media.Player()
sound = pyglet.media.load('canciones//juego.wav')
player.queue(sound)

# keep playing for as long as the app is running (or you tell it to stop):


player.play()
LIMITE_DERECHO = 500
LIMITE_IZQUIERDO = -500
LIMITE_SUPERIOR = 345
LIMITE_INFERIOR = -345
INICIO_X = 487
VELOCIDAD = 0.75


# Inicialización de la clase Jugador

class Jugador(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.vida = 8
        self.peso = 50
        self.moviendo = False

    # Funciones de movimiento


    def derecha(self):
        if not self.moviendo:
            partida.pantalla.tracer(0)
            self.moviendo = True

            self.shape("Pos Sumo//derecha.gif")
            if self.heading() != 0:
                self.setheading(0)
                partida.pantalla.tracer(1)
            moving()

    def izquierda(self):
        if not self.moviendo:
            partida.pantalla.tracer(0)
            self.moviendo = True

            self.shape("Pos Sumo//izquierda.gif")
            if self.heading() != 180:
                self.setheading(180)
                partida.pantalla.tracer(1)
            moving()

    def arriba(self):
        if not self.moviendo:
            partida.pantalla.tracer(0)
            self.shape("Pos Sumo//arriba.gif")
            self.moviendo = True

            if self.heading() != 90:
                self.setheading(90)
                partida.pantalla.tracer(1)
            self.shape("Pos Sumo//arriba.gif")
            moving()

    def abajo(self):
        if not self.moviendo:
            partida.pantalla.tracer(0)
            self.shape("Pos Sumo//abajo.gif")
            self.moviendo = True

            if self.heading() != 270:
                self.setheading(270)
                partida.pantalla.tracer(1)
            moving()

    def stop(self):
        partida.pantalla.tracer(0)
        self.moviendo = False

        moving()
        partida.pantalla.tracer(1)

    def cont_vida(self):
        self.vida -= 1
        partida.vidas.shape("Vida//vida" + str(self.vida) + ".gif")

    def actualizar_peso(self):
        partida.peso.clear()
        partida.peso.write(self.peso, font=("Comic Sans MS", 18, "normal"))


# Inicializo la clase enemigo.

class Enemigo(turtle.Turtle):
    def __init__(self, decremento=0):
        turtle.Turtle.__init__(self)
        self.decremento = decremento
        self.moviendose = True

    def comido(self):
        partida.jugador.peso -= self.decremento
        partida.pantalla.tracer(0)
        self.goto(447, 0)
        partida.jugador.actualizar_peso()
        self.hideturtle()
        if self in lista_mierda_en_pantalla:
            lista_mierda_en_pantalla.remove(self)
        partida.pantalla.tracer(1)
        partida.jugador.cont_vida()

    def tocar_limite(self):
        partida.pantalla.tracer(0)
        self.hideturtle()
        if self in lista_mierda_en_pantalla:
            lista_mierda_en_pantalla.remove(self)
        # print("ha tocado el limite")
        partida.pantalla.tracer(1)


class Sumo(Enemigo):
    def __init__(self):
        Enemigo.__init__(self)

    def comido(self):
        partida.jugador.peso -= self.decremento
        partida.pantalla.tracer(0)
        partida.jugador.forward(-50)
        self.goto(447, 0)
        partida.jugador.actualizar_peso()
        self.hideturtle()
        if self in lista_mierda_en_pantalla:
            lista_mierda_en_pantalla.remove(self)
        partida.pantalla.tracer(1)
        partida.jugador.cont_vida()


class Comida(turtle.Turtle):
    def __init__(self, bonus=1):
        turtle.Turtle.__init__(self)
        self.bonus = bonus
        self.moviendose = True

    def comido(self):
        partida.jugador.peso += self.bonus
        partida.pantalla.tracer(0)
        self.goto(447, 0)
        partida.jugador.actualizar_peso()
        self.hideturtle()
        if self in lista_mierda_en_pantalla:
            lista_mierda_en_pantalla.remove(self)
        print(len(lista_mierda_en_pantalla))
        partida.pantalla.tracer(1)

    def tocar_limite(self):
        partida.pantalla.tracer(0)
        self.hideturtle()
        if self in lista_mierda_en_pantalla:
            lista_mierda_en_pantalla.remove(self)
        # print("ha tocado el limite")
        partida.pantalla.tracer(1)


class Partida:
    def __init__(self):
        self.iniciar_bonus()
        self.iniciar_pantalla()
        self.iniciar_enemigos()
        self.registrar_shapes()
        self.iniciar_hub()
        self.seleccionar_shapes()
        self.esconder_bonus()
        self.iniciar_posiciones_y_otras_cosas()

    def iniciar_bonus(self):
        """
        Esta función inicializa los objetos de bonus y el jugador.
        """

        self.jugador = Jugador()
        self.pollo = Comida(15)
        self.tarta = Comida(5)
        self.jabali = Comida(10)
        self.bacon = Comida(7)
        self.cerveza = Comida(3)

    def iniciar_enemigos(self):
        """
        Esta función inicializa los enemigos.
        """
        self.anguila = Enemigo(5)
        self.pina = Enemigo(7)
        self.sumo_enemy = Sumo()

    def iniciar_pantalla(self):
        """
         Esta función inicia la pantalla y sus cosas necesarias
        """
        self.pantalla = turtle.Screen()
        self.pantalla._root.resizable(0, 0)
        self.pantalla._root.attributes('-fullscreen', True)
        self.pantalla.title("ConSumo")

    def registrar_shapes(self):
        """
        Esta función registra todos los shapes que se van a usar a lo largo del juego.
        """

        # Registro los shapes que usará el jugador.

        self.pantalla.register_shape("Pos Sumo//derecha.gif")
        self.pantalla.register_shape("Pos Sumo//izquierda.gif")
        self.pantalla.register_shape("Pos Sumo//abajo.gif")
        self.pantalla.register_shape("Pos Sumo//arriba.gif")

        # Registro los shapes de los bonus

        self.pantalla.register_shape("Bonus//cerveza.gif")
        self.pantalla.register_shape("Bonus//bacon.gif")
        self.pantalla.register_shape("Bonus//jabali.gif")
        self.pantalla.register_shape("Bonus//pollo.gif")
        self.pantalla.register_shape("Bonus//tarta.gif")

        # Registro los shapes de los enemigos.

        self.pantalla.register_shape("Enemigos//anguila.gif")
        self.pantalla.register_shape("Enemigos//piña.gif")
        self.pantalla.register_shape("Enemigos//sumo//arriba.gif")
        self.pantalla.register_shape("Enemigos//sumo//abajo.gif")
        self.pantalla.register_shape("Enemigos//sumo//Derecha.gif")
        self.pantalla.register_shape("Enemigos//sumo//izquierda.gif")
        # Registro los shapes de la vida.

        for i in range(9):
            self.pantalla.register_shape("Vida//vida" + str(i) + ".gif")

    def iniciar_hub(self):
        """
        Inicializa la interfaz como las vidas etc.
        """
        self.peso = turtle.Turtle()
        self.vidas = turtle.Turtle()

    def esconder_bonus(self):
        self.jabali.hideturtle()
        self.tarta.hideturtle()
        self.cerveza.hideturtle()
        self.pollo.hideturtle()
        self.bacon.hideturtle()
        self.peso.hideturtle()

    def esconder_enemigos(self):
        self.anguila.hideturtle()
        self.pina.hideturtle()
        self.sumo_enemy.hideturtle()

    def seleccionar_shapes(self):
        self.jugador.shape("Pos Sumo//derecha.gif")
        self.jabali.shape("Bonus//jabali.gif")
        self.tarta.shape("Bonus//tarta.gif")
        self.pollo.shape("Bonus//pollo.gif")
        self.bacon.shape("Bonus//bacon.gif")
        self.cerveza.shape("Bonus//cerveza.gif")
        self.anguila.shape("Enemigos//anguila.gif")
        self.pina.shape("Enemigos//piña.gif")
        self.pantalla.bgpic("fondo.gif")
        self.vidas.shape("Vida//vida" + str(self.jugador.vida) + ".gif")
        self.sumo_enemy.shape("Enemigos//sumo//izquierda.gif")

    def iniciar_posiciones_y_otras_cosas(self):
        self.pantalla.tracer(0)
        self.vidas.up()
        self.vidas.speed(0)
        self.vidas.goto(250, 250)
        self.jugador.up()
        self.peso.up()
        self.sumo_enemy.up()
        self.peso.goto(-400, 300)
        self.peso.write(self.jugador.peso, font=("Comic Sans MS", 18, "normal"))
        self.bacon.up()
        self.jabali.up()
        self.pollo.up()
        self.tarta.up()
        self.cerveza.up()
        self.anguila.up()
        self.pina.up()
        self.bacon.goto(INICIO_X, 0)
        self.bacon.setheading(-180)
        self.jabali.goto(INICIO_X, 0)
        self.jabali.setheading(-180)
        self.pollo.goto(INICIO_X, 0)
        self.pollo.setheading(-180)
        self.sumo_enemy.goto(INICIO_X, 0)
        self.sumo_enemy.setheading(-180)
        self.tarta.goto(INICIO_X, 0)
        self.tarta.setheading(-180)
        self.cerveza.goto(INICIO_X, 0)
        self.cerveza.setheading(-180)
        self.anguila.goto(INICIO_X, 0)
        self.anguila.setheading(-180)
        self.pina.goto(INICIO_X, 0)
        self.pina.setheading(-180)
        self.pantalla.tracer(1)


partida = Partida()

lista_bonus = [partida.bacon, partida.cerveza, partida.tarta, partida.pollo, partida.jabali]

# region Teclas Movimiento
partida.pantalla.onkeypress(partida.jugador.izquierda, "a")
partida.pantalla.onkeypress(partida.jugador.derecha, "d")
partida.pantalla.onkeypress(partida.jugador.arriba, "w")
partida.pantalla.onkeypress(partida.jugador.abajo, "s")
partida.pantalla.onkeypress(partida.jugador.vida, "space")
partida.pantalla.onkeyrelease(partida.jugador.stop, "a")
partida.pantalla.onkeyrelease(partida.jugador.stop, "d")
partida.pantalla.onkeyrelease(partida.jugador.stop, "w")
partida.pantalla.onkeyrelease(partida.jugador.stop, "s")
partida.pantalla.listen()
# endregion

cont_pantalla = 0

lista_enemigos = [partida.pina, partida.anguila, partida.sumo_enemy]


def moving():
    partida.pantalla.tracer(0)
    partida.jugador.fd(len(lista_mierda_en_pantalla))
    partida.pantalla.tracer(1)


def stop():
    pass


lista_mierda_en_pantalla = []


def mover_comida(bonus):
    partida.pantalla.tracer(0)
    bonus.forward(0.5)
    partida.pantalla.tracer(1)


def mover_comida_fast_and_furious_on_the_road(bonus):
    partida.pantalla.tracer(0)
    bonus.forward(1)
    partida.pantalla.tracer(1)


def elegir_bonus():
    partida.pantalla.tracer(0)
    comida = random.choice(lista_bonus)
    mover_comida(comida)
    comida.showturtle()
    lista_mierda_en_pantalla.append(comida)
    partida.pantalla.tracer(1)


def elegir_enemigo():
    partida.pantalla.tracer(0)
    enemigo = random.choice(lista_enemigos)
    mover_comida(enemigo)
    enemigo.showturtle()
    lista_mierda_en_pantalla.append(enemigo)
    partida.pantalla.tracer(1)


lista_coordenadas = [(-439.0, 298.0), (-438.0, 5.0), (-437.0, -233.0), (-189.0, -335.0), (-36.0, -332.0),
                     (218.0, -331.0),
                     (435.0, -223.0), (434.0, -27.0), (432.0, 258.0), (206.0, 355.0), (10.0, 353.0), (-259.0, 351.0)]


def posicion_aleatoria(choice):
    partida.pantalla.tracer(0)
    posicion = random.choice(lista_coordenadas)
    choice.goto(posicion)
    if posicion == (-439.0, 298.0) or posicion == (-438.0, 5.0) or posicion == (-437.0, -233.0):
        choice.setheading(0)
    if posicion == (-189.0, -335.0) or posicion == (-36.0, -332.0) or posicion == (218.0, -331.0):
        choice.setheading(90)
    if posicion == (435.0, -223.0) or posicion == (434.0, -27.0) or posicion == (432.0, 258.0):
        choice.setheading(180)
    if posicion == (206.0, 355.0) or posicion == (10.0, 353.0) or posicion == (-259.0, 351.0):
        choice.setheading(180)
    partida.pantalla.tracer(1)


def elegir_bonus_o_enemigos():
    es_enemigo = random.choice([True, False])
    if es_enemigo:
        elegir_enemigo()
    else:
        elegir_bonus()


def num_bonus():
    numero_bonus = random.randint(3, 8)
    for i in range(numero_bonus):
        elegir_bonus_o_enemigos()


def pillar_coordenadas(x, y):
    print(x, y)


partida.pantalla.onclick(pillar_coordenadas)
while True:

    if partida.jugador.moviendo:
        moving()
    if len(lista_mierda_en_pantalla) <= 4:
        num_bonus()

    for basura in lista_mierda_en_pantalla:
        if basura.moviendose:
            if partida.jugador.moviendo:
                mover_comida_fast_and_furious_on_the_road(basura)
            mover_comida(basura)
        if basura.distance(partida.jugador.xcor(), partida.jugador.ycor()) < 20:
            basura.comido()
            posicion_aleatoria(basura)
        if basura.xcor() >= LIMITE_DERECHO or basura.xcor() <= LIMITE_IZQUIERDO:
            basura.tocar_limite()
            posicion_aleatoria(basura)
        if basura.ycor() >= LIMITE_SUPERIOR or basura.ycor() <= LIMITE_INFERIOR:
            basura.tocar_limite()
            posicion_aleatoria(basura)
