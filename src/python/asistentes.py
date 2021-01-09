import DatabaseRepository
import UI
from utils import *

def comprar_entrada(db):
    # Mostramos los asistentes y tomamos el dni 
    db.mostrar_asistentes()
    dni = get_usr_data("Introduzca el DNI del asistente: ", str, "El tipo de dato no es correcto")

    # Mostramos las actividades y tomamos el id
    db.mostrar_actividades()
    id_actividad = get_usr_data("Introduzca el id de la actividad: ", int, "El identificador dado no es valido")

    # Pedimos la cantidad de entradas que quiere el asistente
    cantidad = get_usr_data("Inserte la cantidad de entradas: ", int, "La cantidad introducido no es valida")

    db.savepoint("ComprarEntrada")

    id_entrada = None
    try:
        id_entrada = db.usar_entrada(id_actividad, dni, cantidad)
    except:
        print("Esta actividad no tiene entradas disponibles")
        print("Pruebe con otra actividad")
        wait_for_user_input()
        return

    cantidadPago = db.PRECIO_ENTRADA*float(cantidad)

    try:
        db.comprar_entrada(id_entrada, id_actividad,cantidadPago)
    except:
        print("No se ha podido tramitar el pago")
        db.rollback("ComprarEntrada")

    print("Compra realizada")
    wait_for_user_input()


def covid(db):
    """Se toman los datos para notificar el estado COVID, despues se llama al metodo de la base de datos"""

    # Mostramos los tipos de usuario
    print("Los tipos de persona que pueden notificar su estado son:")
    print("0: Invitados")
    print("1: Periodista")
    print("2: Asistentes")

    # Tomamos el tipo de usurio
    done = False
    usr_type = None
    while done == False:
        usr_type = get_usr_data("Introduzca el tipo de usuario: ", int, "El tipo de dato no es un entero valido")

        if usr_type != 0 and usr_type != 1 and usr_type != 2:
            print("Los unicos valores validos son 0, 1 y 2, vuelve a intentarlo")
            continue

        done = True

    # Mostramos los DNIS para que el usuario sepa cual seleccionar
    if usr_type == 0:
        db.mostrar_invitados()
    elif usr_type == 1:
        db.mostrar_periodistas()
    else:
        db.mostrar_asistentes()

    # El usario introduce los datos
    dni = get_usr_data("Introduzca el DNI deseado: ", str, "El tipo de dato no es correcto")

    # Lanzamos la peticion a la base de datos
    db.notificar_estado_covid(usr_type, dni)

    input("Pulsa una tecla para CONTINUAR...")

def devolver_entrada(db):
    """Se toman los datos necesarios para devolver la entrada"""

    # Preguntamos por el usuario
    db.mostrar_asistentes()

    # Pedimos que el usuario se identifique
    usr = input("Seleccione su usuario: ")

    # Mostramos las entradas que el usuario tiene disponibles
    try:
        db.mostrar_entradas_usuario_no_devueltas(usr)
    except Exception:
        print("Ese usuario no tiene entradas para devolver")
        input("Pulse una tecla para CONTINUAR...")
        return

    # Tomamos la entrada del usuario
    id_entrada = get_usr_data("Introduzca el id de la entrada a devolver: ", int, "El identificador dado no es valido")
    id_actividad = get_usr_data("Introduzca el id de la actividad de la anterior entrada: ", int, "El identificador dado no es valido")

    # Realizamos la devolucion de la entrada
    db.devolver_entrada(id_actividad, id_entrada)

    input("Pulse una tecla para CONTINUAR...")

def actividad_gratuita(db):
    # Mostramos las actividades para que el usuario elija una
    db.mostrar_actividades()
    id_actividad = get_usr_data("Inserte el identificador de la actividad: ", int, "El identificador introducido no es valido")

    # Mostramos los asistentes para que el usuario se identifique
    db.mostrar_asistentes()
    dni = get_usr_data("Inserte el dni del Asistente: ", str, "Los datos introducidos no son validos" )

    # Pedimos la cantidad de entradas que quiere el asistente
    cantidad = get_usr_data("Inserte la cantidad de entradas: ", int, "La cantidad introducido no es valida")

    # Usar la ultima entrada que este disponible
    # Si no hay entradas disponibles, notificarlo al usuario
    try:
        db.usar_entrada(id_actividad, dni, cantidad)
    except:
        print("Esta actividad no tiene entradas disponibles")
        print("Pruebe con otra actividad")
        wait_for_user_input()
        return

    print("Asignacion realizada")
    wait_for_user_input()
