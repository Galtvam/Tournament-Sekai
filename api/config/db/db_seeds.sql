--Usuários
INSERT INTO "user" VALUES('gokuzinho', '$2b$12$5/Z17zSeIudGgyVmorWv1.U/iWny6xNVVJWQ8K8xhI2HmJC/nRqIO', 'Son Goku', 'gokuzinho@gmail.com', '02/02/2010','02/02/2010');
INSERT INTO "user" VALUES('luffyzinho', '$2b$12$9rXVhyf8j/DY7nJtw6q7m.f.5HdVX/K1HIz.M/2dzsXlYgWHbXkD2', 'Monkey D. Luffy', 'luffyzinho@gmail.com', '03/03/2003','03/03/20011');
INSERT INTO "user" VALUES('ichigozinho', '$2b$12$hFtPSBOO/uPzf589tLjDFesiVwsREG2SUSdYUxo.Ur6YGZnvwdrle', 'Kurosaki Ichigo', 'ichigozinho@gmail.com', '04/03/2003','04/03/2009');
INSERT INTO "user" VALUES('natsuzinho', '$2b$12$2ItDRmBIXoGAd8M1ch4wLOSAZajqggiQoXJnW2WH3a3/7C6v5pThK', 'Natsu Dragneel', 'natsuzinho@gmail.com', '05/03/2003','05/03/2007' );
INSERT INTO "user" VALUES('gonzinho', '$2b$12$gqKEZJbsFUakdTF9Aa1PoupNK0Z3IJz0w5RpiH7R/iyNybL3L/oM.', 'Gon Freecs', 'gonzinho@gmail.com', '06/03/2003','06/03/2014');
INSERT INTO "user" VALUES('gintokizinho', '$2b$12$pWdfky9WmAaAap168QNBuegj7GJ.w5itRQeL31VW7z/aFdFzNru32','Sakata Gintoki', 'gintokizinho@gmail.com', '07/03/2003','07/03/2012');
INSERT INTO "user" VALUES('midoriyazinho', '$2b$12$ribXuWny2mc.eshfZxkNGO3c2UyFKe31a36iHppEpXp7QeZjtVyn2', 'Izuku Midoriya', 'midoriya@gmail.com', '08/03/2003','08/03/2013');
INSERT INTO "user" Values('seiyazinho', '$2b$12$HGjwThI5Dm5z3Z8fkZoJZe7X5gn/FB8HgU2u3la5/2yuQbxMgnSRq','Seiya de Pegasus', 'seiyazinho@gmail.com', '09/09/2015', '12/12/2012');

--Times

INSERT INTO "team" VALUES ('OSS','Os Super Sayajins','gokuzinho');
INSERT INTO "team" VALUES ('CDS','Cavaleiros do Saara','gintokizinho');
INSERT INTO "team" VALUES ('CDZ','Cavaleiros do Zodiaco','seiyazinho');
INSERT INTO "team" VALUES ('FT','Fairy Tail','natsuzinho');
INSERT INTO "team" VALUES ('UA','Universidade de Herois','midoriyazinho');
INSERT INTO "team" VALUES ('SDS','Shinigamis do Sertão','ichigozinho');

--Torneios

INSERT INTO "tournament" VALUES (DEFAULT, 'Melhor Torneio de YuGiOh','Melhor torneio de YuGiOh da sua rua, vai ser muito top vey','10/10/2019','11/10/2019','gokuzinho','UA');
INSERT INTO "tournament" VALUES (DEFAULT, 'Melhor Torneio de Robblox','O torneio que as crianças vão amar, um jogo que ninguem gosta, só tiram onda por que é um lixo','05/11/2019','07/11/2019','gintokizinho','UA');
INSERT INTO "tournament" VALUES (DEFAULT, 'Torneio Galático','Torneio de batalha entre deuses e grandes guerreiros de todas as galáxias','11/22/2019','11/26/2019','gokuzinho','CDZ');
INSERT INTO "tournament" VALUES (DEFAULT, 'Exame Hunter','Torneio para saber quais serão os próximos seres qualificados para possui a licença Hunter','05/11/2019','10/11/2019','gonzinho','UA');
INSERT INTO "tournament" VALUES (DEFAULT, 'Torneio de Counter Strike','Torneio que reune os melhores times do cenário brasileiro de cs-go, com premiação de incriveis 3 reais','12/17/2019','12/22/2019','natsuzinho');
INSERT INTO "tournament" VALUES (DEFAULT, 'Torneio de Espadas','Torneio que reune todos os espadachins dos mundos, da sociedade das almas, para saber quem é o mais forte','07/02/2020','03/13/2020','ichigozinho');



