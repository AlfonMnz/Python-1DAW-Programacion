import turtle


class Tortuga(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

t = Tortuga()
print(dir(t))
t.forward(100)
