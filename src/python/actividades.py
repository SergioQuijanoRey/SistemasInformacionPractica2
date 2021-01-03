import database
import UI 

def crear_actividad(db):

    idActividad, descripcion, fecha = UI.input_actividad()
    db.try_execute(
        "INSERT INTO Actividad VALUES ({idActividad}, {descripcion}, {fecha})"
    )
    db.commit()

def rueda_pelicula(db):
    pass

def hora_invitado(db):
    pass

def permiso_periodista(db):
    pass