DROP DATABASE IF EXISTS espotifai;
CREATE DATABASE espotifai;
CREATE TABLE espotifai.Interprete
(
    idinterprete INT PRIMARY KEY,
    idPais INT NOT NULL,
    nombre VARCHAR(619),
    alias VARCHAR(619)
);
CREATE TABLE espotifai.Album
(
    idalbum INT PRIMARY KEY NOT NULL,
    idinterprete INT,
    nombre VARCHAR(619),
    canciones INT
);
CREATE TABLE espotifai.Pais
(
    idPais INT PRIMARY KEY,
    Nombre VARCHAR(619)
);
CREATE TABLE espotifai.Cancion
(
    codigo INT PRIMARY KEY,
    idalbum INT,
    idgenero INT,
    nombre VARCHAR(619),
    duracion INT
);
CREATE TABLE espotifai.Genero
(
    idgenero INT PRIMARY KEY,
    nombre VARCHAR(619),
    descripcion VARCHAR(619)
);

ALTER TABLE espotifai.album
ADD CONSTRAINT album_interprete__fk
FOREIGN KEY (idinterprete) REFERENCES interprete (idinterprete);
ALTER TABLE espotifai.interprete
ADD CONSTRAINT interprete_pais__fk
FOREIGN KEY (idPais) REFERENCES pais (idPais);
ALTER TABLE espotifai.cancion
ADD CONSTRAINT cancion_album__fk
FOREIGN KEY (idalbum) REFERENCES album (idalbum);
ALTER TABLE espotifai.cancion
ADD CONSTRAINT cancion_genero__fk
FOREIGN KEY (idgenero) REFERENCES genero (idgenero);
INSERT INTO espotifai.pais (idPais, Nombre) VALUES (1, 'Huganda');
INSERT INTO espotifai.pais (idPais, Nombre) VALUES (2, 'España');
INSERT INTO espotifai.interprete (idinterprete, idPais, nombre, alias) VALUES (1, 1, 'Bruno Mars', null);
INSERT INTO espotifai.interprete (idinterprete, idPais, nombre, alias) VALUES (2, 2, 'Joaquin Sabina', 'El puto amo');
INSERT INTO espotifai.genero (idgenero, nombre, descripcion) VALUES (1, 'Funk', 'Pues yo que sé socio, esto es una prueba loco');
INSERT INTO espotifai.genero (idgenero, nombre, descripcion) VALUES (2, 'Folk', 'Lo mismo de antes');
INSERT INTO espotifai.album (idalbum, idinterprete, nombre, canciones) VALUES (1, 1, '24K', 9);
INSERT INTO espotifai.album (idalbum, idinterprete, nombre, canciones) VALUES (2, 2, 'Lo niego todo', 12);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (1, 1, 1, '24K Magic', 3);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (2, 1, 1, 'Chunky', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (3, 1, 1, 'Perm', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (4, 1, 1, 'That''s What I Like', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (5, 1, 1, 'Versace on the Floor', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (6, 1, 1, 'Straight up & Down', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (7, 1, 1, 'Calling All My Lovelies', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (8, 1, 1, 'Finesse', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (9, 1, 1, 'Too Good to Say Goodbye', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (10, 2, 2, 'Quien más, quien menos', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (11, 2, 2, 'No tan deprisa', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (12, 2, 2, 'Lo niego todo', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (13, 2, 2, 'Postdata', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (14, 2, 2, 'Lágrimas de mármol', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (15, 2, 2, 'Leningrado', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (16, 2, 2, 'Canción de primavera', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (17, 2, 2, 'Sin pena ni gloria', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (18, 2, 2, 'Las noches de domingo acaban mal', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (19, 2, 2, '¿Qué estoy haciendo aquí?', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (20, 2, 2, 'Churumbelas', NULL);
INSERT INTO espotifai.cancion (codigo, idalbum, idgenero, nombre, duracion) VALUES (21, 2, 2, 'Por delicadeza', NULL);
