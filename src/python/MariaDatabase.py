from DatabaseRepository import DatabaseRepository
import mariadb
import secrets

class MariaDatabase(DatabaseRepository):

    def connect(self):
        try:
            # Datos de la base de datos
            server = secrets.docker_ip
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

    def initialize_data(self):
        self.try_execute_sql_file("./src/sql/CreacionTablas.sql", ignore_error = True)

    def load_triggers(self):
        triggers = [
            "./src/sql/Triggers.sql"
        ]

        for trigger in triggers:
            self.try_execute_sql_file(trigger)
