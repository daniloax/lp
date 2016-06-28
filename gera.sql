CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL);
	
CREATE TABLE activity (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	date INTEGER NOT NULL,
	hour INTEGER NOT NULL,
	fk_user_id INTEGER NOT NULL,
	FOREIGN KEY(fk_user_id) REFERENCES user(id));
	
CREATE TABLE alarm (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	active INTEGER NOT NULL,
	repeat INTEGER NOT NULL,
	reminder INTEGER NOT NULL,
	fk_activity_id INTEGER NOT NULL,
	FOREIGN KEY(fk_activity_id) REFERENCES activity(id));

INSERT INTO user (name, email, password)
VALUES 
("Geraldino", geraldino@unb.br, 123),
("Orlando", "orlando@unb.br", 123),
("Danilo Fukuda", "danilo_fukuda@unb.br", 123),
("Felipe", "felipe@unb.br", 123),
("Danilo Alves", "danilo_alves@unb.br", 123)

INSERT INTO activity (title, description, date, hour, fk_user_id) VALUES 
("Reunião", "Reunião de trabalho", "26/06/2016", "16:20", 1),
("Aula", "Aula de francês", "26/06/2016", "17:20", 1),,
("Academia", "Musculação", "26/06/2016", "18:20", 1),
("Academia", "Natação", "26/06/2016", "19:20", 1),
("Reunião", "Reunião de trabalho", "26/06/2016", "16:20", 2),
("Aula", "Aula de francês", "26/06/2016", "17:20", 2),,
("Academia", "Musculação", "26/06/2016", "18:20", 2),
("Academia", "Natação", "26/06/2016", "19:20", 2),
("Reunião", "Reunião de trabalho", "26/06/2016", "16:20", 3),
("Aula", "Aula de francês", "26/06/2016", "17:20", 3),,
("Academia", "Musculação", "26/06/2016", "18:20", 3),
("Academia", "Natação", "26/06/2016", "19:20", 3),
("Reunião", "Reunião de trabalho", "26/06/2016", "16:20", 4),
("Aula", "Aula de francês", "26/06/2016", "17:20", 4),
("Academia", "Musculação", "26/06/2016", "18:20", 4),
("Academia", "Natação", "26/06/2016", "19:20", 4),
("Reunião", "Reunião de trabalho", "26/06/2016", "16:20", 5),
("Aula", "Aula de francês", "26/06/2016", "17:20", 5),,
("Academia", "Musculação", "26/06/2016", "18:20", 5),
("Academia", "Natação", "26/06/2016", "19:20", 5)

INSERT INTO alarm (reminder, interval, repeat, active, fk_activity_id) VALUES
("2016-06", "00:30", 1, 1, 5),
("2016-06", "01:00", 1, 0, 5),
("2016-07", "02:00", 1, 1, 6),
("2016-07", "01:00", 1, 0, 6)
