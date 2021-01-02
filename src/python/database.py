import sqlite3
import mariadb
import os

class DatabaseFactory:
    """Clase que se encarga de devolver los tipos de bases de datos que soportamos"""
    def get_database(database_type: str) -> DatabaseRepository:
        if database_type == "SQLite":
            return SQLiteDatabase()
        elif database_type == "MariaDB"
            return MariaDatabase()
        else:
            print("ERROR! No hay una base de datos de ese tipo")
            print("Los tipos de base de datos disponibles son:")
            print("\tMariaDB")
            print("\tSQLite")

class DatabaseRepository:
    """
    Interfaz que declara las operaciones que puede realizarse con una base de datos
    Por tanto, no puede ser instanciada directamente, debe ser implementada
    """
    def __init__(self):
        raise Exception("DatabaseRepository es una interfaz, no puede ser instanciada")


# Database selector
database_selector = ["SQLite", "MariaDB"]
database_selector = database_selector[1]

if database_selector == "MariaDB":
    try:
        # Datos de la base de datos
        server = '172.17.0.2'
        database = 'base_datos_almacenamiento'
        username = 'sergio'
        password = 'sergioquijano'
        port = 3306

        conn = mariadb.connect(
            user=username,
            password=password,
            host=server,
            port=port,
            database=database
        )

    except Exception as err:
        print("ERROR conectando con la base de datos de MariaDB")
        print(f"El error fue {err}")
        exit(-1)

elif database_selector == "SQLite":
    print("WARNING! Using testing database")
    try:
        conn = sqlite3.connect('example2.db')
    except:
        print("ERROR conectando con la base de datos de testing")
        exit(-1)
else:
    print(
        f"ERROR, el selector de base de datos '{database_selector}' no es un selector valido")
    exit(-1)

# En todas las bases de datos podemos tomar el cursor de la misma forma
cursor = conn.cursor()

def try_execute(query: str, err_msg: str = "ERROR! ejecutando una peticion a la base de datos", should_return : bool = False):
    """Tries to execute a database query
    Shows error msg if it fails
    """

    try:
        cursor.execute(query)

        if should_return == False:
            return "OK"

        # We have results to return
        result = []
        for row in cursor:
            result.append(row)

        # Safety check
        if result == []:
            raise Exception("No results when should_return is indicated as True")

        return result

    except Exception as err:
        print(err_msg)
        print(f"El codigo del error fue: {err}")
