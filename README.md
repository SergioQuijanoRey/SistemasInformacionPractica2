# Práctica 2 Sistemas de Información

* Repositorio para crear las sentencias de `SQL` de Diseño y Desarrollo Sistemas de Información

# TODO

* [x] Conseguir que funcione python: Jesus y Juanjo
* [ ] Quitar del makefile el "python_jesus"
* [ ] Separar el CrearTablas.sql en creacion de tablas, triggers e insercion de datos
* [ ] Trigger: Dar permiso periodista, si el periodista tiene covid, que no pueda acceder ??
* [ ] Gestionar Asistentes
    * [ ] Comprar entrada : Juanjo
    * [xx] Notificar estado Covid: Sergio
        * [ ] Escribir triggers relacionados con tener covid
        * [ ] El update no falla aunque el usuario pase mal los parametros
    * [xx] Devolver entrada: Sergio
        * [ ] El update no falla aunque el usuario pase mal los parametros
        * [ ] Trigger para saber si la entrada se puede devolver o no
    * [xx] Notificar asistencia actividad gratuita: Lucía
        * [ ] Mostrar actividades que tengan disponibles entradas para simplificar las cosas
* [xx] Gestion de asistentes
    * [xx] Asignar hora invitado para alfombra roja: Lucía
        * [ ] Trigger para comprobar que la hora introducida es correcta
    * [xx] Dar permiso a periodista: Sergio
    * [xx] Asignar rueda de prensa a pelicula: Jesus
        * Duda con savepoint
    * [xx] Crear actividad: Juanjo
      * [ ] Poder particularizar la actividad Creada
* [ ] Gestion de premios
	* [xx] Votar: Juanjo
	* [x] Planificar premio : Lucia
	* [x] Asignar nominado a premio : Juanjo
	* [x] Fallar premio : Jesus
* [ ] Gestión de patrocinadores
	* [x] Dar de alta a patrocinador : Juanjo
	* [x] Patrocinar actividad no económica : Lucía
        * Duda con savepoint
	* [ ] Subasta de patrocinio económico
	* [x] Fijar patrocinador: Sergio
