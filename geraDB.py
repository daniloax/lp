import sqlite3
conexão = sqlite3.connect("geraDB.db")
cursor = conexão.cursor()
cursor.execute('''
    create table usuarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE, senha TEXT)
    ''')
cursor.execute('''
    insert into usuarios (nome, senha) values(?, ?)
    ''', ("Orlando", "ojfs1958"))
cursor.execute('''
    create table atividades (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT, atividade TEXT, data DATE)
    ''')
cursor.execute('''
    insert into atividades (nome,atividade, data) values(?,?,?)
    ''', ("Orlando","Teste de uso","2016-07-02 18:21"))
conexão.commit()
cursor.close()
conexão.close()
