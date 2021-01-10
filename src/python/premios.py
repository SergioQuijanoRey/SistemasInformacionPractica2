import DatabaseRepository
import UI
from utils import *

def votar(db):
    # Mostramos los jueces para que el usuario se identifique como juez
    db.mostrar_jueces()
    id_juez = get_usr_data("Introduzca el DNI del juez: ", str, "DNI no valido")

    # Mostramos las categorias en las que participa el juez para seleccionar en cual votamos
    db.mostrar_categorias_de_juez(id_juez)
    id_categoria = get_usr_data("Introduzca el identificador de la categoria: ", int, "Identificador de la categoria no valido")

    # Mostramos los nominados de la categoria para realizar la votacion
    db.mostrar_nominados_de_categoria(id_categoria)
    id_nominado = get_usr_data("Introduzca el DNI del nominado: ", str, "DNI no valido")

    # Insertamos el voto en la base de datos
    try:
        db.votar(id_juez, id_categoria, id_nominado)
        db.commit()
    except Exception as e:
        print("No se pudo realizar la votacion")
        print(f"El error fue: {e}")
        wait_for_user_input()
        return

    print("Votacion realizada con exito")
    wait_for_user_input()

def planificar_premio(db):
    descrip = get_usr_data("Inserte la descripcion del premio: ", str, "Los datos introducidos no son validos" )
    presen = get_usr_data("Inserte el nombre de la persona que presenta el premio: ", str, "Los datos introducidos no son validos" )

    db.mostrar_galas()
    idgala = get_usr_data("Inserte el identificador de la gala donde sera presentado el premio: ",int, "El dato introducido no es un entero")

    db.presentado_categoria(descrip, presen, idgala)
    wait_for_user_input()


def asignar_nominado(db):

    # El usuario introduce el DNI del candidato
    db.mostrar_nominados()
    dni = get_usr_data("Introduzca el dni del candidato: ", str, "Dato introducido no valido")

    # El usuario introduce la categoria en la que quiere meter al candidato
    db.mostrar_categorias()
    idcategoria = get_usr_data("Introduzca el identificador de la categoria: ", int, "El identificador no es valido")

    # Insertamos los datos en la base de datos
    db.asignar_nominado_a_categoria(idcategoria, dni)
    wait_for_user_input()

def fallar_premio(db):

    db.mostrar_categorias_fallables()
    categoria = get_usr_data("Inserte el identificador de la categoria que desea fijar: ",int, "El dato introducido no es un entero")

    db.fallar_premio(categoria)
    wait_for_user_input()
