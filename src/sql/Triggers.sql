

CREATE TRIGGER devolucionEntradaCovid
AFTER INSERT OR UPDATE ON UsarEntradas
BEGIN
    IF EXISTS (SELECT * FROM Asistentes WHERE DNIAsistente = :new.DNIAsistente AND covid = true ) THEN
        UPDATE Devolucion SET Devolucion = TRUE;
END;

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
  DELIMITER;
