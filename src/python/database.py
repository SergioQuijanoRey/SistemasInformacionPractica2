import sqlite3
import mariadb
import os

class DatabaseFactory:
    """Clase que se encarga de devolver los tipos de bases de datos que soportamos"""
    def get_database(database_type: str):
        if database_type == "SQLite":
            return SQLiteDatabase()
        elif database_type == "MariaDB":
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
        """El inicializador se conecta a la base de datos"""

        self.conn = None
        self.cursor = None

        self.connect()

    def connect(self):
        """Codigo que conecta con la base de datos"""
        raise Exception("DatabaseRepository es una interfaz que no puede ser instanciada")

    def try_execute(self, query: str, err_msg: str = "ERROR! ejecutando una peticion a la base de datos"):
        """
        Tries to execute a database query
        Shows error msg if it fails
        """

        # Las sentencias con SELECT deben retornar
        should_return = False
        if "SELECT" in query or "select" in query:
            should_return = True

        try:
            self.cursor.execute(query)

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

    def try_execute_sql_file(self, file_path: str):
        """
        Lee un archivo con un script en sql y lo ejecuta sentencia a sentencia
        """

        # Tomo los contenidos del fichero
        sqlContent = None
        with open(file_path, 'r') as file_obj:
            sqlContent = file_obj.read()

        # Obtengo las sentencias del fichero
        sqlSentences = sqlContent.split(";")
        sqlSentences = [sentence + ";" for sentence in sqlSentences]

        for sentence in sqlSentences:
            self.try_execute(sentence, f"ERROR! Ejecutando sentencia {sentence}")

    def rollback(self, savepoint: str):
        self.try_execute(f"ROLLBACK TO {savepoint};", f"ERROR haciendo el Rollback al savepoint {savepoint}")

    def savepoint(self, name: str):
        self.try_execute(f"SAVEPOINT {name};", f"Trying to set savepoint {name} failed")
        
    def commit(self):
        """Saves  the current changes to the database"""
        try:
            self.conn.commit()
        except Exception as err:
            print("Hubo un error commitenado los cambios")
            print(f"El codigo de error fue: {e}")
            print("Los cambios no se han guardado :(((")


class SQLiteDatabase(DatabaseRepository):
    def connect(self):
        try:
            conn = sqlite3.connect('example.db')
        except:
            print("ERROR conectando con la base de datos de testing")
            exit(-1)

        self.conn = conn
        self.cursor = self.conn.cursor()

class MariaDatabase(DatabaseRepository):

    def connect(self):
        try:
            # Datos de la base de datos
            server = '172.20.0.2'
            database = 'sergio'
            username = 'sergio'
            password = 'sergio'
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

        self.conn = conn
        self.cursor = self.conn.cursor()
