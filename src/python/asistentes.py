import DatabaseRepository
import UI
from utils import get_usr_data

def comprar_entrada(db):
    #Tomamos los datos
    nombre, dni, cuentaBancaria = UI.input_asistente()
    idEntrada, idActividad, dniAsistente, cantidadEntradas = UI.input_UsarEntrada()
    idPago, cantidadPago, idEntrada2, idActividad2 = UI.input_AbonaPagos()

    #Garantizamos consistencia
    while idEntrada2 != idEntrada or idActividad != idActividad2:
        print("Error en la introduccion de la tupla AbonaPagos, inserte de nuevo")
        idPago, cantidad, idEntrada2, idActividad2 = UI.input_AbonaPagos()

    #Insercción garantizando la transacción
    db.savepoint("ComprarEntrada")

    db.try_execute(
        f"INSERT INTO UsarEntradas VALUES ({IdEntrada}, {idActividad}, {dniAsistente}, {cantidadEntradas})" )#La devolucion se gestiona en el disparador

    db.try_execute(
        f"INSERT INTO AbonaPagos VALUES ({idPago},{cantidadPago},{idEntrada}, {idActividad})")

    db.rollback("ComprarEntrada")

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
    pass

def actividad_gratuita(db):
    pass
