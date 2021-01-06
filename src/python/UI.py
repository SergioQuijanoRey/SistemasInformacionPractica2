import DatabaseRepository
import os
import asistentes
import premios
import patrocinadores
import actividades
import utils

# MENU PRINCIPAL

def main_menu(db):
    """Menu principal que orquesta todas las operaciones del usuario"""
    print("\nBienvenido al mejor festival del mundo")
    print("~" * 80)

    while True:
        show_options()
        try:
            option = int(input("Elija una opcion: "))
        except:
            option = 6

        process_input(option,db)



def process_input(option,db):
    """Procesa la opcion del menu principal"""
    if option == 0:
        print('Saliendo...')
        exit()

    elif option == 1:
        menu_asistentes(db)

    elif option == 2:
        menu_actividades(db)

    elif option == 3:
        menu_premios(db)

    elif option == 4:
        menu_patrocinadores(db)

    else:
        os.system("clear")
        print('Opción no válida.')


def show_options():
    print("Las opciones disponibles son:")
    print("\t0: Salir del Sistema")
    print("\t1: Gestionar Asistentes")
    print("\t2: Gestionar Actividades")
    print("\t3: Gestionar Premios")
    print("\t4: Gestionar Patrocinadores")


# ASISTENTES

def show_asistentes():
    print("Las opciones disponibles son:")
    print("\t0: Volver al menu principal")
    print("\t1: Comprar entrada")
    print("\t2: Notificar estado Covid")
    print("\t3: Devolver entrada")
    print("\t4: Notificar asistencia actividad gratuita")

def menu_asistentes(db):
    """Menu que orquesta todas las operaciones de gestion de asistentes"""
    os.system("clear")
    bucle = True

    while bucle:
        show_asistentes()

        try:
            option = int(input("Elija una opcion: "))
        except:
            option = 6

        bucle = process_asistentes(option,db)



def process_asistentes(option,db):
    """Procesa la opcion del menu asistentes"""
    bucle = True

    if option == 0:
        bucle = False
        os.system("clear")
        print('Volviendo al menu principal...')

    elif option == 1:
        asistentes.comprar_entrada(db)
        os.system("clear")

    elif option == 2:
        asistentes.covid(db)
        os.system("clear")

    elif option == 3:
        asistentes.devolver_entrada(db)
        os.system("clear")

    elif option == 4:
        asistentes.actividad_gratuita(db)
        os.system("clear")

    else:
        os.system("clear")
        print('Opción no válida.')

    return bucle



# PREMIOS

def show_premios():
    print("Las opciones disponibles son:")
    print("\t0: Volver al menu principal")
    print("\t1: Votar")
    print("\t2: Planificar premio")
    print("\t3: Asignar nominado a premio")
    print("\t4: Fallar premio")


def menu_premios(db):
    """Menu que orquesta todas las operaciones de gestion de premios"""
    os.system("clear")
    bucle = True

    while bucle:
        show_premios()

        try:
            option = int(input("Elija una opcion: "))
        except:
            option = 6

        bucle = process_premios(option,db)



def process_premios(option,db):
    """Procesa la opcion del menu premios"""
    bucle = True

    if option == 0:
        bucle = False
        os.system("clear")
        print('Volviendo al menu principal...')

    elif option == 1:
        premios.votar(db)
        os.system("clear")

    elif option == 2:
        premios.planificar_premio(db)
        os.system("clear")

    elif option == 3:
        premios.asignar_nominado(db)
        os.system("clear")

    elif option == 4:
        premios.fallar_premio(db)
        os.system("clear")

    else:
        os.system("clear")
        print('Opción no válida.')

    return bucle


# ACTIVIDADES

def show_actividades():
    print("Las opciones disponibles son:")
    print("\t0: Volver al menu principal")
    print("\t1: Crear actividad")
    print("\t2: Asignar rueda de prensa a pelicula")
    print("\t3: Asignar hora invitado para alfombra roja")
    print("\t4: Dar permiso a periodista")

def menu_actividades(db):
    """Menu que orquesta todas las operaciones de gestion de actividades"""
    os.system("clear")
    bucle = True

    while bucle:
        show_actividades()

        try:
            option = int(input("Elija una opcion: "))
        except:
            option = 6

        bucle = process_actividades(option,db)



def process_actividades(option,db):
    """Procesa la opcion del menu actividades"""
    bucle = True

    if option == 0:
        bucle = False
        os.system("clear")
        print('Volviendo al menu principal...')

    elif option == 1:
        actividades.crear_actividad(db)
        os.system("clear")

    elif option == 2:
        actividades.rueda_pelicula(db)


    elif option == 3:
        actividades.hora_invitado(db)

    elif option == 4:
        actividades.permiso_periodista(db)
        os.system("clear")

    else:
        os.system("clear")
        print('Opción no válida.')

    return bucle





    # PATROCINADORES

