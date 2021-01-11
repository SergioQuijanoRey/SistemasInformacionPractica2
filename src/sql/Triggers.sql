

DELIMITER //
CREATE OR REPLACE TRIGGER devolucion_Entrada_Covid
  AFTER 
  UPDATE ON UsarEntradas
  FOR EACH ROW 
    BEGIN

      DECLARE covid BOOLEAN;

      SELECT Covid INTO covid FROM Asistentes WHERE Asistentes.DNIAsistente=NEW.DNIAsistentes;

      IF covid = TRUE THEN
        UPDATE UsarEntradas SET Devolucion = TRUE WHERE UsarEntradas.DNIAsistentes=NEW.DNIAsistentes;
        --select "penguin" as log into outfile '/tmp/result.txt'
      END IF;

    END //
DELIMITER ;


DELIMITER //
CREATE OR REPLACE TRIGGER devolucion_Entrada_Covid_update
  BEFORE 
  UPDATE ON Asistentes
  FOR EACH ROW 
    BEGIN

      IF NEW.Covid = TRUE THEN
        UPDATE UsarEntradas SET Devolucion = TRUE WHERE UsarEntradas.DNIAsistentes = NEW.DNIAsistente;
      END IF;

    END //
DELIMITER ;




--Trigger para comprobar la hora a la que acude el invitado en asignar_hora_invitado
DELIMITER //
CREATE OR REPLACE TRIGGER comprobar_hora_invitado
  BEFORE
  INSERT ON Acudir
  FOR EACH ROW
    BEGIN
        DECLARE hora_inicio TIME;
        DECLARE hora_fin TIME;

        SELECT horaInicio INTO hora_inicio FROM AlfombraRoja WHERE AlfombraRoja.idAlfombraRoja = NEW.idAlfombraRoja;
        SELECT horaFin INTO hora_fin FROM AlfombraRoja WHERE AlfombraRoja.idAlfombraRoja = NEW.idAlfombraRoja;

        IF NEW.hora < hora_inicio THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hora anterior a la hora de inicio de la alfombra';
        ELSEIF NEW.hora > hora_fin THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hora posterior a la hora de fin de la alfombra';
        END IF;

    END //
  DELIMITER ;

--Trigger para que subasta patrocinio economico no se permitan propuestas economicas negativas
DELIMITER //
CREATE OR REPLACE TRIGGER comprobar_propuesta_economica
  BEFORE
  INSERT ON Puja
  FOR EACH ROW
    BEGIN

        IF NEW.Valor < 0 THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se pueden pujar valores negativos';
        END IF;

    END //
  DELIMITER ;

--Trigger para ver que en oferta no economica, el coste sea un numero positivo
  DELIMITER //
  CREATE OR REPLACE TRIGGER comprobar_coste_no_economica
    BEFORE
    INSERT ON OfertaActividadNoEconomica
    FOR EACH ROW
      BEGIN

          IF NEW.Coste < 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El coste de la oferta no puede ser negativo';
          END IF;

      END //
    DELIMITER ;

--Trigger para ver que en dar de alta patrocinador, la prevision sea un numero positivo
  DELIMITER //
  CREATE OR REPLACE TRIGGER comprobar_prevision_patrocinador
    BEFORE
    INSERT ON Patrocinador
    FOR EACH ROW
      BEGIN

          IF NEW.Prevision < 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La prevision no puede ser negativa';
          END IF;

      END //
  DELIMITER ;

--Trigger para ver que en usar entrada, la cantidad de entradas no sea negativa
  DELIMITER //
  CREATE OR REPLACE TRIGGER comprobar_cantidad_entradas
    BEFORE
    UPDATE ON UsarEntradas
    FOR EACH ROW
      BEGIN

          IF NEW.Cantidad <= 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La cantidad de entradas no puede ser negativa o nula';
          END IF;

      END //
  DELIMITER ;
