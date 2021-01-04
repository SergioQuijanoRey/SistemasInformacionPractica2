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
    pass

def hora_invitado(db):
    dni = input("Inserte el dni del Invitado (ej: 00000000X): ")
    alfombra = get_usr_data("Inserte el identificador de la alfombra roja: ", int, "El dato introducido no es un entero")
    hora = input("Inserte la hora a la que acude el invitado ( ej: 20:00:00): ")

    db.try_execute(
        f"INSERT INTO Acudir(DNIInvitado, idAlfombraRoja, hora) VALUES (\"{dni}\", {alfombra}, \"{hora}\")"
    )

    

def permiso_periodista(db):
    pass
