import DatabaseRepository
import UI
from utils import *

def crear_actividad(db):
    """Meter cuantas entradas quiere el usuario y hacer el insert """
    descripcion    = input("Inserte la descripcion de la actividad: ")
    fecha          = input("Inserte la fecha de la actividad: ")

    # Creamos la actividad
    try:
        db.crear_actividad(descripcion, fecha)
    except Exception as e:
        print("No se pudo crear la actividad")
        print(f"El codigo de erorr fue {e}")
        wait_for_user_input()
        raise Exception("No se pudo crear la actividad")

def rueda_pelicula(db):
    save = "RUEDAPRENSA"
    db.savepoint(save)

    ruedaPrensa = None
    try:
        ruedaPrensa = crear_actividad(db)
    except Exception as e:
        print("No se pudo crear la actividad para la rueda de prensa")
        print(f"El codigo de error fue {e}")
        print("Intentelo de nuevo")
        return


    db.mostrar_peliculas()
    pelicula = get_usr_data("Inserte el identificador de la película: ",int, "El dato introducido no es un entero")

    nombre = get_usr_data("Inserta el nombre de la Rueda de Prensa: ", str)
    plazas = get_usr_data("Inserte el numero de plazas: ",int, "El dato introducido no es un entero")
    lugar = input("Inserte el lugar: ")

    db.asignar_rueda_pelicula(ruedaPrensa,  pelicula, nombre, plazas, lugar, save)
    wait_for_user_input()


def hora_invitado(db):
    db.mostrar_invitados()
    dni = get_usr_data("Inserte el dni del Invitado: ", str, "Los datos introducidos no son validos" )

    db.mostrar_alfombras()
    alfombra = get_usr_data("Inserte el identificador de la alfombra roja: ",
                            int, "El dato introducido no es un entero")

    hora = get_usr_data("Inserte la hora a la que acude el invitado ( ej: 20:00:00): ", str, "Los datos introducidos no son validos")

    db.asignar_hora_invitado(dni, alfombra, hora)
    wait_for_user_input()


def permiso_periodista(db):
    """Tomamos los datos necesarios para dar permiso a un periodista y llamamos al metodo de la base de datos para que los introduzca"""

    # Mostramos los periodistas para que el usuario sepa cual elegir
    db.mostrar_periodistas()

    # Tomamos el dni del periodista
    dni_periodista = get_usr_data(
        "Inserte el dni del periodista: ", str, "Los datos introducidos no son validos")

    # Mostramos las actividades para que el usuario sepa cual elegir
    db.mostrar_ruedas_prensa()

    # Seleccionamos la actividad
    id_actividad = get_usr_data("Inserte el identificador de la actividad: ", int, "El identificador introducido no es valido")

    # Lanzamos la peticion a la bse de datos
    db.dar_permiso_periodista(dni_periodista, id_actividad)

    wait_for_user_input()
