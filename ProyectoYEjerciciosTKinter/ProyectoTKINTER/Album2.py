import tercero.ProyectoTKINTER.ControBBDD


class Album:
    def __init__(self, id_album, id_interprete, nombre, canciones):
        self.id_album = id_album
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.canciones = canciones

    def __str__(self):
        return "Album({},{},{},{})".format(self.id_album, self.id_interprete, self.nombre, self.canciones)


class ColeccionAlbum:
    def __init__(self, controladorBD):
        self.cbd = controladorBD
        self.dic_album = dict()
        self.cargar_albumes()

    def cargar_albumes(self):
        cursorAlbumes = self.cbd.cargar_albumesBD()
        for fila in cursorAlbumes:
            id_album, id_interprete, nombre, canciones = fila
            self.dic_album[id_album] = Album(id_album, id_interprete, nombre, canciones)


class Cancion:
    def __init__(self,codigo, id_album, id_genero):
        self.codigo = codigo
        self.id_album = id_album
        self.id_genero = id_genero



class ColeccionCanciones:
    def __init__(self, controladorBD):
        self.cbd = controladorBD
        self.dic_canciones = dict()
        self.cargar_canciones()

    def cargar_canciones(self):
        pass
