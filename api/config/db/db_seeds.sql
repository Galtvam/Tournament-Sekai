--Usuários
INSERT INTO "user" VALUES('Gokuzinho','33333333','Son Goku', 'gokuzinho@gmail.com', '02/02/2010','02/02/2010');
INSERT INTO "user" VALUES('Luffyzinho', '77777777', 'Monkey D. Luffy', 'luffyzinho@gmail.com', '03/03/2003','03/03/20011');
INSERT INTO "user" VALUES('Ichigozinho', '66666666', 'Kurosaki Ichigo', 'ichigozinho@gmail.com', '04/03/2003','04/03/2009');
INSERT INTO "user" VALUES('Natsuzinho', '22222222', 'Natsu Dragneel', 'natsuzinho@gmail.com', '05/03/2003','05/03/2007' );
INSERT INTO "user" VALUES('Gonzinho', '55555555','Gon Freecs', 'gonzinho@gmail.com', '06/03/2003','06/03/2014');
INSERT INTO "user" VALUES('Gintokizinho','44444444','Sakata Gintoki', 'gintokizinho@gmail.com', '07/03/2003','07/03/2012');
INSERT INTO "user" VALUES('Midoriyazinho', '11111111', 'Izuku Midoriya', 'midoriya@gmail.com', '08/03/2003','08/03/2013');
INSERT INTO "user" Values('Seiyazinho','88888888','Seiya de Pegasus', 'seiyazinho@gmail.com', '09/09/2015', '12/12/2012');

--Times

INSERT INTO "team" VALUES ('OSS','Os Super Sayajins','Gokuzinho');
INSERT INTO "team" VALUES ('CDS','Cavaleiros do Saara','Gintokizinho');
INSERT INTO "team" VALUES ('CDZ','Cavaleiros do Zodiaco','Seiyazinho');
INSERT INTO "team" VALUES ('FT','Fairy Tail','Natsuzinho');
INSERT INTO "team" VALUES ('UA','Universidade de Herois','Midoriyazinho');
INSERT INTO "team" VALUES ('SDS','Shinigamis do Sertão','Ichigozinho');

--Torneios

INSERT INTO "tournament" VALUES (1,'Melhor Torneio de YuGiOh','Melhor torneio de YuGiOh da sua rua, vai ser muito top vey','10/10/2019','11/10/2019','Gokuzinho','UA');
INSERT INTO "tournament" VALUES (2,'Melhor Torneio de Robblox','O torneio que as crianças vão amar, um jogo que ninguem gosta, só tiram onda por que é um lixo','05/11/2019','07/11/2019','Gintokizinho','UA');
INSERT INTO "tournament" VALUES (3,'Torneio Galático','Torneio de batalha entre deuses e grandes guerreiros de todas as galáxias','11/22/2019','11/26/2019','Gokuzinho','CDZ');
INSERT INTO "tournament" VALUES (4,'Exame Hunter','Torneio para saber quais serão os próximos seres qualificados para possui a licença Hunter','05/11/2019','10/11/2019','Gonzinho','UA');
INSERT INTO "tournament" VALUES (5,'Torneio de Counter Strike','Torneio que reune os melhores times do cenário brasileiro de cs-go, com premiação de incriveis 3 reais','12/17/2019','12/22/2019','Natsuzinho');
INSERT INTO "tournament" VALUES (6,'Torneio de Espadas','Torneio que reune todos os espadachins dos mundos, da sociedade das almas, para saber quem é o mais forte','07/02/2020','03/13/2020','Ichigozinho');



--Telefones

INSERT INTO phone VALUES ('+558192024396','Gokuzinho');
INSERT INTO phone VALUES ('+558179964184','Luffyzinho');
INSERT INTO phone VALUES ('+558111441468','Ichigozinho');
INSERT INTO phone VALUES ('+558172421724','Natsuzinho');
INSERT INTO phone VALUES ('+558164802709','Gonzinho');
INSERT INTO phone VALUES ('+558130807150','Gintokizinho');
INSERT INTO phone VALUES ('+558123849320','Midoriyazinho');
INSERT INTO phone VALUES ('+558100422296','Seiyazinho');
INSERT INTO phone VALUES ('+558184587668','Gonzinho');
INSERT INTO phone VALUES ('+558184587669','Gonzinho');

--Partidas

INSERT INTO match VALUES(1,'10/10/2019','UA',1);
INSERT INTO match VALUES(2,'10/10/2019','FT',1);
INSERT INTO match VALUES(3,'10/10/2019','UA',1);
INSERT INTO match VALUES(4,'10/10/2019','FT',1);
INSERT INTO match VALUES(5,'10/10/2019','UA',1);

--Jogos
INSERT INTO play VALUES('UA',1,1);
INSERT INTO play VALUES('CDZ',1,1);
INSERT INTO play VALUES('FT',2,1);
INSERT INTO play VALUES('SDS',2,1);
INSERT INTO play VALUES('UA',3,1);
INSERT INTO play VALUES('FT',3,1);
INSERT INTO play VALUES('CDS',4,1);
INSERT INTO play VALUES('FT',4,1);
INSERT INTO play VALUES('UA',5,1);
INSERT INTO play VALUES('FT',5,1);


--Partidas
INSERT INTO match VALUES(1,'05/11/2019','UA',2);
INSERT INTO match VALUES(2,'06/11/2019','OSS',2);
INSERT INTO match VALUES(3,'07/11/2019','UA',2);

--Jogos
INSERT INTO play VALUES('UA',1,2);
INSERT INTO play VALUES('CDZ',1,2);
INSERT INTO play VALUES('OSS',2,2);
INSERT INTO play VALUES('SDS',2,2);
INSERT INTO play VALUES('UA',3,2);
INSERT INTO play VALUES('OSS',3,2);


