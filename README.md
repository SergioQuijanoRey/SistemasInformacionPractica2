# Práctica 2 Sistemas de Información

* Repositorio para crear las sentencias de `SQL` de Diseño y Desarrollo Sistemas de Información

# TODO

* [x] Conseguir que funcione python: Jesus y Juanjo
* [ ] Quitar del makefile el "python_jesus"
* [ ] Separar el CrearTablas.sql en creacion de tablas, triggers e insercion de datos
* [ ] Trigger: Dar permiso periodista, si el periodista tiene covid, que no pueda acceder ??
* [ ] Gestionar Asistentes
    * [xx] Comprar entrada : Juanjo
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
        * [x ] Trigger para comprobar que la hora introducida es correcta
    * [xx] Dar permiso a periodista: Sergio
    * [xx] Asignar rueda de prensa a pelicula: Jesus
        * Duda con savepoint
    * [xx] Crear actividad: Juanjo
      * [ ] Poder particularizar la actividad Creada
* [xx] Gestion de premios
	* [xx] Votar: Juanjo
        * [ ] Un juez puede votar en categorñías que no le corresponde
	* [xx] Planificar premio : Lucia
	* [xx] Asignar nominado a premio : Juanjo
	* [xx] Fallar premio : Jesus
* [ ] Gestión de patrocinadores
	* [xx] Dar de alta a patrocinador : Juanjo
	* [xx] Patrocinar actividad no económica : Lucía
        * Duda con savepoint
	* [xx] Subasta de patrocinio económico
	* [xx] Fijar patrocinador: Sergio

* **Triggers**:
    * [ ] Trigger para saber si la entrada se puede devolver o no segun fecha y covid : Juanjo
    * [x ] Trigger para comprobar que la hora introducida es correcta: Jesus
    * [ ] Trigger para comprobar en votar, que la categoria, el juez y nominado esten de verdad relacionados
    * [ ] Trigger para ver que en devolver entrada, los datos sean correctos, porque el UPDATE no falla
    * [x ] Trigger para ver que en usar entrada, la cantidad de entradas no sea negativa : Junta directiva
    * [x ] Trigger para ver que en dar de alta patrocinador, la prevision sea un numero positivo : Jesus
    * [x ] Trigger para ver que en oferta no economica, el coste sea un numero positivo : Lucia
	* [x ] Trigger para que subasta patrocinio economico no se permitan propuestas economicas negativas : Lucia

## Cosas que revisar antes de hacer la entrega

* [ ] Comprobar que cada subsistema tenga al menos un trigger
* [ ] Describir en el PDF las transacciones
* [ ] Fe de erratas de la práctica 2 en el PDF
* [ ] Poner el código de los disparadores en el PDF
* [ ] Motivacion del software escogido en el PDF (media página)

