def get_int(input_msg: str):
    value = None
    correcto = False

    while correcto == False:
        value = input(input_msg)
        try:
            value = int(value)
        except:
            print("El valor dado no es un entero valido")
            continue

        correcto = True

    return value
