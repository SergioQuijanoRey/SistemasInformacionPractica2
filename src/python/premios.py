import DatabaseRepository
import UI
from utils import get_usr_data

def votar(db):
    db.mostrar_nominados()
    db.mostrar_jueces()
    dniJuez, idCategoria, dniNominado = UI.input_votacion()

    db.try_execute(
        f"INSERT INTO VotarNominado(DNIJuez, IdCategoria, DNINominado) VALUES (\"{dniJuez}\", {idCategoria},\"{dniNominado}\")"
    )

    db.commit()

def planificar_premio(db):
    descrip = get_usr_data("Inserte la descripcion del premio: ", str, "Los datos introducidos no son validos" )
    presen = get_usr_data("Inserte el nombre de la persona que presenta el premio: ", str, "Los datos introducidos no son validos" )

    db.mostrar_galas()
    idgala = get_usr_data("Inserte el identificador de la gala donde sera presentado el premio: ",int, "El dato introducido no es un entero")

    db.presentado_categoria(descrip, presen, idgala)



def asignar_nominado(db):

    db.mostrar_nominados()
    dni, idcategoria = UI.input_candidato()

    db.try_execute(
        f"INSERT INTO SerCandidato(DNINominado, IdCategoria) VALUES (\"{dni}\",{idcategoria})")

    db.commit()

def fallar_premio(db):
    pass
