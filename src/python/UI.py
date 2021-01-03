import database

def main_menu(db):
    """Menu principal que orquesta todas las operaciones del usuario"""
    print("Este es el menu principal")
    print("Hay que hacer cosas con el parametro db")

def menu_actividad():
    idActividad = input('Inserte el identificador de Actividad:')
    while type(idActividad) != int:
        idActividad = input('Identificador no válido, inserte otro de nuevo:')

    descripcion = input("Inserte la descripcion de la actividad: ")
    while len(descripcion)<= 0 or len(descripcion) >300 or type(descripcion) != str:
        descripcion = input("Descripcion no valida, inserte otra:")

    fecha = input('Inserte un fecha')
    #Como gestiono la correcta introducción de una fecha?
    return idActividad, descripcion, fecha

def menu_asistente():
    nombre = input("Introduce el nombre del asistente")
    while type(nombre) != str or len(nomrbe)<= 0 or len(nombre) >300
        nombre = input("Nombre no valido, insertelo de nuevo:")

    dni = input("Introduce el dni del asistente")
    while type(dni) != str or len(dni)<=0 or len(dni)>9
        dni = input("Dni incorrecto, insertelo de nuevo:")
    
    cuentaBancaria = input("introduce el numero de cuenta bancaria")
    while type(cuentaBancaria) != str or len(cuentaBancaria)>400 or len(cuentaBancaria)<= 0
        cuentaBancaria = input("Cuenta Bancaria no valida, inserte otra")
    
    return nombre, dni, cuentaBancaria

def menu_UsarEntrada():

    idEntrada = input("Inserte el identificador de la entrada")
    while type(idEntrada) != int
        input("Identificador no valido, insertelo de nuevo:")

    idActividad = input("Inserte el identificador de la actividad")
    while type(idActividad) != int
        input("Identificador no valido, insertelo de nuevo:")
    
    return idEntrada, idActividad

def menu_AbonaPagos():
    idPago = input("Introduce el identificador del pago")
    while type(idPago) != int 
        idPago =input("Identificador erroneo, insertelo de nuevo")
    
    cantidad = input("Introduce la cantidad del pago")
    while type(cantidad) != float 
        cantidad =input("cantidad erronea, insertela de nuevo")

    idEntrada = input("Introduce el identificador de la entada")
    while type(idEntrada) != int 
        idEntrada =input("Identificador erroneo, insertelo de nuevo")

    idActividad = input("Introduce el identificador de la Actividad")
    while type(idActividad) != int 
        idActividad =input("Identificador erroneo, insertelo de nuevo")

    return idPago, cantidad, idEntrada, idActividad
