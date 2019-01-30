"""

"""


class Agenda:
    def __init__(self):
        self.agenda = {}
        self.i = -1

    def __next__(self):
        self.i += 1
        if self.i < len(self.agenda):
            return self.agenda[sorted(list(self.agenda))[self.i]]
        raise StopIteration

    def __iter__(self):
        return self

    def add_contacto(self, nombre, contacto):
        self.agenda[nombre] = contacto


class Contacto:
    def __init__(self, nombre, tlf, email):
        self.nombre = nombre
        self.telefono = tlf
        self.email = email

ag=Agenda()
c1 = ("talgaba", 123456879, 'atalgaba@gmail.com')
c2 = ('hola', 123456789, 'howeifowei@gmail.com')
c3 = ('pepe', 123546787, 'ohnfiwjeiowr@gmail.com')
ag.add_contacto("juan", c1)
ag.add_contacto("david", c2)
ag.add_contacto("paco", c3)
for i in ag:
    print(i)