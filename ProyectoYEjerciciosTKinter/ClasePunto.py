"""
A) es suma de puntos, si a un punto no le damos parámetros se inicializa en 0,0
B) Definir la clase traza que contiene una serie de instancias punto, para guardar los puntos dentro de la clase traza
vamos a guardar una lista de tal forma que un objeto de la clase traza tiene muchos objetos de la clase puntos.
Añadir nuevo punto, comparar dos trazas (Serán iguales si sus puntos son iguales) Si una traza no se le pasan parámetros
inicia una lista vacía
Distancia de los puntos
Longitud de la traza
Guardar en un fichero
Leer el fichero
Método dibuja traza, que dibuja la traza
Y capturar puntos y guardar en traza.
Sobre esta clase traza definir los operadores len y p in t
"""
from math import sqrt
import turtle


class Punto:
    def __init__(self, xcor=0.00, ycor=0.00):
        self.x = xcor
        self.y = ycor

    def __eq__(self, punto):
        return (self.x, self.y) == (punto.x, punto.y)

    def __gt__(self, punto):
        return (self.modulo()) > (punto.modulo())

    def __ge__(self, punto):
        return (self.modulo()) >= (punto.modulo())

    def __lt__(self, punto):
        return (self.modulo()) < (punto.modulo())

    def __le__(self, punto):
        return (self.modulo()) <= (punto.modulo())

    def suma(self, punto):
        return Punto(punto.x + self.x, self.y + punto.y)

    def resta(self, punto):
        return Punto(self.x - punto.x, self.y - punto.y)

    def distancia(self, punto):
        d = sqrt(((punto.x - self.x) ** 2) + ((punto.y - self.y) ** 2))
        return d

    def modulo(self):
        return sqrt(((self.x) ** 2) + (self.y) ** 2)


class Traza:
    def __init__(self, lista_traza=[]):
        self.trazado = lista_traza
        self.i = 0

    def __eq__(self, traza):
        return self.trazado == traza.trazado

    def __next__(self):
        self.i += 1
        if self.i < len(self.trazado):
            return self.trazado[self.i]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.trazado)

    def __contains__(self, item):
        return item in self

    def add_punto(self, punto):
        self.trazado.append(punto)

    def longitud(self):
        long = 0
        for punto in range(len(self.trazado) - 1):
            suma = self.trazado[punto].distancia(self.trazado[punto + 1])
            long += suma
        return long

    def guardar(self, fichero):
        fich = open(fichero, 'a')
        for punto in self.trazado:
            fich.write(str(punto) + ',')
        fich.close()

    def leer(self):
        fichero = open('puntos.txt')
        for linea in fichero:
            print(linea)
        fichero.close()

    """def pinta_traza(self):
        tortuga = turtle.Turtle()
        screen = turtle.Screen()
        for punto in self.trazado:
            tortuga.goto(punto.x, punto.y)

        screen.exitonclick()"""


"""tortuga = turtle.Turtle()
screen = turtle.Screen()


def pintar_turtle(x, y):
    lista = []

    lista.append(Punto(x,y))
    tortuga.setpos(x,y)
    return lista"""

"""def add_traza(x,y):
    lista_puntos = pintar_turtle(x,y)
    traza = Traza(lista_puntos)"""

"""screen.onclick(pintar_turtle)
screen.onclick(add_traza, btn=3)
screen.mainloop()"""

p1 = Punto(320, 0)
p2 = Punto(0, 320)
p3 = Punto(-320, 0)
p4 = Punto(0, -320)
t1 = Traza()
t1.add_punto(p1)
t1.add_punto(p2)
t1.add_punto(p3)
t1.add_punto(p4)
for i in t1:
    print(i)
