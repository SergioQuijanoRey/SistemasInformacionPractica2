from DatabaseRepository import DatabaseRepository
from MariaDatabase import MariaDatabase
from SQLiteDatabase import SQLiteDatabase

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
