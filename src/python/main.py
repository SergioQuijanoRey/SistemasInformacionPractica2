import database
import UI

if __name__ == "__main__":

    # Tomamos el objeto tipo base de datos
    database_type = "MariaDB"
    db = database.DatabaseFactory.get_database(database_type)

    # Lanzamos la aplicacion
    UI.main_menu(db)

    # Finaliza la aplicacion
    print("Aplicacion finalizada con exito")
