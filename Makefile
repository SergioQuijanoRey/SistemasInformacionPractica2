all:
	@echo "Las funcionalidades de este makefile son:"
	@echo "	install: instala el software necesario para lanzar la aplicacion: docker + pipenv"
	@echo "	run: ejecuta la aplicacion"
	@echo "	perms: da permisos a la base de datos. Se tiene que esperar un poco despues de instalar para poder ejecutarse con exito"
	@echo "	database: conecta con la base de datos corriendo en el contenedor"

install:
	@echo "Construyendo imagen de docker"
	@echo "================================================================================"
	docker build -t mariadb_practicas:latest .

	@echo "Asignando red de docker"
	@echo "================================================================================"
	docker network create own_network || echo "La red ya existe"

	@echo ""
	@echo "Limpiando contenedores anteriores"
	@echo "================================================================================"
	docker stop mariadb_practicas 2> /dev/null || echo "No hay contenedor que limpiar" && echo "Contenedor parado"
	docker rm -f mariadb_practicas || echo "No hay contenedor que borrar" && echo "Contenedor borrado"

	@echo ""
	@echo "Corriendo un contenedor de dicha imagen"
	@echo "================================================================================"
	docker run --name mariadb_practicas --net=own_network -d mariadb_practicas:latest

	@echo ""
	@echo "La ip del contenedor es:"
	@echo "================================================================================"
	docker inspect mariadb_practicas | grep -i ipaddress

	@echo ""
	@echo "Instalando paquetes de pipenv"
	@echo "================================================================================"
	pipenv install


run:
	@echo "Lanzando el contenedor, si no estaba ya lanzando"
	docker start mariadb_practicas
	@echo ""
	@echo "Lanzando aplicacion de python"
	pipenv run python3 ./src/python/main.py

perms:
	@echo ""
	@echo "Dando permisos a la base de datos"
	@echo "================================================================================"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "GRANT ALL PRIVILEGES ON *.* TO 'sergio'@localhost IDENTIFIED BY 'sergio';"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "FLUSH PRIVILEGES;"
	docker exec mariadb_practicas mysql -u root "-psergio" -e "COMMIT;"

database:
	echo "Conectando con la base de datos"
	@echo "================================================================================"
	docker exec -it mariadb_practicas mysql -u sergio "-psergio"