def show_patrocinadores():
    print("Las opciones disponibles son:")
    print("\t0: Volver al menu principal")
    print("\t1: Dar de alta a patrocinador")
    print("\t2: Patrocinar actividad no economica")
    print("\t3: Subasta de patrocinio economico")
    print("\t4: Fijar patrocinador")

def menu_patrocinadores(db):
    """Menu que orquesta todas las operaciones de gestion de patrocinadores"""
    os.system("clear")
    bucle = True

    while bucle:
        show_patrocinadores()

        try:
            option = int(input("Elija una opcion: "))
        except:
            option = 6

        bucle = process_patrocinadores(option,db)



def process_patrocinadores(option,db):
    """Procesa la opcion del menu patrocinadores"""
    bucle = True

    if option == 0:
        bucle = False
        os.system("clear")
        print('Volviendo al menu principal...')

    elif option == 1:
        patrocinadores.alta_patrocinador(db)
        os.system("clear")

    elif option == 2:
        patrocinadores.no_economica(db)
        os.system("clear")

    elif option == 3:
        patrocinadores.subasta(db)
        os.system("clear")

    elif option == 4:
        patrocinadores.fijar(db)
        os.system("clear")

    else:
        os.system("clear")
        print('Opción no válida.')

    return bucle



# JUANJO

def input_actividad():
    #Por el auto_increment, no metemos el identificador
    descripcion = input("Inserte la descripcion de la actividad: ")
    while len(descripcion)<= 0 or len(descripcion) >3000:
        descripcion = input("Descripcion no valida, inserte otra: ")

    fecha = input('Inserte un fecha: ')
    #condicion = False
    #while condicion != True:
    #    try:
    #        utils.validate_date(fecha)
    #        condicion = True 
    #    except:
    #        print("Error, la fecha introducida no es correcta")
    #        fecha=input("inserte de nuevo la fecha")
    return descripcion, fecha

def input_asistente():
    nombre = input("Introduce el nombre del asistente:  ")
    while len(nombre)<= 0 or len(nombre) >300:
        nombre = input("Nombre no valido, insertelo de nuevo:  ")

    dni = input("Introduce el dni del asistente:   ")
    while len(dni)<=0 or len(dni)>9:
        dni = input("Dni incorrecto, insertelo de nuevo:   ")

    cuentaBancaria = input("introduce el numero de cuenta bancaria:   ")
    while len(cuentaBancaria)>400 or len(cuentaBancaria)<= 0:
        cuentaBancaria = input("Cuenta Bancaria no valida, inserte otra:   ")

    return nombre, dni, cuentaBancaria

def input_UsarEntrada():

    idEntrada = utils.get_int("Inserte el identificador de la entrada: ")
    while idEntrada < 0 :
        idEntrada = utils.get_int("Identificador no valido, insertelo de nuevo: ")

    idActividad = utils.get_int("Inserte el identificador de la actividad: ")
    while idActividad < 0:
        idActividad = utils.get_int("Identificador no valido, insertelo de nuevo: ")

    cantidad = utils.get_int("Introduzca la cantidad, por defecto es 1: ")
    while cantidad < 1:
        cantidad = utils.get_int("Cantidad no valida, introduzcala de nuevo: ")

    return idEntrada, idActividad, cantidad


def input_AbonaPagos():
    cantidad = utils.get_int("Introduzca el precio de la actividad:  ")
    while cantidad < 0:
        cantidad = utils.get_int("Meta el precio correctamente: ")
    
    return cantidad

def input__patrocinador():

    nombre = input("Inserte el nombre del patrocinador: ")

    while len(nombre) < 0 or len(nombre) > 200:
        nombre = input("Nombre no correcto, prueba otra vez: ")

    prevision=utils.get_usr_data(
        "Inserte prevision:  ",
        float,
        "El dato insertado no es de tipo float")

    while prevision < 0:
        prevision=utils.get_usr_data(
            "No puede haber una prevision negativa, inserte otra: ",
            float,
            "El dato insertado no es de tipo float")
    
    return nombre, prevision 

def input_candidato():

    dni = input("Introduzca el dni del candidato: ")
    while len(dni) < 0 or len(dni)>9:
        dni = input("dni incorrecto, introduzcalo correctamente: ")
    
    idcategoria = utils.get_int("Introduzca el identificador de la categoria: ")
    while idcategoria < 0:
        idcategoria = utils.get_int("Error, entero no puede ser negativo, introduzcalo de nuevo: ")

    return dni, idcategoria