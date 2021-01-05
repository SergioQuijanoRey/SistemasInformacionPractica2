FROM python:3.8

# Instalacion de paquetes
RUN pip install mariadb

# Copiamos el codigo
WORKDIR /code
COPY ./ /code

# Comando a lanzar
CMD ["python", "/code/src/python/main.py"]
