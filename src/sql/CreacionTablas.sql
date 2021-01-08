CREATE TABLE IF NOT EXISTS Invitados (
    DNIInvitado VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300),
    covid BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO Invitados (DNIInvitado, Nombre, covid) VALUES
    ("0000000k", "Lucía Salamanca 1", FALSE),
    ("0000001k", "Lucía Salamanca 2", FALSE),
    ("0000002k", "Lucía Salamanca 3", FALSE),
    ("0000003k", "Lucía Salamanca 4", FALSE),
    ("0000004k", "Lucía Salamanca 5", FALSE),
    ("0000005k", "Lucía Salamanca 6", FALSE),
    ("0000006k", "Lucía Salamanca 7", FALSE),
    ("0000007k", "Lucía Salamanca 8", FALSE),
    ("0000008k", "Lucía Salamanca 9", FALSE),
    ("0000009k", "Lucía Salamanca 10", FALSE);

CREATE TABLE IF NOT EXISTS Periodista(
    DNIPeriodista VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300),
    covid BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO Periodista (DNIPeriodista, Nombre, covid) VALUES
    ("0000000k", "Jesus Lopez 1", FALSE),
    ("0000001k", "Jesus Lopez 2", FALSE),
    ("0000002k", "Jesus Lopez 3", FALSE),
    ("0000003k", "Jesus Lopez 4", FALSE),
    ("0000004k", "Jesus Lopez 5", FALSE),
    ("0000005k", "Jesus Lopez 6", FALSE),
    ("0000006k", "Jesus Lopez 7", FALSE),
    ("0000007k", "Jesus Lopez 8", FALSE),
    ("0000008k", "Jesus Lopez 9", FALSE),
    ("0000009k", "Jesus Lopez 10", FALSE);

CREATE TABLE IF NOT EXISTS Jueces(
    DNIJuez VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300)
);
INSERT INTO Jueces (DNIJuez, Nombre) VALUES
    ("0000000k", "Sergio Quijano 1"),
    ("0000001k", "Sergio Quijano 2"),
    ("0000002k", "Sergio Quijano 3"),
    ("0000003k", "Sergio Quijano 4"),
    ("0000004k", "Sergio Quijano 5"),
    ("0000005k", "Sergio Quijano 6"),
    ("0000006k", "Sergio Quijano 7"),
    ("0000007k", "Sergio Quijano 8"),
    ("0000008k", "Sergio Quijano 9"),
    ("0000009k", "Sergio Quijano 10");

CREATE TABLE IF NOT EXISTS Nominados(
    DNINominado VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300)
);
INSERT INTO Nominados (DNINominado, Nombre) VALUES
    ("0000000k", "Antonio Merino 1"),
    ("0000001k", "Antonio Merino 2"),
    ("0000002k", "Antonio Merino 3"),
    ("0000003k", "Antonio Merino 4"),
    ("0000004k", "Antonio Merino 5"),
    ("0000005k", "Antonio Merino 6"),
    ("0000006k", "Antonio Merino 7"),
    ("0000007k", "Antonio Merino 8"),
    ("0000008k", "Antonio Merino 9"),
    ("0000009k", "Antonio Merino 10");

