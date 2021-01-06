import DatabaseRepository
import UI

def votar(db):
    db.mostrar_nominados()
    db.mostrar_jueces()
    dniJuez, idCategoria, dniNominado = UI.input_votacion()

    db.try_execute(
        f"INSERT INTO VotarNominado(DNIJuez, IdCategoria, DNINominado) VALUES (\"{dniJuez}\", {idCategoria},\"{dniNominado}\")"
    )

    db.commit()

def planificar_premio(db):
    pass

def asignar_nominado(db):

    db.mostrar_nominados()
    dni, idcategoria = UI.input_candidato()

    db.try_execute(
        f"INSERT INTO SerCandidato(DNINominado, IdCategoria) VALUES (\"{dni}\",{idcategoria})")

    db.commit()

def fallar_premio(db):
    pass
