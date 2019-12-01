CREATE TABLE IF NOT EXISTS "user"(
  "login" VARCHAR(20) PRIMARY KEY NOT NULL,
  "password" VARCHAR(64) NOT NULL,
  "name" TEXT NOT NULL,
  email VARCHAR(64) NOT NULL UNIQUE,
  birthday DATE NOT NULL,
  registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

  country TEXT,
  "state" TEXT,
  city TEXT ,
  neighborhood TEXT,
  street TEXT,
  "number" INT,
  complement TEXT

);

CREATE TABLE IF NOT EXISTS phone(
  phone VARCHAR (14) NOT NULL,
  "login" VARCHAR(20) NOT NULL,

  PRIMARY KEY (phone,"login"),
  FOREIGN KEY ("login") REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS follow(
  login_follower VARCHAR(20) NOT NULL,
  login_followed VARCHAR(20) NOT NULL,

  PRIMARY KEY (login_follower, login_followed),
  FOREIGN KEY (login_follower) REFERENCES "user" ("login"),
  FOREIGN KEY (login_followed) REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS team(
  initials VARCHAR(5) PRIMARY KEY NOT NULL,
  "name" VARCHAR(26) NOT NULL,
  owner_login VARCHAR(20) NOT NULL,

  FOREIGN KEY (owner_login) REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS tournament(
  cod_tournament SERIAL PRIMARY KEY,
  "name" VARCHAR(30) NOT NULL,
  "description" TEXT,
  "start_date" DATE NOT NULL,
  end_date  DATE NOT NULL,
  owner_login VARCHAR(20) NOT NULL,
  winner VARCHAR(5),

  FOREIGN KEY ("winner") REFERENCES team ("initials") ON UPDATE CASCADE,
  FOREIGN KEY (owner_login) REFERENCES "user" ("login") ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS moderator(
  "login" VARCHAR(20) PRIMARY KEY NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login") ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS punter(
  "login" VARCHAR(20) PRIMARY KEY NOT NULL,
  balance FLOAT NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login") ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS participant(
  "login" VARCHAR(20) PRIMARY KEY NOT NULL,
  nickname VARCHAR(20) UNIQUE NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login") ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS moderate(
  moderator_login VARCHAR(20) NOT NULL,
  cod_tournament SERIAL,

  PRIMARY KEY (moderator_login, cod_tournament),
  FOREIGN KEY (moderator_login) REFERENCES "user" ("login") ON DELETE CASCADE,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS match(
  id_match INT,
  "date" DATE NOT NULL,
  winner VARCHAR(5),
  cod_tournament SERIAL,

  PRIMARY KEY (id_match, cod_tournament),
  FOREIGN KEY (winner) REFERENCES team (initials) ON UPDATE CASCADE,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS play(
  initials VARCHAR(5),
  id_match INT,
  cod_tournament SERIAL,

  PRIMARY KEY (initials, id_match, cod_tournament),
  FOREIGN KEY (initials) REFERENCES team (initials) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_match,cod_tournament) REFERENCES match (id_match,cod_tournament) ON DELETE CASCADE,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS team_member(
  participant_login VARCHAR(20) NOT NULL,
  initials VARCHAR(5) NOT NULL,

  PRIMARY KEY (participant_login,initials),
  FOREIGN KEY (participant_login) REFERENCES "user" ("login") ON DELETE CASCADE,
  FOREIGN KEY (initials) REFERENCES team (initials) ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE IF NOT EXISTS integrate(
  participant_login VARCHAR(20) NOT NULL,
  initials VARCHAR(5) NOT NULL,
  cod_tournament SERIAL,

  PRIMARY KEY (participant_login,initials, cod_tournament),
  FOREIGN KEY (participant_login) REFERENCES "user" ("login") ON DELETE CASCADE,
  FOREIGN KEY (initials) REFERENCES team (initials) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS mvp_bet(
  punter_login VARCHAR(20) NOT NULL,
  participant_login VARCHAR(20) NOT NULL,
  initials VARCHAR(5) NOT NULL,
  cod_tournament SERIAL,

  PRIMARY KEY (punter_login, participant_login,initials, cod_tournament),
  FOREIGN KEY (punter_login) REFERENCES "user" ("login") ON DELETE CASCADE,
  FOREIGN KEY (participant_login) REFERENCES "user" ("login") ON DELETE CASCADE,
  FOREIGN KEY (initials) REFERENCES team (initials) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE

);

CREATE TYPE "type" AS ENUM ('VARCHAR','TEXT','INT','FLOAT','DATE','SERIAL');

CREATE TABLE IF NOT EXISTS attribute(
  id_attribute INT,
  cod_tournament SERIAL,
  "name" VARCHAR(20) NOT NULL,
  "type" "type" NOT NULL,
  

  PRIMARY KEY (id_attribute, cod_tournament),
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS attribute_participant(
  id_attribute INT,
  participant_login VARCHAR(20) NOT NULL,
  cod_tournament SERIAL,
  "value" TEXT,

  PRIMARY KEY (id_attribute, cod_tournament, participant_login),
  FOREIGN KEY (id_attribute,cod_tournament) REFERENCES attribute (id_attribute,cod_tournament) ON DELETE CASCADE,
  FOREIGN KEY (participant_login) REFERENCES "user" ("login") ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS attribute_match(
  id_attribute INT,
  id_match INT,
  cod_tournament SERIAL,
  "value" TEXT,

  PRIMARY KEY (id_attribute, id_match,cod_tournament),
  FOREIGN KEY (id_attribute,cod_tournament) REFERENCES attribute (id_attribute,cod_tournament) ON DELETE CASCADE,
  FOREIGN KEY (id_match,cod_tournament) REFERENCES match (id_match,cod_tournament) ON DELETE CASCADE

);
