import sqlite3
import mariadb
import secrets
import os


class DatabaseRepository:
    """
    Interfaz que declara las operaciones que puede realizarse con una base de datos
    Por tanto, no puede ser instanciada directamente, debe ser implementada
    """

    def __init__(self):
        """El inicializador se conecta a la base de datos"""

        self.conn = None
        self.cursor = None

        # Nos conectamos a la base de datos
        self.connect()

        # Inicializamos la base de datos
        self.initialize_data()

        # Cargamos los triggers
        self.load_triggers()

    def connect(self):
        """Codigo que conecta con la base de datos"""
        raise Exception(
            "DatabaseRepository es una interfaz que no puede ser instanciada")

    def initialize_data(self):
        """Carga los datos iniciales en la base de datos a traves de ficheros sql"""
        raise Exception(
            "DatabaseRepository es una interfaz que no puede ser instanciada")

    def execute(self, query: str):
        """
        Lanza una peticion a la base de datos
        Si la base de datos lanza una excepcion, es responsabilidad del invocante manejar las excepciones
        """

        # Las sentencias con SELECT deben retornar
        should_return = False
        if "SELECT" in query or "select" in query:
            should_return = True

        self.cursor.execute(query)

        if should_return == False:
            return "OK"

        # We have results to return
        result = []
        for row in self.cursor:
            result.append(row)

        # Safety check
        if result == []:
            raise Exception(
                "No results when should_return is indicated as True")

        return result

    def try_execute(self, query: str, err_msg: str = "ERROR! ejecutando una peticion a la base de datos", ignore_error: bool = False):
        """
        Intenta ejecutar una sentencia
        Si la base de datos lanza una excepcion, la funcion la captura y muestra el mensaje de error
        """

        # Las sentencias con SELECT deben retornar
        should_return = False
        if "SELECT" in query or "select" in query:
            should_return = True

        try:
            results = self.execute(query)

            if should_return == False:
                return "OK"

            return results

        except Exception as err:
            if ignore_error == False:
                print(err_msg)
                print(f"El codigo del error fue: {err}")

    def try_execute_sql_file(self, file_path: str, ignore_error: bool = False):
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
            self.try_execute(
                sentence, f"ERROR! Ejecutando sentencia {sentence}", ignore_error=ignore_error)

    def rollback(self, savepoint: str):
        self.try_execute(
            f"ROLLBACK TO {savepoint};", f"ERROR haciendo el Rollback al savepoint {savepoint}")

    def savepoint(self, name: str):
        self.try_execute(f"SAVEPOINT {name};",
                         f"Trying to set savepoint {name} failed")

    def commit(self):
        """Saves  the current changes to the database"""
        try:
            self.conn.commit()
        except Exception as err:
            print("Hubo un error commitenado los cambios")
            print(f"El codigo de error fue: {e}")
            print("Los cambios no se han guardado :(((")

    def load_triggers(self):
        """Carga los triggers de la base de datos, a partir de una serie de ficheros"""
        raise Exception(
            "DatabaseRepository es una interfaz que no puede ser instanciada")

    def dar_permiso_periodista(self, dni_periodista: str, id_rueda_prensa: int):
        """Da permiso de acceso a un periodista a una rueda de prensa"""
        try:
            self.execute(f"INSERT INTO Acceder(DNIPeriodista, IdRuedaPrensa) VALUES ('{dni_periodista}', {id_rueda_prensa});")
            self.commit()
            print("Permisos asignados con exito")

        except Exception as e:
            print("No ha sido posible dar permisos al periodista")
            print(f"El codigo de error fue {e}")
            print("Vuelvelo a intentar desde el menu principal")

    def notificar_estado_covid(self, usr_type: int, dni: str):
        """Notificamos el estado de COVID de un tipo de usuario """
        # TODO -- hacer como un trigger de Mariadb

        # Condicion de seguridad
        if usr_type != 0 and usr_type != 1 and usr_type != 2:
            print("ERROR en DatabaseRepository.notificar_estado_covid()")
            print("El usr_type no tiene un valor valido")
            return

        # Usuario Invitado
        if usr_type == 0:
            try:
                self.execute(f"UPDATE Invitados SET covid = TRUE WHERE DNIInvitado = '{dni}'")
                self.commit()
            except Exception as e:
                print("No se pudo notificar el estado covid del invitado")
                print(f"El error fue {e}")

        # Usuario Periodista
        elif usr_type == 1:
            try:
                self.execute(f"UPDATE Periodista SET covid = TRUE WHERE DNIPeriodista = '{dni}'")
                self.commit()
            except Exception as e:
                print("No se pudo notificar el estado covid del periodista")
                print(f"El error fue {e}")

        # Usuario Asistente
        else:
            try:
                self.execute(f"UPDATE Asistentes SET Covid = TRUE WHERE DNIAsistente = '{dni}'")
                self.commit()
            except Exception as e:
                print("No se pudo notificar el estado covid del asistente")
                print(f"El error fue {e}")



    def mostrar_periodistas(self):
        """Mostramos los usuarios tipo Periodistas almacenados en la base de datos"""
        print("Los periodistas de la base de datos son:")
        results = self.try_execute("SELECT * FROM Periodista")
        for result in results:
            dni = result[0]
            name = result[1]
            print(f"{name} con DNI {dni}")

    def mostrar_ruedas_prensa(self):
        """Mostramos las ruedas de prensa almacenadas en la base de datos"""
        print("Las ruedas de prensa de la base de datos son: ")
        results = self.try_execute("SELECT IdRuedaPrensa, nombre FROM RuedaDePrensaAsigna")

        for result in results:
            identificador = result[0]
            nombre = result[1]
            print(f"Rueda de prensa {nombre} con identificador {identificador}")

    def mostrar_invitados(self):
        """Mostramos los usuarios tipo Invitado de la base de datos"""
        print("Los invitados de la base de datos son:")

        results = self.try_execute("SELECT DNIInvitado, Nombre FROM Invitados;")
        for result in results:
            dni = result[0]
            nombre = result[1]
            print(f"Invitado {nombre} tiene DNI {dni}")

    def mostrar_asistentes(self):
        """Mostramos los usuarios tipo Asistente de la base de datos"""
        print("Los asistentes de la base de datos son:")

        results = self.try_execute("SELECT DNIAsistente, Nombre FROM Asistentes;")
        for result in results:
            dni = result[0]
            nombre = result[1]
            print(f"Asistente {nombre} tiene DNI {dni}")

    def mostrar_alfombras(self):
        """Mostramos las alfombras rojas almacenadas en la base de datos"""
        print("Las alfombras rojas de la base de datos son: ")
        results = self.try_execute("SELECT idAlfombraRoja, horaInicio, horaFin  FROM AlfombraRoja;")

        for result in results:
            identificador = result[0]
            inicio = result[1]
            fin = result[2]
            print(f"Alfombra roja con identificador {identificador}, hora de inicio: {inicio} y hora de fin: {fin}")


    def mostrar_peliculas(self):
        """Mostramos las alfombras rojas almacenadas en la base de datos"""
        print("Las peliculas de la base de datos son: ")
        results = self.try_execute("SELECT idPelicula, Nombre FROM Pelicula;")

        for result in results:
            identificador = result[0]
            nombre = result[1]
            print(f"Pelicula \"{nombre}\" con identificador {identificador}")

    def actividad_mayor(self):
        result = self.try_execute("SELECT MAX(idActividad) FROM Actividad;")
        try:
            max = int(result[0][0])
        except:
            print("Error al convertir idActividad maximo a entero")
            max = 0

        return max

    def asignar_hora_invitado(self, dni: str, idAlfombra: int, hora: str):
        """Asignamos una hora para un invitado en la alfombra roja"""
        try:
            self.execute(f"INSERT INTO Acudir(DNIInvitado, idAlfombraRoja, hora) VALUES (\"{dni}\", {idAlfombra}, \"{hora}\");")
            self.commit()

        except Exception as e:
            print("No se pudo asignar la hora al invitado")
            print(f"El error fue {e}")
            
    def asignar_rueda_pelicula(self, ruedaPrensa: int, pelicula: int, nombre: str, plazas: int, lugar: str):
        try:
            self.execute(f"INSERT INTO RuedaDePrensaAsigna(IdRuedaPrensa, idPelicula, nombre, plazas, lugar) VALUES ({ruedaPrensa}, {pelicula}, \"{nombre}\", {plazas}, \"{lugar}\");")
            self.commit()

        except Exception as e:
            print("No se pudo asignar la hora al invitado")
            print(f"El error fue {e}")
