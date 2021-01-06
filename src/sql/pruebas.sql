
CREATE TABLE IF NOT EXISTS animals (id mediumint(9)
NOT NULL AUTO_INCREMENT,
name char(30) NOT NULL,
PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS animal_count (animals int);

INSERT INTO animal_count (animals) VALUES(0);

CREATE TRIGGER IF NOT EXISTS increment_animal
AFTER INSERT ON animals
FOR EACH ROW
UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
