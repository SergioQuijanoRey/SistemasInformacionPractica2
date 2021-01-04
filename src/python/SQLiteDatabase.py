from DatabaseRepository import DatabaseRepository
import sqlite3

class SQLiteDatabase(DatabaseRepository):
    def connect(self):
        try:
            conn = sqlite3.connect('example.db')
        except:
            print("ERROR conectando con la base de datos de testing")
            exit(-1)

        self.conn = conn
        self.cursor = self.conn.cursor()

    def initialize_data(self):
        self.try_execute_sql_file("./src/sql/CreacionTablas.sql")

    def load_triggers(self):
        triggers = [
            "./src/sql/Triggers.sql"
        ]

        for trigger in triggers:
            self.try_execute_sql_file(trigger)


