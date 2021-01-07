import DatabaseRepository
import UI
from utils import get_usr_data
from utils import wait_for_user_input

def alta_patrocinador(db):
    nombre, prevision = UI.input__patrocinador()
    db.try_execute(
        f"INSERT INTO Patrocinador (Nombre, Prevision) VALUES (\"{nombre}\",{prevision})"
    )
    db.commit()

def no_economica(db):
    pass

def subasta(db):
    pass

def fijar(db):
    """Fijamos el patrocinador que gana una determinada puja"""

    # Mostramos las actividades subastadas que no han sido terminadas
    # Si no hay actividades subastadas finalizamos
    try:
        db.mostrar_subastadas_no_asignadas()
    except Exception:
        print("No se encontraron actividades subastadas no asignadas ya")
        print("No se hace nada")
        input("Pulsa una tecla para CONTINUAR...")
        return

    # El usuario selecciona la puja para fijar su patrocinador
    id_actividad_subastada = get_usr_data("Introduzca el id de la actividad subastada: ", int, "El identificador dado no es valido")

    # Fijamos el patrocinador y lo mostramos
    db.fijar_patrocinador(id_actividad_subastada)
    wait_for_user_input()
