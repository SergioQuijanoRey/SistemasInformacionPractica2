import DatabaseRepository
import UI
from utils import get_usr_data, get_int
import actividades
from utils import wait_for_user_input

def alta_patrocinador(db):
    # El usuario introduce los datos del patrocinador
    nombre = get_usr_data("Inserte el nombre del patrocinador: ", str, "El dato introducido no es valido")
    prevision = get_usr_data("Inserte prevision: ", float, "El dato introducido no es valido")

    # Añadimos el patrocinador a la base de datos
    db.alta_patrocinador(nombre, prevision)
    wait_for_user_input()

def no_economica(db):
    db.temporal = True

    save = "NOECONOMICA"
    db.savepoint(save)

    try:
        actividades.crear_actividad(db)
    except Exception as e:
        print("No se pudo crear la actividad para la rueda de prensa")
        print(f"El codigo de error fue {e}")
        print("Intentelo de nuevo")
        db.temporal = False
        return


    db.mostrar_patrocinadores()
    idpatro = get_usr_data("Inserte el identificador del patrocinador: ",int, "El dato introducido no es un entero")

    coste = get_usr_data("Inserte el coste de la actividad: ",float, "El dato introducido no es valido")
    descrip = get_usr_data("Inserte la descripcion de la retribucion: ", str, "Los datos introducidos no son validos" )
    actividad = db.actividad_mayor()

    db.temporal = False
    db.oferta_no_economica(actividad, idpatro, coste, descrip, save)
    wait_for_user_input()



def subasta(db):
    """ Un patrocinador hace una puja en una subasta"""

    # Mostramos las actividades que se pueden subastar
    db.mostrar_subastadas()
    idactividad = get_usr_data("Id de la actividad: ",int, "El dato introducido no es un entero")

    # Mostramos los patrocinadores y elegimos
    db.mostrar_patrocinadores()
    idpatro = get_usr_data("Inserte el identificador del patrocinador: ",int, "El dato introducido no es un entero")

    valor = get_usr_data("Inserte el valor de la subasta: ",float, "El dato introducido no es valido")

    db.puja(idactividad, idpatro, valor)
    wait_for_user_input()


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
