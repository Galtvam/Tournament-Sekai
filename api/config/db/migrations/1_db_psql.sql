CREATE FUNCTION assign_id_match() RETURNS trigger AS $assign_id_match$
    BEGIN
    
    END; $assign_id_match$
    LANGUAGE PLPGSQL;
    
 CREATE TRIGGER assign_id_match BEFORE INSERT OR UPDATE ON empregados
    FOR EACH ROW EXECUTE PROCEDURE assign_id_match();





END

CREATE OR REPLACE FUNCTION matches_counter
(v_cod_tournament INTEGER) 
RETURNS integer AS 
$$
DECLARE
matches_count INT;
BEGIN
    SELECT COUNT(*)
    INTO matches_count
    FROM match AS m
    INNER JOIN tournament AS t on m.cod_tournament = t.cod_tournament
    WHERE t.cod_tournament = v_cod_tournament;

   RETURN matches_count;
END; $$
LANGUAGE PLPGSQL;

select matches_counter(5)