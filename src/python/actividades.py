import DatabaseRepository
import UI
from utils import get_usr_data

def crear_actividad(db):
    # TODO -- limpiar esta funcion
    # TODO -- devolver identificador de la actividad creada
    """Meter cuantas entradas quiere el usuario y hacer el insert """
    descripcion, fecha = UI.input_actividad()
    try:
        db.execute(
            f"INSERT INTO Actividad (Descripcion, Fecha) VALUES (\"{descripcion}\", \"{fecha}\")"
        )
    except Exception as e:
        print("No se pudo ")
        print(f"El error fue {e}")
        raise Exception("No se ha podido crear la actividad")

    IdActividad = db.actividad_mayor()

    cantidadEntradas = utils.get_int("Cuantas entradas desea que tenga la actividad: ")
    query = "INSERT INTO UsarEntradas(IdEntrada, IdActividad) VALUES "
    query += f"({0}, ({IdActividad}), "
    for i+1 in range cantidadEntradas:
        query += f",({i}, ({IdActividad})"
    query += ";"

    try:
        db.execute(query)
    except expression as e:
        print("Error, crear_actividad, no se pudo insertar las entradas")
        print(f"El error fue {e}")
        raise Exception("No se ha insertar las entradas,")

    db.commit()


def rueda_pelicula(db):
    save = "RUEDAPRENSA"
    db.savepoint(save)

    crear_actividad(db)
    ruedaPrensa = db.actividad_mayor()

    db.mostrar_peliculas()
    pelicula = get_usr_data("Inserte el identificador de la película: ",int, "El dato introducido no es un entero")

    nombre = get_usr_data("Inserta el nombre de la Rueda de Prensa: ", str)
    plazas = get_usr_data("Inserte el numero de plazas: ",int, "El dato introducido no es un entero")
    lugar = input("Inserte el lugar: ")

    db.asignar_rueda_pelicula(ruedaPrensa,  pelicula, nombre, plazas, lugar, save)



def hora_invitado(db):
    db.mostrar_invitados()
    dni = get_usr_data("Inserte el dni del Invitado: ", str, "Los datos introducidos no son validos" )

    db.mostrar_alfombras()
    alfombra = get_usr_data("Inserte el identificador de la alfombra roja: ",
                            int, "El dato introducido no es un entero")

    hora = get_usr_data("Inserte la hora a la que acude el invitado ( ej: 20:00:00): ", str, "Los datos introducidos no son validos")

    db.asignar_hora_invitado(dni, alfombra, hora)



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

    input("Pulsa una tecla para CONTINUAR...")
