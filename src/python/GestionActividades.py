import database
import UI 

def crear_actividad():

    idActividad, descripcion, fecha = UI.crear_actividad()
    database.try_execute(
        "INSERT INTO Actividad VALUES ({idActividad}, {descripcion}, {fecha})"
    )
    database.commit()