-- Trigger para ver que el juez y el nominado estan en las categorias correspondientes
DELIMITER //
CREATE OR REPLACE TRIGGER juez_y_nominado_en_la_categoria
  BEFORE
  INSERT ON VotarNominado
  FOR EACH ROW
    BEGIN
        DECLARE dni_juez VARCHAR(9);
        DECLARE nominado VARCHAR(9);

        SELECT DNIJuez INTO dni_juez FROM ValorarCategoria WHERE DNIJuez = NEW.DNIJuez AND IdCategoria = NEW.IdCategoria;
        SELECT DNINominado INTO nominado FROM SerCandidato WHERE DNINominado = NEW.DNINominado AND IdCategoria = NEW.IdCategoria;

        IF NEW.DNIJuez <> dni_juez THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El juez no esta asignado a esa categoria';
        ELSEIF NEW.DNINominado <> nominado THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El candidato no esta nominado a esa categoria';
        END IF;

    END //
DELIMITER ;

-- El juez no puede votar mas de dos veces
DELIMITER //
CREATE OR REPLACE TRIGGER juez_vota_una_unica_vez
  BEFORE
  INSERT ON VotarNominado
  FOR EACH ROW
    BEGIN
        DECLARE nominado VARCHAR(9);

        SELECT DNINominado INTO nominado FROM VotarNominado WHERE DNIJuez = NEW.DNIJuez AND IdCategoria = NEW.IdCategoria;

        IF nominado IS NOT NULL THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El juez ya ha votado en esta categoria';
        END IF;

    END //
DELIMITER ;
