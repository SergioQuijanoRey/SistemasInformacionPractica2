def get_int(input_msg: str):
    return get_usr_data(input_msg, int, "El dato introducido no es un entero")

def get_usr_data(input_msg: str, datatype_converter, err_msg: str = "El tipo de dato introducido no es correcto"):
    value = None
    correcto = False

    while correcto == False:
        value = input(input_msg)
        try:
            value = datatype_converter(value)
        except:
            print(err_msg)
            continue

        correcto = True

    return value

def validate_date(string_date: str):
    try:
        # MariaDB uses this format by default
        datetime.datetime.strptime(string_date, '%Y-%m-%d')
    except:
        raise ValueError("INCORRECT DATE TIME")

def wait_for_user_input():
    input("Pulse una tecla para CONTINUAR...")
