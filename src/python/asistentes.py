import DatabaseRepository
import UI
from utils import get_usr_data

def comprar_entrada(db):
    #Tomamos los datos
    nombre, dni, cuentaBancaria = UI.input_asistente()
    idEntrada, idActividad, cantidadEntradas = UI.input_UsarEntrada()
    cantidadPago = UI.input_AbonaPagos()

    #db.savepoint("ComprarEntrada")

    db.try_execute(
        f"INSERT INTO Asistentes(DNIAsistente, Nombre, CuentaBancaria) VALUES (\"{dni}\",\"{nombre}\",\"{cuentaBancaria}\")"
    )

    db.try_execute(
        f"INSERT INTO UsarEntradas(IdEntrada, IdActividad, DNIAsistentes, Cantidad) VALUES ({idEntrada}, {idActividad}, \"{dni}\", {cantidadEntradas})" )#La devolucion se gestiona en el disparador

    db.try_execute(
        f"INSERT INTO AbonaPagos(Cantidad, IdEntrada, IdActividad) VALUES ({cantidadPago},{idEntrada}, {idActividad})")

    #db.rollback("ComprarEntrada")

    #Hacer efectivos los cambios
    db.commit()

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
    db.mostrar_actividades()

    id_actividad = get_usr_data("Inserte el identificador de la actividad: ", int, "El identificador introducido no es valido")

    db.mostrar_asistentes()

    dni = get_usr_data("Inserte el dni del Asistente: ", str, "Los datos introducidos no son validos" )

    entrada = get_usr_data("Inserte el numero de entrada: ", int, "El identificador introducido no es valido")

    db.usar_entrada(id_actividad, dni, entrada)
