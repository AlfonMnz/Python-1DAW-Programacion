import mysql.connector


class ControlBD:
    def __init__(self, user='root', password='1234', host='127.0.0.1', database='espotifai'):
        self.cnx = ''
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.numero_album = self.generador_album(self.seleccionar_max_album())
        self.numero_cancion = self.generador_cancion(self.seleccionar_max_cancion())
        self.numero_interprete = self.generador_interprete(self.seleccionar_max_interprete())

    def abrir_conexion(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host,
                                           database=self.database)

    def cerrar_conexion(self):
        self.cnx.close()
        self.cnx = ''

    def cargar_albumesBD(self):
        self.abrir_conexion()
        query = '''SELECT * FROM album'''
        c = self.cnx.cursor()
        c.execute(query)
        self.cerrar_conexion()
        return c

    def seleccionar_album(self, codigo):
        self.abrir_conexion()
        c = self.cnx.cursor()
        query = '''SELECT * FROM album WHERE idalbum = {}'''.format(codigo)
        c.execute(query)
        resultado = c.fetchall()
        self.seleccionar_canciones_de_un_album(resultado[0][0])
        return resultado

    def seleccionar_canciones_de_un_album(self, codigo):
        self.abrir_conexion()
        c = self.cnx.cursor()
        query = '''SELECT * FROM cancion WHERE idalbum = {}'''.format(codigo)
        c.execute(query)
        return c

    def seleccionar_max_album(self):
        self.abrir_conexion()
        c = self.cnx.cursor()
        query = '''SELECT MAX(idalbum) FROM album'''
        c.execute(query)
        maximo = c.fetchone()
        self.cerrar_conexion()
        return maximo[0]

    def generador_album(self, inicial):
        i = inicial
        while True:
            i += 1
            yield i

    def seleccionar_max_cancion(self):
        self.abrir_conexion()
        c = self.cnx.cursor()
        query = '''SELECT MAX(codigo) FROM cancion'''
        c.execute(query)
        maximo = c.fetchone()
        self.cerrar_conexion()
        return maximo[0]

    def generador_cancion(self, inicial):
        i = inicial
        while True:
            i += 1
            yield i

    def seleccionar_max_interprete(self):
        self.abrir_conexion()
        c = self.cnx.cursor()
        query = '''SELECT MAX(idinterprete) FROM interprete'''
        c.execute(query)
        maximo = c.fetchone()
        self.cerrar_conexion()
        return maximo[0]

    def generador_interprete(self, inicial):
        i = inicial
        while True:
            i += 1
            yield i

    def insertar_album(self, album):
        pass


cbd = ControlBD()
print("el siguiente del generador de album es:", next(cbd.numero_album))
print("el siguiente del generador de album es:", next(cbd.numero_album))
print("el siguiente del generador de cancion es es:", next(cbd.numero_cancion))
print("el siguiente del generador de cancion es es:", next(cbd.numero_cancion))
print("el siguiente del generador de interprete es :", next(cbd.numero_interprete))
print("el siguiente del generador de interprete es:", next(cbd.numero_interprete))
