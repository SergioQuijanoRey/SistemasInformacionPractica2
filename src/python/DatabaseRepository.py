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

        # Cargamos los procedimientos
        self.load_procedures()

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
        sqlSentences = [sentence for sentence in sqlSentences if sentence != "\n"]
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

    def load_procedures(self):
        """Cargan los procedimientos a la base de datos"""
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

    def mostrar_actividades(self):
        """Mostramos las actividades almacenadas en la base de datos"""
        print("Las actividades de la base de datos son: ")
        results = self.try_execute("SELECT idActividad, Descripcion, fecha FROM Actividad;")

        for result in results:
            identificador = result[0]
            descrp = result[1]
            fecha = result[2]
            print(f"idActividad: {identificador}, Descripcion: {descrp}, Fecha: {fecha}")

    def mostrar_nominados(self):
        """Mostramos los Nominados almacenados en la base de datos"""
        print("Los Nominados de la Base de Datos son: ")
        results = self.try_execute("SELECT * FROM Nominados;")

        for result in results:
            dni = result[0]
            nombre = result[1]
            print(f"DNI: {dni}, Nombre: {nombre} ")

    def mostrar_jueces(self):
        """Mostramos los Jueces almacenados en la base de datos"""
        print("Los Jueces de la Base de Datos son: ")
        results = self.try_execute("SELECT * FROM Jueces;")

        for result in results:
            dni = result[0]
            nombre = result[1]
            print(f"DNI: {dni}, Nombre: {nombre} ")

    def mostrar_galas(self):
        """Mostramos las galas almacenadas en la base de datos"""
        print("Las Galas de la Base de Datos son: ")
        results = self.try_execute("SELECT idGala FROM Gala;")

        for result in results:
            idgala = result[0]
            print(f"Gala con identificador: {idgala}")

    def mostrar_entradas_usuario_no_devueltas(self, usr: str):
        """
        Muestra las entradas de un usuario, que no hayan sido ya devueltas
        """

        query = """
            SELECT IdEntrada
            FROM UsarEntradas
            WHERE DNIAsistentes = '{usr}' AND Devolucion = FALSE;""".format(usr = usr)

        results = None
        try:
            results = self.execute(query)
        except Exception as e:
            print("No se pudieron mostrar las entradas de este usuario")
            print(f"El codigo de error fue {e}")
            raise Exception("Usuario sin entradas")

        # Mostramos las entradas
        print(f"Las entradas que {usr} puede devolver son:")
        for result in results:
            id_entrada = result[0]
            print(f"Entrada {id_entrada}")

    def mostrar_patrocinadores(self):
        """Mostramos los patrocinadores almacenados en la base de datos"""
        print("Los Patrocinadores de la Base de Datos son: ")
        results = self.try_execute("SELECT IdPatrocinador, Nombre FROM Patrocinador;")

        for result in results:
            idpatro = result[0]
            nombre = result[1]
            print(f"Patrocinador \"{nombre}\" con identificador {idpatro}")

    def mostrar_entradadas_para_actividad(self, IdActividad: str):
        """Mostramos los identificadores de la entradas para la actividad dada como argumento"""
        print("Las entradas de la Base de datos para la Actividad son:")
        query = f"""
            SELECT IdEntrada FROM UsarEntradas
            WHERE IdActividad = \"{IdActividad}\"
        """

        try:
            self.execute(query)
        except:
            except Exception as e:
            print("No se realizar la consulta")
            print(f"El error fue {e}")
        


    def mostrar_subastadas_no_asignadas(self):
        """
        Muestra las actividades subastadas que no han sido ya asignadas
        Lanzamos una excepcion para que el menu pueda actuar acuerdo a la situacion
        """

        query = """
            SELECT IdActividadSubastada, Nombre FROM ActividadSubastada
            WHERE IdActividadSubastada NOT IN (
                SELECT IdActividadAsignada FROM ActividadAsignada
            );
        """
        results = None
        try:
            results = self.execute(query)
        except Exception as e:
            print("No se pudo encontrar actividades subastadas que no hayan sido ya asignadas")
            print(f"El error fue {e}")
            raise Exception("No se encontraron resultados")

        for result in results:
            id_actividad = result[0]
            nombre = result[1]
            print(f"Actividad {nombre} identificada por {id_actividad}")

    def mostrar_mejor_patrocinador(self, id_actividad_subastada: int):
        """Mostramos el mejor patrocinador para una actividad subastada"""

        query = """
            SELECT IdPatrocinador, Valor
            FROM Puja
            WHERE Valor IN (
                SELECT MIN(Valor)
                FROM Puja
                WHERE IdActividad = {id_actividad_subastada}
            );
        """.format(id_actividad_subastada = id_actividad_subastada)

        patrocinador_escogido = "Desconocido"
        patrocinador_escogido = self.try_execute(query, "No se pudo escoger al mejor patrocinador")
        valor_puja, patrocinador_escogido = patrocinador_escogido[0][1], patrocinador_escogido[0][0]
        print(f"El patrocinador escogido es: {patrocinador_escogido} con un valor de {valor_puja}")

    def actividad_mayor(self):
        results = self.try_execute("SELECT MAX(idActividad) FROM Actividad;")
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

    def asignar_rueda_pelicula(self, ruedaPrensa: int, pelicula: int, nombre: str, plazas: int, lugar: str, save:str):
        try:
            self.execute(f"INSERT INTO RuedaDePrensaAsigna(IdRuedaPrensa, idPelicula, nombre, plazas, lugar) VALUES ({ruedaPrensa}, {pelicula}, \"{nombre}\", {plazas}, \"{lugar}\");")
            self.commit()

        except Exception as e:
            print("No se pudo asignar la rueda de prensa a la pelicula")
            print(f"El error fue {e}")
            db.rollback(save)

    def usar_entrada(self, idActividad, dni, entrada):
        try:
            self.execute(f"INSERT INTO UsarEntradas(IdEntrada, IdActividad, DNIAsistentes) VALUES ({entrada}, {idActividad}, \"{dni}\");")
            self.commit()

        except Exception as e:
            print("No se pudo asignar la entrada al asistente")
            print(f"El error fue {e}")

    def presentado_categoria(self, descrip: str, presen: str, idgala: int):
        try:
            self.execute(f"INSERT INTO PresentadoCategoria(Descripcion, Presentador, idGala) VALUES (\"{descrip}\", \"{presen}\", {idgala});")
            self.commit()

        except Exception as e:
            print("No se pudo planificar la categoria")
            print(f"El error fue {e}")

    def oferta_no_economica(self, idactividad: int, idpatro: int, coste: float, descrip: str, save: str):
        try:
            self.execute(f"INSERT INTO OfertaActividadNoEconomica(IdActividadNoEconomica, IdPatrocinador, Coste, DescripcionRetribucion) VALUES ({idactividad}, {idpatro}, {coste}, \"{descrip}\");")
            self.commit()

        except Exception as e:
            print("No se pudo planificar la categoria")
            print(f"El error fue {e}")
            db.rollback(save)


    def devolver_entrada(self, id_entrada: int):
        """
        Se devuelve una entrada
        Para ello se marca como devuelta, para no perder datos de pagos
        """

        query = """
            UPDATE UsarEntradas
            SET Devolucion = TRUE
            WHERE IdEntrada = '{id_entrada}'
        """.format(id_entrada = id_entrada)

        self.try_execute(query)


    def fallar_premio(self, idcategoria: int):
        """Se falla la categoria indicada como parametro"""
        try:
            results = self.execute(f"SELECT DNINominado, COUNT(DNINominado) votos FROM VotarNominado  WHERE IdCategoria={idcategoria} GROUP BY DNINominado;")
        except Exception as e:
            print("No se pudo fijar la categoria correctamente")
            print(f"El error fue {e}")

        print("Los resultados de la votacion son:")
        for result in results:
            dni = result[0]
            votos = result[1]
            print(f"Nominado: {dni}   Votos: {votos}")

        print("")


    def fijar_patrocinador(self, id_actividad_subastada: int):
        # Marcamos la actividad como asignada
        self.try_execute(f"INSERT INTO ActividadAsignada VALUES ({id_actividad_subastada})", f"No se pudo marcar la actividad {id_actividad_subastada} como asignada")

        # Mostramos el patrocinador
        self.mostrar_mejor_patrocinador(id_actividad_subastada)

    def comprar_entrada(self, IdEntrada: str, IdActividad: str, DNIAsistentes: str, Cantidad: int, cantidadPago:float):

        self.try_execute(
            f"INSERT INTO UsarEntradas(IdEntrada, IdActividad, DNIAsistentes, Cantidad) VALUES ({IdEntrada}, {IdActividad}, \"{DNIAsistentes}\", {Cantidad})" )#La devolucion se gestiona en el disparador

        self.try_execute(
            f"INSERT INTO AbonaPagos(cantidadPago, IdEntrada, IdActividad) VALUES ({cantidadPago},{IdEntrada}, {IdActividad})")
        
        self.commit()

    def crear_actividad(self, descripcion: str, fecha:str):
        try:
            db.execute(
                f"INSERT INTO Actividad (Descripcion, Fecha) VALUES (\"{descripcion}\", \"{fecha}\")"
            )
        except Exception as e:
            print("No se pudo ")
            print(f"El error fue {e}")
            raise Exception("No se ha podido crear la actividad")

        self.commit()

    def insertar_entradas_para_actividad(IdActividad: str):

        query = "INSERT INTO UsarEntradas(IdEntrada, IdActividad) VALUES "
        query + = f"({0}, ({IdActividad}), "

        for i+1 in range cantidadEntradas:
            query + = f",({i}, ({IdActividad})"
        query + = ";"

        try:
            db.execute(query)
        except expression as e:
            print("Error, crear_actividad, no se pudo insertar las entradas")
            print(f"El error fue {e}")
            raise Exception("No se ha insertar las entradas,")

        self.commit()
        