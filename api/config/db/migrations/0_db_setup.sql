CREATE TABLE IF NOT EXISTS "user"(
  "login" VARCHAR(20) PRIMARY KEY NOT NULL,
  "password" VARCHAR(50) NOT NULL,
  "name" TEXT NOT NULL,
  email VARCHAR(256) NOT NULL,
  birthday DATE NOT NULL,
  registration_date DATE NOT NULL,

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

CREATE TABLE IF NOT EXISTS tournament(
  cod_tournament VARCHAR(10) PRIMARY KEY NOT NULL,
  "name" VARCHAR(30) NOT NULL,
  descripton TEXT,
  "start_date" DATE NOT NULL,
  end_date  DATE NOT NULL,
  owner_login VARCHAR(20) NOT NULL,


  FOREIGN KEY (owner_login) REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS moderator(
  login VARCHAR(20) PRIMARY KEY NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS punter(
  login VARCHAR(20) PRIMARY KEY NOT NULL,
  balance FLOAT NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS participant(
  login VARCHAR(20) PRIMARY KEY NOT NULL,
  nickname VARCHAR(20) UNIQUE NOT NULL,

  FOREIGN KEY ("login") REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS moderate(
  moderator_login VARCHAR(20) NOT NULL,
  cod_tournament VARCHAR(16) NOT NULL,

  PRIMARY KEY (moderator_login, cod_tournament),
  FOREIGN KEY (moderator_login) REFERENCES "user" ("login") ,
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament)
);


CREATE TABLE IF NOT EXISTS team(
  initials VARCHAR(5) PRIMARY KEY NOT NULL,
  "name" VARCHAR(20) NOT NULL

);

CREATE TABLE IF NOT EXISTS match(
  id_match VARCHAR(10) NOT NULL,
  "date" DATE NOT NULL,
  winner VARCHAR(5),
  cod_tournament VARCHAR(10) NOT NULL,

  PRIMARY KEY (id_match, cod_tournament),
  FOREIGN KEY (winner) REFERENCES team (initials),
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) 
);

CREATE TABLE IF NOT EXISTS play(
  initials VARCHAR(5) NOT NULL,
  id_match VARCHAR(10) NOT NULL,
  cod_tournament VARCHAR(10) NOT NULL,

  PRIMARY KEY (initials, id_match, cod_tournament),
  FOREIGN KEY (initials) REFERENCES team (initials),
  FOREIGN KEY (id_match,cod_tournament) REFERENCES match (id_match,cod_tournament),
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament) 
);

CREATE TABLE IF NOT EXISTS integrate(
  participant_login VARCHAR(20) NOT NULL,
  initials VARCHAR(5) NOT NULL,
  cod_tournament VARCHAR(10) NOT NULL,

  PRIMARY KEY (participant_login,initials, cod_tournament),
  FOREIGN KEY (participant_login) REFERENCES "user" ("login"),
  FOREIGN KEY (initials) REFERENCES team (initials),
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament)

);

CREATE TABLE IF NOT EXISTS mvp_bet(
  punter_login VARCHAR(20) NOT NULL,
  participant_login VARCHAR(20) NOT NULL,
  initials VARCHAR(5) NOT NULL,
  cod_tournament VARCHAR(10) NOT NULL,

  PRIMARY KEY (punter_login, participant_login,initials, cod_tournament),
  FOREIGN KEY (punter_login) REFERENCES "user" ("login"),
  FOREIGN KEY (participant_login) REFERENCES "user" ("login"),
  FOREIGN KEY (initials) REFERENCES team (initials),
  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament)

);

CREATE TYPE "type" AS ENUM ('VARCHAR','TEXT','INT','FLOAT','DATE');

CREATE TABLE IF NOT EXISTS attribute(
  id_attribute VARCHAR(10) PRIMARY KEY NOT NULL,
  "name" VARCHAR(20) NOT NULL,
  "type" "type" NOT NULL,
  cod_tournament VARCHAR(10) NOT NULL,

  FOREIGN KEY (cod_tournament) REFERENCES tournament (cod_tournament)

);

CREATE TABLE IF NOT EXISTS attribute_participant(
  id_attribute VARCHAR(10) NOT NULL,
  participant_login VARCHAR(20) NOT NULL,
  "value" TEXT,

  PRIMARY KEY (id_attribute, participant_login),
  FOREIGN KEY (id_attribute) REFERENCES attribute (id_attribute),
  FOREIGN KEY (participant_login) REFERENCES "user" ("login")

);

CREATE TABLE IF NOT EXISTS attribute_match(
  id_attribute VARCHAR(10) NOT NULL,
  id_match VARCHAR(10) NOT NULL,
  cod_tournament VARCHAR(10) NOT NULL,
  "value" TEXT,

  PRIMARY KEY (id_attribute, id_match,cod_tournament),
  FOREIGN KEY (id_attribute) REFERENCES attribute (id_attribute),
  FOREIGN KEY (id_match,cod_tournament) REFERENCES match (id_match,cod_tournament)

);