--Telefones

INSERT INTO "phone" VALUES ('+558192024396','gokuzinho');
INSERT INTO "phone" VALUES ('+558179964184','luffyzinho');
INSERT INTO "phone" VALUES ('+558111441468','ichigozinho');
INSERT INTO "phone" VALUES ('+558172421724','natsuzinho');
INSERT INTO "phone" VALUES ('+558164802709','gonzinho');
INSERT INTO "phone" VALUES ('+558130807150','gintokizinho');
INSERT INTO "phone" VALUES ('+558123849320','midoriyazinho');
INSERT INTO "phone" VALUES ('+558100422296','seiyazinho');
INSERT INTO "phone" VALUES ('+558184587668','gonzinho');
INSERT INTO "phone" VALUES ('+558184587669','gonzinho');

--Partidas

INSERT INTO "match" VALUES(1,'10/10/2019','UA',1);
INSERT INTO "match" VALUES(2,'10/10/2019','FT',1);
INSERT INTO "match" VALUES(3,'10/10/2019','UA',1);
INSERT INTO "match" VALUES(4,'10/10/2019','FT',1);
INSERT INTO "match" VALUES(5,'10/10/2019','UA',1);

--Jogos
INSERT INTO "play" VALUES('UA',1,1);
INSERT INTO "play" VALUES('CDZ',1,1);
INSERT INTO "play" VALUES('FT',2,1);
INSERT INTO "play" VALUES('SDS',2,1);
INSERT INTO "play" VALUES('UA',3,1);
INSERT INTO "play" VALUES('FT',3,1);
INSERT INTO "play" VALUES('CDS',4,1);
INSERT INTO "play" VALUES('FT',4,1);
INSERT INTO "play" VALUES('UA',5,1);
INSERT INTO "play" VALUES('FT',5,1);


--Partidas
INSERT INTO "match" VALUES(1,'05/11/2019','UA',2);
INSERT INTO "match" VALUES(2,'06/11/2019','OSS',2);
INSERT INTO "match" VALUES(3,'07/11/2019','UA',2);

--Jogos
INSERT INTO "play" VALUES('UA',1,2);
INSERT INTO "play" VALUES('CDZ',1,2);
INSERT INTO "play" VALUES('OSS',2,2);
INSERT INTO "play" VALUES('SDS',2,2);
INSERT INTO "play" VALUES('UA',3,2);
INSERT INTO "play" VALUES('OSS',3,2);


--Partidas

INSERT INTO "match" VALUES(1,'06/10/2019','SDS',4);
INSERT INTO "match" VALUES(2,'06/11/2019','FT',4);
INSERT INTO "match" VALUES(3,'07//12/2019','UA',4);
INSERT INTO "match" VALUES(4,'08/12/2019','UA',4);
INSERT INTO "match" VALUES(5,'11/05/2019','UA',4);

--Jogos
INSERT INTO "play" VALUES('SDS',1 ,4);
INSERT INTO "play" VALUES('UA',1 ,4);
INSERT INTO "play" VALUES('FT',2 ,4);
INSERT INTO "play" VALUES('OSS',2 ,4);
INSERT INTO "play" VALUES('UA',3 ,4);
INSERT INTO "play" VALUES('CDZ',3 ,4);
INSERT INTO "play" VALUES('UA',4 ,4);
INSERT INTO "play" VALUES('SDS',4 ,4);
INSERT INTO "play" VALUES('UA',5 ,4);
INSERT INTO "play" VALUES('SDS',5 ,4);

--Membros do time

INSERT INTO "team_member" VALUES('midoriyazinho', 'UA');
INSERT INTO "team_member" VALUES('natsuzinho', 'FT');
INSERT INTO "team_member" VALUES('gintokizinho', 'CDS');
INSERT INTO "team_member" VALUES('seiyazinho', 'CDZ');
INSERT INTO "team_member" VALUES('ichigozinho', 'SDS');
INSERT INTO "team_member" VALUES('gonzinho', 'OSS');
INSERT INTO "team_member" VALUES('luffyzinho', 'SDS');
INSERT INTO "team_member" VALUES('gokuzinho', 'CDZ');


--Integrantes

