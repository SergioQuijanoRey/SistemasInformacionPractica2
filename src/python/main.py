from DatabaseFactory import DatabaseFactory
import UI

if __name__ == "__main__":

    # Tomamos el objeto tipo base de datos
    print("Cargando base de datos")
    database_type = "MariaDB"
    db = DatabaseFactory.get_database(database_type)
    print("Base de datos cargada")

    # Lanzamos la aplicacion
    UI.main_menu(db)

    # Finaliza la aplicacion
    print("Aplicacion finalizada con exito")
