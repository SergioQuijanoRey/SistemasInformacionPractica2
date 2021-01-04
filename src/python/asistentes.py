import DatabaseRepository
import UI

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
    pass

def devolver_entrada(db):
    pass

def actividad_gratuita(db):
    pass
