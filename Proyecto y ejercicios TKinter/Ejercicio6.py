"""
Crear una función que le demos un fichero de texto en formato csv y esa función genere una base de datos con la misma
estructura del fichero, con manejo de excepciones.
Si falla la linea, debe ignorar la linea y carga las demas.
"""
import sqlite3
from tercero import ClasePersona


def añadir_contacto(contacto):
    c.execute('''INSERT INTO contacto VALUES (?, ?, ?, ?);''',
              (contacto.nombre, contacto.edad, contacto.telefono, contacto.email))
    conn.commit()

def leer_fichero(nombrefichero):
    archivo = open(nombrefichero)
    for linea in archivo:
        pass
conn = sqlite3.connect('agenda.db')
c = conn.cursor()
