CREATE OR REPLACE FUNCTION team_owner_member() RETURNS trigger AS $team_owner_member$
    BEGIN
		INSERT INTO team_member VALUES (NEW.owner_login, NEW.initials);
        RETURN NEW;
    END;
$team_owner_member$ LANGUAGE PLPGSQL;

DROP TRIGGER IF EXISTS team_owner_member ON team;
CREATE TRIGGER team_owner_member AFTER INSERT ON team
    FOR EACH ROW EXECUTE PROCEDURE team_owner_member();


CREATE OR REPLACE FUNCTION create_tournament_match() RETURNS trigger AS $create_tournament_match$
    BEGIN
        UPDATE match SET id_match=matches_counter(NEW.cod_tournament) + 1
        WHERE cod_tournament=NEW.cod_tournament AND id_match=NEW.id_match;
        RETURN NEW;
    END;
$create_tournament_match$ LANGUAGE PLPGSQL;

DROP TRIGGER IF EXISTS create_tournament_match ON match;
CREATE TRIGGER create_tournament_match AFTER INSERT ON match
    FOR EACH ROW EXECUTE PROCEDURE create_tournament_match();

CREATE OR REPLACE FUNCTION matches_counter (v_cod_tournament INTEGER) 
RETURNS integer AS 
$$
DECLARE
    matches_count INT;
BEGIN
    SELECT coalesce(MAX(id_match), 1) INTO matches_count FROM match AS m
    INNER JOIN tournament AS t on m.cod_tournament = t.cod_tournament
    WHERE t.cod_tournament = v_cod_tournament;

   RETURN matches_count;
END; $$
LANGUAGE PLPGSQL;