INSERT INTO "integrate" VALUES('midoriyazinho', 'UA', 1);
INSERT INTO "integrate" VALUES('natsuzinho', 'FT', 1);
INSERT INTO "integrate" VALUES('gintokizinho', 'CDS', 1);
INSERT INTO "integrate" VALUES('seiyazinho', 'CDZ', 1);
INSERT INTO "integrate" VALUES('ichigozinho', 'SDS', 1);

INSERT INTO "integrate" VALUES('natsuzinho', 'UA', 2);
INSERT INTO "integrate" VALUES('midoriyazinho', 'UA', 2);
INSERT INTO "integrate" VALUES('gokuzinho', 'CDZ', 2);
INSERT INTO "integrate" VALUES('ichigozinho', 'CDZ', 2);
INSERT INTO "integrate" VALUES('seiyazinho', 'OSS', 2);
INSERT INTO "integrate" VALUES('gonzinho', 'OSS', 2);
INSERT INTO "integrate" VALUES('gintokizinho', 'SDS', 2);
INSERT INTO "integrate" VALUES('luffyzinho', 'SDS', 2);

INSERT INTO "integrate" VALUES('luffyzinho', 'SDS', 4);
INSERT INTO "integrate" VALUES('midoriyazinho', 'UA', 4);
INSERT INTO "integrate" VALUES('gonzinho', 'FT', 4);
INSERT INTO "integrate" VALUES('ichigozinho','OSS', 4);
INSERT INTO "integrate" VALUES('gokuzinho', 'CDZ', 4);

--Follows

INSERT INTO "follow" VALUES('natsuzinho', 'gokuzinho');
INSERT INTO "follow" VALUES('gonzinho', 'gokuzinho');
INSERT INTO "follow" VALUES('seiyazinho', 'gokuzinho');
INSERT INTO "follow" VALUES('gonzinho', 'ichigozinho');
INSERT INTO "follow" VALUES('gokuzinho', 'seiyazinho');
INSERT INTO "follow" VALUES('gokuzinho', 'midoriyazinho');
INSERT INTO "follow" VALUES('luffyzinho', 'midoriyazinho');
INSERT INTO "follow" VALUES('luffyzinho', 'natsuzinho');
INSERT INTO "follow" VALUES('gintokizinho', 'natsuzinho');
INSERT INTO "follow" VALUES('ichigozinho', 'seiyazinho');
INSERT INTO "follow" VALUES('midoriyazinho', 'luffyzinho');


--Apostador
INSERT INTO "punter" VALUES('gintokizinho', 600.70);
INSERT INTO "punter" VALUES('ichigozinho', 902.32);

--Aposta do MVP

INSERT INTO "mvp_bet" VALUES('gintokizinho','seiyazinho', 'CDZ', 1);
INSERT INTO "mvp_bet" VALUES('ichigozinho','midoriyazinho', 'UA', 1);
INSERT INTO "mvp_bet" VALUES('gintokizinho','natsuzinho', 'UA', 2);
INSERT INTO "mvp_bet" VALUES('ichigozinho','luffyzinho', 'SDS', 2);
INSERT INTO "mvp_bet" VALUES('gintokizinho','luffyzinho', 'SDS', 4);
INSERT INTO "mvp_bet" VALUES('gintokizinho','gokuzinho', 'CDZ', 4);

--Moderador
INSERT INTO "moderator" VALUES('gokuzinho');
INSERT INTO "moderator" VALUES('luffyzinho');
INSERT INTO "moderator" VALUES('midoriyazinho');

--Moderação

INSERT INTO "moderate" VALUES('gokuzinho',1);
INSERT INTO "moderate" VALUES('luffyzinho',2);
INSERT INTO "moderate" VALUES('midoriyazinho',4);

--Participantes
INSERT INTO "participant" VALUES('gokuzinho','Macaco Rabudo');
INSERT INTO "participant" VALUES('luffyzinho','Borrachudo');
INSERT INTO "participant" VALUES('ichigozinho','Espadachim Vagante');
INSERT INTO "participant" VALUES('natsuzinho','Maluco do Fogo');
INSERT INTO "participant" VALUES('gonzinho','Demonio Ingenuo');
INSERT INTO "participant" VALUES('seiyazinho','Cavaleiro de Pegasus');
INSERT INTO "participant" VALUES('gintokizinho','Prata');
INSERT INTO "participant" VALUES('midoriyazinho','Deku');