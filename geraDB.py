import sqlite3
conexao = sqlite3.connect("geraDB.db")
cursor = conexao.cursor()
cursor.execute('''
    create table user(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE, password TEXT)
    ''')
cursor.execute('''
    insert into user (name, password) values(?, ?)
    ''', ("Orlando", "ojfs1958"))
cursor.execute('''
    create table activity (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT, description TEXT, date DATE)
    ''')
cursor.execute('''
    insert into activity (title,description, date) values(?,?,?)
    ''', ("teste","Teste de uso","2016-07-02 18:21"))
conexao.commit()
cursor.close()
conexao.close()
