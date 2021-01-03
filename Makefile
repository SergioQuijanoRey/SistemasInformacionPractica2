all:
	@echo "Las funcionalidades de este makefile son:"
	@echo "	install: instala el software necesario para lanzar la aplicacion: docker + pipenv"
	@echo "	run: ejecuta la aplicacion"

install:
	@echo "Construyendo imagen de docker"
	@echo "================================================================================"
	docker build -t mariadb_practicas:latest .

	@echo ""
	@echo "Limpiando contenedores anteriores"
	@echo "================================================================================"
	docker stop mariadb_practica 2> /dev/null || echo "No hay contenedor que limpiar"
	docker rm -f mariadb_practicas

	@echo ""
	@echo "Corriendo un contenedor de dicha imagen"
	@echo "================================================================================"
	docker run --name mariadb_practicas -d mariadb_practicas:latest

	@echo ""
	@echo "La ip del contenedor es:"
	@echo "================================================================================"
	docker inspect mariadb_practicas | grep -i ipaddress

	@echo ""
	@echo "Instalando paquetes de pipenv"
	@echo "================================================================================"
	pipenv install

run:
	@echo "Lanzando aplicacion de python"
	pipenv run python3 ./src/python/main.py