--Partidas

INSERT INTO match VALUES(1,'06/10/2019','SDS',4);
INSERT INTO match VALUES(2,'06/11/2019','FT',4);
INSERT INTO match VALUES(3,'07//12/2019','UA',4);
INSERT INTO match VALUES(4,'08/12/2019','UA',4);
INSERT INTO match VALUES(5,'11/05/2019','UA',4);

--Jogos
INSERT INTO play VALUES('SDS',1 ,4);
INSERT INTO play VALUES('UA',1 ,4);
INSERT INTO play VALUES('FT',2 ,4);
INSERT INTO play VALUES('OSS',2 ,4);
INSERT INTO play VALUES('UA',3 ,4);
INSERT INTO play VALUES('CDZ',3 ,4);
INSERT INTO play VALUES('UA',4 ,4);
INSERT INTO play VALUES('SDS',4 ,4);
INSERT INTO play VALUES('UA',5 ,4);
INSERT INTO play VALUES('SDS',5 ,4);

--Integrantes

INSERT INTO "integrate" VALUES('Midoriyazinho', 'UA', 1);
INSERT INTO "integrate" VALUES('Natsuzinho', 'FT', 1);
INSERT INTO "integrate" VALUES('Gintokizinho', 'CDS', 1);
INSERT INTO "integrate" VALUES('Seiyazinho', 'CDZ', 1);
INSERT INTO "integrate" VALUES('Ichigozinho', 'SDS', 1);

INSERT INTO "integrate" VALUES('Natsuzinho', 'UA', 2);
INSERT INTO "integrate" VALUES('Midoriyazinho', 'UA', 2);
INSERT INTO "integrate" VALUES('Gokuzinho', 'CDZ', 2);
INSERT INTO "integrate" VALUES('Ichigozinho', 'CDZ', 2);
INSERT INTO "integrate" VALUES('Seiyazinho', 'OSS', 2);
INSERT INTO "integrate" VALUES('Gonzinho', 'OSS', 2);
INSERT INTO "integrate" VALUES('Gintokizinho', 'SDS', 2);
INSERT INTO "integrate" VALUES('Luffyzinho', 'SDS', 2);

INSERT INTO "integrate" VALUES('Luffyzinho', 'SDS', 4);
INSERT INTO "integrate" VALUES('Midoriyazinho', 'UA', 4);
INSERT INTO "integrate" VALUES('Gonzinho', 'FT', 4);
INSERT INTO "integrate" VALUES('Ichigozinho','OSS', 4);
INSERT INTO "integrate" VALUES('Gokuzinho', 'CDZ', 4);

--Follows

INSERT INTO "follow" VALUES('Natsuzinho', 'Gokuzinho');
INSERT INTO "follow" VALUES('Gonzinho', 'Gokuzinho');
INSERT INTO "follow" VALUES('Seiyazinho', 'Gokuzinho');
INSERT INTO "follow" VALUES('Gonzinho', 'Ichigozinho');
INSERT INTO "follow" VALUES('Gokuzinho', 'Seiyazinho');
INSERT INTO "follow" VALUES('Gokuzinho', 'Midoriyazinho');
INSERT INTO "follow" VALUES('Luffyzinho', 'Midoriyazinho');
INSERT INTO "follow" VALUES('Luffyzinho', 'Natsuzinho');
INSERT INTO "follow" VALUES('Gintokizinho', 'Natsuzinho');
INSERT INTO "follow" VALUES('Ichigozinho', 'Seiyazinho');
INSERT INTO "follow" VALUES('Midoriyazinho', 'Luffyzinho');


--Apostador
INSERT INTO "punter" VALUES('Gintokizinho', 600.70);
INSERT INTO "punter" VALUES('Ichigozinho', 902.32);

--Aposta do MVP

INSERT INTO "mvp_bet" VALUES('Gintokizinho','Seiyazinho', 'CDZ', 1);
INSERT INTO "mvp_bet" VALUES('Ichigozinho','Midoriyazinho', 'UA', 1);
INSERT INTO "mvp_bet" VALUES('Gintokizinho','Natsuzinho', 'UA', 2);
INSERT INTO "mvp_bet" VALUES('Ichigozinho','Luffyzinho', 'SDS', 2);
INSERT INTO "mvp_bet" VALUES('Gintokizinho','Luffyzinho', 'SDS', 4);
INSERT INTO "mvp_bet" VALUES('Gintokizinho','Gokuzinho', 'CDZ', 4);

--Moderador
INSERT INTO "moderator" VALUES('Gokuzinho');
INSERT INTO "moderator" VALUES('Luffyzinho');
INSERT INTO "moderator" VALUES('Midoriyazinho');

--Moderação

INSERT INTO "moderate" VALUES('Gokuzinho',1);
INSERT INTO "moderate" VALUES('Luffyzinho',2);
INSERT INTO "moderate" VALUES('Midoriyazinho',4);

--Participantes
INSERT INTO "participant" VALUES('Gokuzinho','Macaco Rabudo');
INSERT INTO "participant" VALUES('Luffyzinho','Borrachudo');
INSERT INTO "participant" VALUES('Ichigozinho','Espadachim Vagante');
INSERT INTO "participant" VALUES('Natsuzinho','Maluco do Fogo');
INSERT INTO "participant" VALUES('Gonzinho','Demonio Ingenuo');
INSERT INTO "participant" VALUES('Seiyazinho','Cavaleiro de Pegasus');
INSERT INTO "participant" VALUES('Gintokizinho','Prata');
INSERT INTO "participant" VALUES('Midoriyazinho','Deku');