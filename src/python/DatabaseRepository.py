import sqlite3
import mariadb
import secrets
import os


class DatabaseRepository:
    """
    Interfaz que declara las operaciones que puede realizarse con una base de datos
    Por tanto, no puede ser instanciada directamente, debe ser implementada
    """
    PRECIO_ENTRADA = 15.50

    def __init__(self):
        """El inicializador se conecta a la base de datos"""

        self.conn = None
        self.cursor = None
        self.temporal = False   # Para evitar hacer commits y poder hacer rollback

        # Nos conectamos a la base de datos
        self.connect()

        # Inicializamos la base de datos
        self.initialize_data()

    def __del__(self):
        self.commit()

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

        # Para hacer operaciones temporales
        if self.temporal is True:
            return

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

    def mostrar_categorias(self):
        """Mostramos los Nominados almacenados en la base de datos"""
        print("Los Nominados de la Base de Datos son: ")
        results = self.try_execute("SELECT idCategoria, Descripcion FROM PresentadoCategoria;")

        for result in results:
            categoria = result[0]
            descrip = result[1]
            print(f"Categoria '{descrip}' con identificador {categoria} ")

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
            SELECT IdEntrada, IdActividad
            FROM UsarEntradas
            WHERE DNIAsistentes = '{usr}' AND Devolucion = FALSE;""".format(usr = usr)

        results = None
        try:
            results = self.execute(query)
        except Exception as e:
            print("No se pudieron mostrar las entradas de este usuario")
            print(f"El codigo de error fue {e}")
            raise Exception("Usuario sin entradas")

        if len(results) == 0:
            raise Exception("Usuario sin entradas")

        # Mostramos las entradas
        print(f"Las entradas que {usr} puede devolver son:")
        for result in results:
            id_entrada = result[0]
            id_actividad = result[1]
            print(f"Entrada {id_entrada} de la actividad {id_actividad}")

    def mostrar_patrocinadores(self):
        """Mostramos los patrocinadores almacenados en la base de datos"""
        print("Los Patrocinadores de la Base de Datos son: ")
        results = self.try_execute("SELECT IdPatrocinador, Nombre FROM Patrocinador;")

        for result in results:
            idpatro = result[0]
            nombre = result[1]
            print(f"Patrocinador \"{nombre}\" con identificador {idpatro}")


    def mostrar_subastadas(self):
        """Mostramos los patrocinadores almacenados en la base de datos"""
        print("Las actividades subastadas son:")
        query = f"""
            SELECT IdActividadSubastada, Nombre FROM ActividadSubastada;
        """
        results = None
        try:
            results = self.execute(query)
        except Exception as e:
            print("No se encontraron los resultados")
            print(f"El error fue {e}")
            raise Exception ("No se encontraron los resultados")

        for result in results:
            id_actividad = result[0]
            nombre = result[1]
            print(f"Actividad {nombre} identificada por {id_actividad}")

    def mostrar_subastadas_no_asignadas(self):
        """
        Muestra las actividades subastadas que no han sido ya asignadas
        Lanzamos una excepcion para que el menu pueda actuar acuerdo a la situacion
        """

        query = """
            SELECT DISTINCT IdActividad FROM Puja
            WHERE IdActividad NOT IN (
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
            print(f"Actividad {id_actividad} esta disponible para fijarse")

    def mostrar_mejor_patrocinador(self, id_actividad_subastada: int):
        """Mostramos el mejor patrocinador para una actividad subastada"""

        query = """
            SELECT IdPatrocinador, Valor
            FROM Puja
            WHERE Valor IN (
                SELECT MAX(Valor)
                FROM Puja
                WHERE IdActividad = {id_actividad_subastada}
            );
        """.format(id_actividad_subastada = id_actividad_subastada)

        patrocinador_escogido = "Desconocido"

        try:
            patrocinador_escogido = self.execute(query)
            valor_puja, patrocinador_escogido = patrocinador_escogido[0][1], patrocinador_escogido[0][0]
        except Exception as e:
            print("No se pudo tomar al mejor patrocinador")
            print(f"El codigo de error fue {e}")
            return

        print(f"El patrocinador escogido es: {patrocinador_escogido} con un valor de {valor_puja}")

    def mostrar_categorias_de_juez(self, id_juez: str):
        """Muestra las categorias en las que puede votar un juez"""
        query = """
            SELECT IdCategoria
            FROM ValorarCategoria
            WHERE DNIJuez = '{id_juez}';
        """.format(id_juez = id_juez)

        results = self.try_execute(query, "Error seleccionando las categorias en las que un juez puede votar")

        # No estamos manejando esto con excepciones
        if results is None or len(results) == 0:
            return

        for result in results:
            id_categoria = result[0]
            print(f"Categoria con identificador {id_categoria}")

    def mostrar_categorias_fallables(self):
        """Mostramos las categorias en las que se ha votado"""
        try:
            results = self.execute("SELECT DISTINCT IdCategoria FROM VotarNominado")
        except Exeption as e:
            print("No se han encontrado categorias que se puedan fijar")
            print(f"El error fue {e}")

        print("Las categorías que se pueden fallar son: ")
        for result in results:
            id_categoria = result[0]
            print(f"Categoria {id_categoria}")


    def mostrar_nominados_de_categoria(self, id_categoria: int):
        """Muestra los nominados de una categoria concreta"""

        query = """
            SELECT DNINominado
            FROM SerCandidato
            WHERE idCategoria = {id_categoria};
        """.format(id_categoria = id_categoria)

        try:
            results = self.execute(query)
        except Exception as e:
            print("Fallo seleccionando los nominados de la categoria")
            print(f"El error fue {e}")
            raise("No se pudieron seleccionar nominados")

        for result in results:
            dni = result[0]
            print(f"Nominado con DNI: {dni}")

    def actividad_mayor(self):
        results = self.try_execute("SELECT MAX(idActividad) FROM Actividad;")
        try:
            return int(results[0][0])
        except:
            print("Error al intentar obtener la ultima actividad insertada en la base de datos")
            print("Se devuelve la actividad 0")
            return 0

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
            self.rollback(save)

    def usar_entrada(self, idActividad: int, dni: str, cantidad: int):
        # Tomamos la ultima entrada disponible
        ultima_entrada_disponible = None
        try:
            ultima_entrada_disponible = self.get_ultima_entrada_disponible(idActividad)
        except:
            print("Esa actividad no tiene entradas disponibles")
            print("Intentelo con otra actividad")
            raise Exception("No quedan entradas disponibles")


        # Asignamos a la actividad y al asistente la entrada
        try:
            query = """
                UPDATE UsarEntradas
                SET DNIAsistentes = '{dni}', Cantidad = {cantidad}
                WHERE
                    IdActividad = {idActividad}
                    AND IdEntrada = {ultima_entrada_disponible};
            """.format(dni = dni, idActividad = idActividad, ultima_entrada_disponible = ultima_entrada_disponible, cantidad = cantidad)
            self.execute(query)
            self.commit()

        except Exception as e:
            print("No se pudo asignar la entrada al asistente")
            print(f"El error fue {e}")
            raise Exception("No se puedo asignar entrada")

        return ultima_entrada_disponible

    def presentado_categoria(self, descrip: str, presen: str, idgala: int):
        try:
            self.execute(f"INSERT INTO PresentadoCategoria(Descripcion, Presentador, idGala) VALUES (\"{descrip}\", \"{presen}\", {idgala});")
            self.commit()

        except Exception as e:
            print("No se pudo planificar la categoria")
            print(f"El error fue {e}")

    def oferta_no_economica(self, idactividad: int, idpatro: int, coste: float, descrip: str, save: str):
        query = f"INSERT INTO OfertaActividadNoEconomica(IdActividadNoEconomica, IdPatrocinador, Coste, DescripcionRetribucion) VALUES ({idactividad}, {idpatro}, {coste}, \"{descrip}\");"

        try:
            self.execute(query)
        except Exception as e:
            print("No se pudo crear la oferta no economica")
            print(f"El error fue {e}")
            self.rollback(save)
            return

        self.commit()


    def devolver_entrada(self, id_actividad: int, id_entrada: int):
        """
        Se devuelve una entrada
        Para ello se marca como devuelta, para no perder datos de pagos
        """

        query = """
            UPDATE UsarEntradas
            SET Devolucion = TRUE
            WHERE IdEntrada = '{id_entrada}' AND IdActividad = '{id_actividad}'
        """.format(id_entrada = id_entrada, id_actividad = id_actividad)

        self.try_execute(query)
        self.commit()


    def fallar_premio(self, idcategoria: int):
        """Se falla la categoria indicada como parametro"""
        try:
            results = self.execute(f"SELECT DNINominado, COUNT(DNINominado) votos FROM VotarNominado  WHERE IdCategoria={idcategoria} GROUP BY DNINominado;")
        except Exception as e:
            print("No se pudo fallar la categoria correctamente")
            print(f"El error fue {e}")
            return

        print("Los resultados de la votacion son:")
        for result in results:
            dni = result[0]
            votos = result[1]
            print(f"Nominado: {dni}   Votos: {votos}")

        # Tomamos el ganador
        max_votos = int(result[0][1])
        ganador = result[0][0]
        for result in results:
            current_candidato = result[0]
            current_votos = int(result[1])

            if current_votos > max_votos:
                max_votos = current_votos
                ganador = current_candidato

        print(f"Por tanto, el ganador es {ganador} con {max_votos} votos")


    def fijar_patrocinador(self, id_actividad_subastada: int):
        # Marcamos la actividad como asignada
        self.try_execute(f"INSERT INTO ActividadAsignada VALUES ({id_actividad_subastada})", f"No se pudo marcar la actividad {id_actividad_subastada} como asignada")

        # Mostramos el patrocinador
        self.mostrar_mejor_patrocinador(id_actividad_subastada)

    def alta_patrocinador(self, nombre: str, prevision: float):
        query = f"INSERT INTO Patrocinador(Nombre, Prevision) VALUES (\"{nombre}\",{prevision});"
        self.try_execute(
            query,
            "No se pudo introducir el nuevo patrocinador"
        )
        self.commit()

    def get_ultima_entrada_disponible(self, idActividad: int):
        """
        Devuelve la ultima entrada disponible para una actividad concreta
        Si no hay entradas disponibles, lanza una excepcion
        """

        ultima_entrada_disponible = None
        try:
            query = """
                SELECT IdEntrada
                FROM UsarEntradas
                WHERE
                    DNIAsistentes IS NULL
                    AND IdActividad = {idActividad}
            """.format(idActividad = idActividad)

            # Tomo el primer resultado devuelto por la base de datos
            ultima_entrada_disponible = self.execute(query)
            ultima_entrada_disponible = ultima_entrada_disponible[0][0]
        except Exception as e:
            print(f"No se pudo obtener una entrada disponible para la actividad {idActividad}")
            print(f"El codigo de error fue {e}")
            raise Exception("No hay entradas disponibles")

        return ultima_entrada_disponible

    def comprar_entrada(self, id_entrada: str, id_actividad: str, cantidadPago:float):

        try:
            self.execute(
                f"INSERT INTO AbonaPagos(Cantidad, IdEntrada, IdActividad) VALUES ({cantidadPago},{id_entrada}, {id_actividad});"
            )
        except Exception as e:
            print("No se pudo insertar el pago en la base de datos")
            print(f"El error fue {e}")
            raise Exception("No se ha podido crear el pago")

        self.commit()

    def crear_actividad(self, descripcion: str, fecha:str):
        try:
            self.execute(
                f"INSERT INTO Actividad (Descripcion, Fecha) VALUES (\"{descripcion}\", \"{fecha}\")"
            )
        except Exception as e:
            print("No se pudo insertar la actividad en la base de datos")
            print(f"El error fue {e}")
            raise Exception("No se ha podido crear la actividad")

        self.commit()

    def insertar_entradas_para_actividad(self, IdActividad: str, cantidadEntradas:int):

        # Creamos la peticion para insertar un numero dado de entradas a una actividad
        query = "INSERT INTO UsarEntradas(IdEntrada, IdActividad) VALUES "
        query += f"({0}, {IdActividad}) "

        for i in range (cantidadEntradas-1):
            query += f",({i+1}, {IdActividad})"
        query += ";"

        try:
            self.execute(query)
        except Exception as e:
            print("Error, crear_actividad, no se pudo insertar las entradas")
            print(f"El error fue {e}")
            raise Exception("No se ha insertar las entradas,")

        self.commit()

    def votar(self, id_juez: str, id_categoria: int, id_nominado: str):
        """Se realiza una votacion"""

        query = """
            INSERT INTO VotarNominado(DNIJuez, IdCategoria, DNINominado) VALUES
                ("{id_juez}", {id_categoria}, "{id_nominado}");
        """.format(id_juez = id_juez, id_categoria = id_categoria, id_nominado = id_nominado )

        try:
            self.execute(query)
        except Exception as e:
            print("No se pudo insertar la votacion en la base de datos")
            print(f"El codigo de error fue: {e}")
            raise Exception("No se pudo insertar la votacion")

        self.commit()


    def puja(self, idactividad: int, idpatro: int, valor: float):
        """Se realiza la puja"""

        query = """
            INSERT INTO Puja(IdPatrocinador, IdActividad, Valor) VALUES
                ({idpatro}, {idactividad}, {valor});
        """.format(idpatro = idpatro, idactividad = idactividad, valor = valor )

        self.try_execute(query)
        self.commit()

    def asignar_nominado_a_categoria(self, idCategoria: int, dniNominado: str):
        self.try_execute(
            f"INSERT INTO SerCandidato(DNINominado, IdCategoria) VALUES (\"{dniNominado}\",{idCategoria});",
            "No se pudo asignar el nominado a esta categoria"
        )
        self.commit()