CREATE TABLE IF NOT EXISTS Asistentes (
    DNIAsistente VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(300),
    CuentaBancaria VARCHAR(400),
    Covid BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO Asistentes(DNIAsistente, Nombre, CuentaBancaria, Covid) VALUES
    ("0000000k", "Pilar Aranda 1", "123456789jjx", FALSE),
    ("0000001k", "Pilar Aranda 2", "123456791jjx", FALSE),
    ("0000002k", "Pilar Aranda 3", "123456791jjx", FALSE),
    ("0000003k", "Pilar Aranda 4", "123456791jjx", FALSE),
    ("0000004k", "Pilar Aranda 5", "123456792jjx", FALSE),
    ("0000005k", "Pilar Aranda 6", "123456791jjx", FALSE),
    ("0000006k", "Pilar Aranda 7", "123456790jjx", FALSE),
    ("0000007k", "Pilar Aranda 8", "123456791jjx", FALSE),
    ("0000008k", "Pilar Aranda 9", "123456791jjx", FALSE),
    ("0000010k", "Pilar Aranda 10","123456792jjx", FALSE);


CREATE TABLE IF NOT EXISTS Actividad(
    IdActividad INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(3000),
    Fecha DATE
);

INSERT INTO Actividad(Descripcion, Fecha) VALUES
    ("Desc 0", "2020-12-13"),
    ("Desc 1", "2020-12-13"),
    ("Desc 2", "2020-12-13"),
    ("Desc 3", "2020-12-13"),
    ("Desc 4", "2020-12-13"),
    ("Desc 5", "2020-12-13"),
    ("Desc 6", "2020-12-13"),
    ("Desc 7", "2020-12-13"),
    ("Desc 8", "2020-12-13"),
    ("Desc 9", "2020-12-13"),
    ("Desc 10", "2020-12-13"),
    ("Desc 11", "2020-12-13"),
    ("Desc 12", "2020-12-13"),
    ("Desc 13", "2020-12-13"),
    ("Desc 14", "2020-12-13"),
    ("Desc 15", "2020-12-13"),
    ("Desc 16", "2020-12-13"),
    ("Desc 17", "2020-12-13"),
    ("Desc 18", "2020-12-13"),
    ("Desc 19", "2020-12-13"),
    ("Desc 20", "2020-12-13"),
    ("Desc 21", "2020-12-13"),
    ("Desc 22", "2020-12-13"),
    ("Desc 23", "2020-12-13"),
    ("Desc 24", "2020-12-13"),
    ("Desc 25", "2020-12-13"),
    ("Desc 26", "2020-12-13"),
    ("Desc 27", "2020-12-13"),
    ("Desc 28", "2020-12-13"),
    ("Desc 29", "2020-12-13"),
    ("Desc 30", "2020-12-13"),
    ("Desc 31", "2020-12-13"),
    ("Desc 32", "2020-12-13"),
    ("Desc 33", "2020-12-13"),
    ("Desc 34", "2020-12-13"),
    ("Desc 35", "2020-12-13"),
    ("Desc 36", "2020-12-13"),
    ("Desc 37", "2020-12-13"),
    ("Desc 38", "2020-12-13"),
    ("Desc 39", "2020-12-13"),
    ("Desc 40", "2020-12-13"),
    ("Desc 41", "2020-12-13"),
    ("Desc 42", "2020-12-13"),
    ("Desc 43", "2020-12-13"),
    ("Desc 44", "2020-12-13"),
    ("Desc 45", "2020-12-13"),
    ("Desc 46", "2020-12-13"),
    ("Desc 47", "2020-12-13"),
    ("Desc 48", "2020-12-13"),
    ("Desc 49", "2020-12-13"),
    ("Desc 50", "2020-12-13");

CREATE TABLE IF NOT EXISTS AlfombraRoja(
    idAlfombraRoja INT PRIMARY KEY,
    horaInicio TIME,
    horaFin TIME,
    lugar VARCHAR(3000),
    FOREIGN KEY(idAlfombraRoja) REFERENCES Actividad(idActividad)
);

INSERT INTO AlfombraRoja(idAlfombraRoja, horaInicio, horaFin, lugar) VALUES
    (1, "20:00:00", "21:30:00", "Sala Magna"),
    (2, "20:00:00", "21:30:00", "Sala Magna"),
    (3, "20:00:00", "21:30:00", "Sala Magna"),
    (4, "20:00:00", "21:30:00", "Sala Magna"),
    (5, "20:00:00", "21:30:00", "Sala Magna"),
    (6, "20:00:00", "21:30:00", "Sala Magna"),
    (7, "20:00:00", "21:30:00", "Sala Magna"),
    (8, "20:00:00", "21:30:00", "Sala Magna"),
    (9, "20:00:00", "21:30:00", "Sala Magna");

CREATE TABLE IF NOT EXISTS ActividadSubastada(
    IdActividadSubastada INT PRIMARY KEY,
    Nombre VARCHAR(300),
    Lugar Varchar(3000),
    FOREIGN KEY(idActividadSubastada) REFERENCES Actividad(idActividad)
);

INSERT INTO ActividadSubastada(idActividadSubastada, Nombre, Lugar) VALUES
    (11, "Actividad Subastada 11", "Domingo en la tarde en los coches de choque"),
    (12, "Actividad Subastada 12", "Domingo en la tarde en los coches de choque"),
    (13, "Actividad Subastada 13", "Domingo en la tarde en los coches de choque"),
    (14, "Actividad Subastada 14", "Domingo en la tarde en los coches de choque"),
    (15, "Actividad Subastada 15", "Domingo en la tarde en los coches de choque"),
    (16, "Actividad Subastada 16", "Domingo en la tarde en los coches de choque"),
    (17, "Actividad Subastada 17", "Domingo en la tarde en los coches de choque"),
    (18, "Actividad Subastada 18", "Domingo en la tarde en los coches de choque"),
    (19, "Actividad Subastada 19", "Domingo en la tarde en los coches de choque");


CREATE TABLE IF NOT EXISTS Gala(
    idGala INT PRIMARY KEY,
    Presentador VARCHAR(300),
    FOREIGN KEY(idGala) REFERENCES Actividad(idActividad)
);

INSERT INTO Gala(idGala, Presentador) VALUES
    (20, "1.5 Juan"),
    (21, "1.5 Juan"),
    (22, "1.5 Juan"),
    (23, "1.5 Juan"),
    (24, "1.5 Juan"),
    (25, "1.5 Juan"),
    (26, "1.5 Juan"),
    (27, "1.5 Juan"),
    (28, "1.5 Juan"),
    (29, "1.5 Juan");

CREATE TABLE IF NOT EXISTS Patrocinador (
    IdPatrocinador INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(200),
    Prevision DOUBLE
);

INSERT INTO Patrocinador(Nombre, Prevision) VALUES
    ("Cola Coca", 1000000.0),
    ("Cola Coca", 1000001.0),
    ("Cola Coca", 1000002.0),
    ("Cola Coca", 1000003.0),
    ("Cola Coca", 1000004.0),
    ("Cola Coca", 1000005.0),
    ("Cola Coca", 1000006.0),
    ("Cola Coca", 1000007.0),
    ("Cola Coca", 1000008.0),
    ("Cola Coca", 1000009.0);


CREATE TABLE IF NOT EXISTS Pelicula(
    idPelicula INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(300),
    Genero VARCHAR(300)
);

INSERT INTO Pelicula(Nombre, Genero) VALUES
    ("Padre no hay mas que 1", "Familiar"),
    ("Padre no hay mas que 2", "Familiar"),
    ("Padre no hay mas que 3", "Familiar"),
    ("Padre no hay mas que 4", "Familiar"),
    ("Padre no hay mas que 5", "Familiar"),
    ("Padre no hay mas que 6", "Familiar"),
    ("Padre no hay mas que 7", "Familiar"),
    ("Padre no hay mas que 8", "Familiar"),
    ("Padre no hay mas que 9", "Familiar"),
    ("Padre no hay mas que 10", "Familiar");

CREATE TABLE IF NOT EXISTS ActividadAsignada(
    IdActividadAsignada INT PRIMARY KEY,
    FOREIGN KEY(IdActividadAsignada) REFERENCES ActividadSubastada(idActividadSubastada)
);

INSERT INTO ActividadAsignada(idActividadAsignada) VALUES
    (11),
    (12),
    (13),
    (14),
    (15),
    (19);

CREATE TABLE IF NOT EXISTS UsarEntradas(
    IdEntrada INT,
    IdActividad INT,

    /*PUEDE SER NULO, PARA CREAR LAS ENTRADAS ANTES DE QUE LA GENTE LAS VAYA A COMPRAR*/
    DNIAsistentes VARCHAR(9) DEFAULT NULL,

    Cantidad INT DEFAULT 1,
    Devolucion BOOLEAN NOT NULL DEFAULT FALSE,

    FOREIGN KEY(IdActividad) REFERENCES Actividad(IdActividad),
    FOREIGN KEY(DNIAsistentes) REFERENCES Asistentes(DNIAsistente),

    PRIMARY KEY(IdEntrada, IdActividad)
);

INSERT INTO UsarEntradas(IdEntrada, IdActividad, DNIAsistentes) VALUES
    (1, 1, "0000000k"),
    (1, 2, "0000001k"),
    (1, 3, "0000002k"),
    (2, 4, "0000003k"),
    (2, 5, "0000004k"),
    (2, 6, "0000005k"),
    (3, 7, "0000006k"),
    (3, 8, "0000007k"),
    (3, 9, "0000008k");


CREATE TABLE IF NOT EXISTS AbonaPagos(
    IdPago INT PRIMARY KEY AUTO_INCREMENT,
    Cantidad DOUBLE,
    IdEntrada INT NOT NULL,
    IdActividad INT NOT NULL,

    FOREIGN KEY(IdEntrada, IdActividad) REFERENCES UsarEntradas(IdEntrada, IdActividad)
);

INSERT INTO AbonaPagos(Cantidad, IdEntrada, IdActividad) VALUES
    (200.12, 1, 1),
    (205.12, 2, 4),
    (202.12, 3, 8);



CREATE TABLE IF NOT EXISTS Acudir(
    DNIInvitado VARCHAR(9),
    idAlfombraRoja INT,
    hora TIME,

    FOREIGN KEY(DNIInvitado) REFERENCES Invitados(DNIInvitado),
    FOREIGN KEY(idAlfombraRoja) REFERENCES AlfombraRoja(idAlfombraRoja),
    PRIMARY KEY(DNIInvitado, idAlfombraRoja)
);

INSERT INTO Acudir(DNIInvitado, idAlfombraRoja, hora) VALUES
    ("0000001k", 1, "20:00:00"),
    ("0000002k", 2, "20:00:00"),
    ("0000003k", 3, "20:00:00"),
    ("0000004k", 4, "20:00:00"),
    ("0000005k", 5, "20:00:00");

CREATE TABLE IF NOT EXISTS RuedaDePrensaAsigna(
    IdRuedaPrensa INT PRIMARY KEY,
    idPelicula INT NOT NULL,
    nombre VARCHAR(300),
    plazas INT DEFAULT 100,
    lugar VARCHAR(300),

    FOREIGN KEY(IdRuedaPrensa) REFERENCES Actividad(idActividad),
    FOREIGN KEY(idPelicula) REFERENCES Pelicula(idPelicula)
);

INSERT INTO RuedaDePrensaAsigna(IdRuedaPrensa, idPelicula, nombre, lugar) VALUES
    (30, 1, "Rueda de prensa 0", "Sitio donde se hacen las ruedas de prensa"),
    (31, 2, "Rueda de prensa 1", "Sitio donde se hacen las ruedas de prensa"),
    (32, 3, "Rueda de prensa 2", "Sitio donde se hacen las ruedas de prensa"),
    (33, 4, "Rueda de prensa 3", "Sitio donde se hacen las ruedas de prensa"),
    (34, 5, "Rueda de prensa 4", "Sitio donde se hacen las ruedas de prensa"),
    (35, 6, "Rueda de prensa 5", "Sitio donde se hacen las ruedas de prensa"),
    (36, 7, "Rueda de prensa 6", "Sitio donde se hacen las ruedas de prensa"),
    (37, 8, "Rueda de prensa 7", "Sitio donde se hacen las ruedas de prensa"),
    (38, 9, "Rueda de prensa 8", "Sitio donde se hacen las ruedas de prensa"),
    (39, 10, "Rueda de prensa 9", "Sitio donde se hacen las ruedas de prensa");

CREATE TABLE IF NOT EXISTS Acceder(
    DNIPeriodista VARCHAR(9),
    IdRuedaPrensa INT,

    FOREIGN KEY(DNIPeriodista) REFERENCES Periodista(DNIPeriodista),
    FOREIGN KEY(IdRuedaPrensa) REFERENCES RuedaDePrensaAsigna(IdRuedaPrensa),

    PRIMARY KEY(DNIPeriodista, IdRuedaPrensa)
);

INSERT INTO Acceder(DNIPeriodista, IdRuedaPrensa) VALUES
    ("0000000k", 30),
    ("0000001k", 31),
    ("0000002k", 32),
    ("0000003k", 33),
    ("0000004k", 34);

CREATE TABLE IF NOT EXISTS Puja (
    IdPatrocinador INT ,
    IdActividad INT ,
    Valor DOUBLE NOT NULL,

    FOREIGN KEY(IdPatrocinador) REFERENCES Patrocinador(IdPatrocinador),
    FOREIGN KEY(IdActividad) REFERENCES ActividadSubastada(IdActividadSubastada),

    PRIMARY KEY(IdPatrocinador, IdActividad)
);

INSERT INTO Puja(IdPatrocinador, IdActividad, Valor) VALUES
    (1, 11, 200.20),
    (2, 12, 202.20),
    (3, 13, 204.20),
    (4, 13, 206.20),
    (5, 13, 300.20),
    (3, 13, 204.20),
    (5, 15, 208.20);

CREATE TABLE IF NOT EXISTS OfertaActividadNoEconomica(
    IdActividadNoEconomica INT PRIMARY KEY,
    IdPatrocinador INT NOT NULL,
    Coste DOUBLE,
    DescripcionRetribucion VARCHAR(1000),

    FOREIGN KEY(IdActividadNoEconomica) REFERENCES Actividad(IdActividad),
    FOREIGN KEY(IdPatrocinador) REFERENCES Patrocinador(IdPatrocinador)
);

INSERT INTO OfertaActividadNoEconomica(IdActividadNoEconomica, IdPatrocinador, Coste, DescripcionRetribucion) VALUES
    (41, 1, 200.20, "Descripcion 1"),
    (42, 2, 202.20, "Descripcion 2"),
    (43, 3, 204.20, "Descripcion 3"),
    (44, 4, 206.20, "Descripcion 4"),
    (45, 5, 208.20, "Descripcion 5");

CREATE TABLE IF NOT EXISTS PresentadoCategoria(
    idCategoria INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(3000),
    Presentador VARCHAR(1000),
    idGala INT NOT NULL,

    FOREIGN KEY(idGala) REFERENCES Gala(idGala)
);

INSERT INTO PresentadoCategoria(Descripcion, Presentador, idGala) VALUES
    ("Mejor Actriz no 1", "David Broncano", 22),
    ("Mejor Actriz no 2", "David Broncano", 23),
    ("Mejor Actriz no 3", "David Broncano", 24),
    ("Mejor Actriz no 4", "David Broncano", 25),
    ("Mejor Actriz no 5", "David Broncano", 26);


CREATE TABLE IF NOT EXISTS SerCandidato (
    DNINominado VARCHAR(9),
    IdCategoria INT,

    FOREIGN KEY(DNINominado) REFERENCES Nominados(DNINominado),
    FOREIGN KEY(IdCategoria) REFERENCES PresentadoCategoria(idCategoria),

    PRIMARY KEY(DNINominado, IdCategoria)
);

INSERT INTO SerCandidato(DNINominado, IdCategoria) VALUES
    ("0000000k", 1),
    ("0000001k", 2),
    ("0000002k", 3),
    ("0000003k", 4),
    ("0000004k", 5);

CREATE TABLE IF NOT EXISTS ValorarCategoria (
    DNIJuez VARCHAR(9),
    IdCategoria INT,

    FOREIGN KEY(DNIJuez) REFERENCES Jueces(DNIJuez),
    FOREIGN KEY(IdCategoria) REFERENCES PresentadoCategoria(idCategoria),

    PRIMARY KEY(DNIJuez, IdCategoria)
);

INSERT INTO ValorarCategoria(DNIJuez, IdCategoria) VALUES
    ("0000000k", 1),
    ("0000001k", 2),
    ("0000002k", 3),
    ("0000003k", 4),
    ("0000004k", 5);


CREATE TABLE IF NOT EXISTS VotarNominado(
    DNIJuez VARCHAR(9),
    IdCategoria INT,
    DNINominado VARCHAR(9),

    FOREIGN KEY(DNIJuez) REFERENCES Jueces(DNIJuez),
    FOREIGN KEY(IdCategoria) REFERENCES PresentadoCategoria(idCategoria),
    FOREIGN KEY(DNINominado) REFERENCES Nominados(DNINominado),

    PRIMARY KEY(DNIJuez, IdCategoria, DNINominado)
);

INSERT INTO VotarNominado(DNIJuez, IdCategoria, DNINominado) VALUES
    ("0000001k", 2, "0000001k"),
    ("0000002k", 3, "0000002k"),
    ("0000003k", 4, "0000003k"),
    ("0000004k", 5, "0000004k");
