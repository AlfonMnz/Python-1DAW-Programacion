"""

Repasico rico
Tenemos una colección de cromos, un album, la iteración del album se le da a través de los cromos

"""

class Cromo:
    damian = 0
    def __init__(self, nombre,valor):
        self.id = Cromo.damian + 1
        Cromo.damian = self.id
        self.nombre= nombre
        self.valor = valor
    def __str__(self):
        return "El id es {}".format(self.id)
a = Cromo("juan",5)
b= Cromo("david",9)
c = Cromo("pan",5)
print(a,b,c)
