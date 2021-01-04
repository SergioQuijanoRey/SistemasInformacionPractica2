

CREATE TRIGGER devolucionEntradaCovid
AFTER INSERT OR UPDATE ON UsarEntradas
BEGIN
    IF EXISTS (SELECT * FROM Asistentes WHERE DNIAsistente = :new.DNIAsistente AND covid = true ) THEN
        UPDATE Devolucion SET Devolucion = TRUE;
END;