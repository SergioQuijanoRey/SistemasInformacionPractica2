import DatabaseRepository
import UI

def alta_patrocinador(db):
    nombre, prevision = UI.input__patrocinador()
    db.try_execute(
        f"INSERT INTO Patrocinador (Nombre, Prevision) VALUES (\"{nombre}\",{prevision})"
    )
    db.commit()

def no_economica(db):
    pass

def subasta(db):
    pass

def fijar(db):
    pass
