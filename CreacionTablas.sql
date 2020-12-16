CREATE TABLE Invitados (
    DNIInvitado VARCHAR2(9) PRIMARY KEY,
    Nombre VARCHAR2(100),
    covid BOOLEAN DEFAULT FALSE NOT NULL
);

/**CREATE TABLE Periodista(
    DNIPeriodista, Nombre, covid
);

CREATE TABLE Jueces(
    DNIJuez, Nombre
);

CREATE TABLE Nominados(
    DNINominado,Nombre
);

CREATE TABLE Asistentes (
    DNIAsistente, Nombre, CuentaBancaria, Covid
);

CREATE TABLE Actividad(
    IdActividad, Descripción, Fecha
);

CREATE TABLE AlfombraRoja(
    idAlfombraRoja, horaInicio, horaFin, lugar
);

CREATE TABLE ActividadSubastada(
    IdActividadSubastada, Nombre, Lugar
);

CREATE TABLE Gala(
    idGala, Presentador
);

CREATE TABLE Patrocinador (
    IdPatrocinador, Nombre, Prevision
);

CREATE TABLE Pelicula(
    idPelicula,  Nombre, Genero
);

CREATE TABLE ActividadAsignada(
    IdActividadAsignada
);

CREATE TABLE UsarEntradas(
    IdEntrada,idActividad, DNIAsistentes, Cantidad, Devolucion
);

CREATE TABLE AbonaPagos(
    IdPago, Cantidad, IdEntrada
);

CREATE TABLE Acudir(
    DNIInvitado, idAlfombraRoja,  hora
);

CREATE TABLE Acceder(
    DNIPeriodista, IdRuedaPrensa
);

CREATE TABLE RuedaDePrensaAsigna(
    IdRuedaPrensa, idPelicula, nombre, plazas, lugar
);

CREATE TABLE Puja (
    idPatrocinador, IdActividad, Valor
);

CREATE TABLE OfertaActividadNoEconomica(
    idActividadNoEconomica, idPatrocinador, Coste, DescripcionRetribucion
);

CREATE TABLE SerCandidato (
    DNINominado, idCategoria
);

CREATE TABLE PresentadoCategoría(
    idCategoria, Descripción, Presentador, idGala
);

CREATE TABLE ValorarCategoria (
    DNIJuez  , idCategoria
);

CREATE TABLE VotarNominado(
    DNIJuez, DNINominado, idCategoria
);*/
