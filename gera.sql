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

INSERT INTO activity (title, description, date, hour, fk_user_id)
VALUES ("atividade1", "atividade1", "2016-06-26", "14:20", 1)
