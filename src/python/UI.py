

def crear_actividad():
    idActividad = input('Inserte el identificador de Actividad:')
    while type(idActividad) != int:
        idActividad = input('Identificador no válido, inserte otro de nuevo:')
    
    descripcion = input("Inserte la descripcion de la actividad: ")
    while len(descripcion)<= 0 or len(descripcion) >300 or type(descripcion) != str:
        descripcion = input("Descripcion no valida, inserte otra:")

    fecha = input('Inserte un fecha')
    #Como gestiono la correcta introducción de una fecha?
    return idActividad, descripcion, fecha