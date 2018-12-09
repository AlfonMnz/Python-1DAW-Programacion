"""
 Crear una tabla para contactos
 definir en las clases la funcionalidad para guardar y recuperar contactos de la base de datos
 va a tener un metodo guardar contactos
 Recuperar contacto con nombre
 Que error produce cuando le pedimos algo que no existe
 El método cargar agenda que cargue todos los contactos desde la base de datos en memoria como diccionario de objetos.
"""

import sqlite3
from tercero import ClasePersona


def añadir_contacto(contacto):
    c.execute('''INSERT INTO contacto VALUES (?, ?, ?, ?);''',
              (contacto.nombre, contacto.edad, contacto.telefono, contacto.email))
    conn.commit()
    

def ver_contacto(nombre_contacto):
    c.execute('SELECT * FROM contacto WHERE contacto.nombre = ?', (nombre_contacto,))
    return c.fetchone()


def cargar_agenda():
    agenda = []
    agenda.append(c.execute('''SELECT * FROM contacto'''))


conn = sqlite3.connect('agenda.db')
c = conn.cursor()
c1 = ClasePersona.Contacto('Antonio', 24, 111222333, 'trolo@lolo.com')
c2 = ClasePersona.Contacto('Fran', 24, 111222333, 'trolo@lolo.com')
c3 = ClasePersona.Contacto('Joan', 24, 111222333, 'trolo@lolo.com')
añadir_contacto(c1)
añadir_contacto(c2)
añadir_contacto(c3)
conn.commit()
conn.close()
conn = sqlite3.connect('agenda.db')
c = conn.cursor()
print(ver_contacto('Antonio'))
