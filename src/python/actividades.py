import database
import UI 
from utils import get_usr_data

def crear_actividad(db):

    idActividad, descripcion, fecha = UI.input_actividad()
    db.try_execute(
        f"INSERT INTO Actividad VALUES ({idActividad}, {descripcion}, {fecha})"
    )
    db.commit()



def rueda_pelicula(db):
    ruedaPrensa = get_usr_data("Inserte el identificador de la rueda de prensa: ", int, "El dato introducido no es un entero")
    pelicula = get_usr_data("Inserte el identificador de la película: ", int, "El dato introducido no es un entero")
    nombre = input("Inserta el nombre de la Rueda de Prensa: ")
    plazas = get_usr_data("Inserte el numero de plazas: ", int, "El dato introducido no es un entero")
    lugar = input("Inserte el lugar: ")

    db.try_execute(
        f"INSERT INTO RuedaDePrensaAsigna(IdRuedaPrensa, idPelicula, nombre, plazas, lugar) VALUES ({ruedaPrensa}, {pelicula}, \"{nombre}\", {plazas}, \"{lugar}\")"
    )
    db.commit()
    

    


def hora_invitado(db):
    dni = input("Inserte el dni del Invitado (ej: 00000000X): ")
    alfombra = get_usr_data("Inserte el identificador de la alfombra roja: ", int, "El dato introducido no es un entero")
    hora = input("Inserte la hora a la que acude el invitado ( ej: 20:00:00): ")

    db.try_execute(
        f"INSERT INTO Acudir(DNIInvitado, idAlfombraRoja, hora) VALUES (\"{dni}\", {alfombra}, \"{hora}\")"
    )

    db.commit()
    

def permiso_periodista(db):
    pass
