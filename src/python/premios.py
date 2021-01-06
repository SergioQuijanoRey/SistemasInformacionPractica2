import DatabaseRepository
import UI

def votar(db):
    pass

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
