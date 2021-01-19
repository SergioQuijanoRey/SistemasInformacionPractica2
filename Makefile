all:
	@echo "Las funcionalidades de este makefile son:"
	@echo "	install: instala el software necesario para lanzar la aplicacion: docker + pipenv"
	@echo "	database_run: ejecuta la base de datos"
	@echo "	database_connect: conecta con la base de datos corriendo en el contenedor"
	@echo "	python_run: lanza la aplicacion corriendo otro contenedor"
	@echo "	plain_run: lanza la aplicacion corriendo directamente desde el host"
	@echo "	perms: da permisos a la base de datos. Se tiene que esperar un poco despues de instalar para poder ejecutarse con exito"
	@echo "	load_triggers: carga los triggers en la base de datos"

install:
	@echo "Construyendo imagen de docker"
	@echo "================================================================================"
	docker build -t mariadb_practicas:latest .

	@echo ""
	@echo "Asignando red de docker"
	@echo "================================================================================"
	docker network create --subnet=172.20.0.0/16 own_network 2> /dev/null || echo "La red ya existe"

	@echo ""
	@echo "Limpiando contenedores anteriores"
	@echo "================================================================================"
	docker stop mariadb_practicas 2> /dev/null || echo "No hay contenedor que limpiar" && echo "Contenedor parado"
	docker rm -f mariadb_practicas || echo "No hay contenedor que borrar" && echo "Contenedor borrado"

	@echo ""
	@echo "Corriendo un contenedor de dicha imagen"
	@echo "================================================================================"
	docker run --name mariadb_practicas --net=own_network --ip 172.20.0.2 -d mariadb_practicas:latest

	@echo ""
	@echo "La ip del contenedor es:"
	@echo "================================================================================"
	docker inspect mariadb_practicas | grep -i ipaddress

	@echo ""
	@echo "Instalando paquetes de pipenv"
	@echo "================================================================================"
	pipenv install

database_run:
	@echo "Lanzando el contenedor de bases de datos, si no estaba ya lanzando"
	@echo "================================================================================"
	docker start mariadb_practicas

plain_run:
	@echo ""
	@echo "Lanzando aplicacion de python desde el host"
	@echo "================================================================================"
	pipenv run python3 ./src/python/main.py

database_connect:
	@echo "Conectando con la base de datos"
	@echo "================================================================================"
	docker exec -it mariadb_practicas mysql -u sergio "-psergio" sergio

python_run:
	@echo "Creando contenedor de python con el codigo actualizado"
	@echo "================================================================================"
	docker build -t python_jesus:latest -f ./Jesus/Dockerfile .

	@echo ""
	@echo "Borrando los contenedores de python corriendo anteriores"
	@echo "================================================================================"
	docker stop python_jesus 2> /dev/null || echo "No habia contenedor que parar"
	docker rm -f python_jesus 2> /dev/null || echo "No habia contenedor que borrar"

	@echo ""
	@echo "Lanzamos el contenedor de python"
	@echo "================================================================================"
	docker run --name python_jesus --net=own_network --ip 172.20.0.3 -it python_jesus

perms:
	@echo ""
	@echo "Dando permisos a la base de datos"
	@echo "================================================================================"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "GRANT ALL PRIVILEGES ON *.* TO 'sergio'@localhost IDENTIFIED BY 'sergio';"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "GRANT ALL PRIVILEGES ON *.* TO 'sergio'@172.20.0.3 IDENTIFIED BY 'sergio';"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "FLUSH PRIVILEGES;"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "COMMIT;"

load_triggers:
	@echo ""
	@echo "Cargando los triggers en la base de datos"
	@echo "================================================================================"
	docker exec mariadb_practicas mysql -u root "-psergio" "sergio" -e "SOURCE /code/Triggers.sql;"
	docker exec mariadb_practicas mysql -u root "-psergio" "sergio" -e "SOURCE /code/TriggersPremios.sql;"
	docker exec mariadb_practicas mysql -u root "-psergio" "sergio" -e "COMMIT;"
