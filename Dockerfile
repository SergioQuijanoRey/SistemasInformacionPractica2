FROM mariadb:10.5
RUN apt update ; apt install vim -y

# MariaDB user, password, database and root password
ENV MYSQL_USER=sergio \
    MYSQL_PASSWORD=sergio \
    MYSQL_DATABASE=sergio \
    MYSQL_ROOT_PASSWORD=sergio

# SQL files with trigger code are added to the database
COPY ./src/sql/Triggers.sql /code/
COPY ./src/sql/TriggersPremios.sql /code/
