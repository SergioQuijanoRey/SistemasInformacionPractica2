import DatabaseRepository
import UI
from utils import get_usr_data
import actividades

def alta_patrocinador(db):
    nombre, prevision = UI.input__patrocinador()
    db.try_execute(
        f"INSERT INTO Patrocinador (Nombre, Prevision) VALUES (\"{nombre}\",{prevision})"
    )
    db.commit()

def no_economica(db):
    actividades.crear_actividad(db)
    actividad = db.actividad_mayor()

    db.mostrar_patrocinadores()
    idpatro = get_usr_data("Inserte el identificador del patrocinador: ",int, "El dato introducido no es un entero")

    coste = get_usr_data("Inserte el coste de la actividad: ",float, "El dato introducido no es valido")
    descrip = get_usr_data("Inserte la descripcion de la retribucion: ", str, "Los datos introducidos no son validos" )

    db.oferta_no_economica(actividad, idpatro, coste, descrip)



def subasta(db):
    pass

def fijar(db):
    pass
