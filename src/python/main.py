import database

if __name__ == "__main__":

    # Tomamos el objeto tipo base de datos
    database_type = "SQLite"
    database = database.DatabaseFactory.get_database(database_type)

