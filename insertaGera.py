import sqlite3
conexão = sqlite3.connect("geraDB.db")
cursor = conexão.cursor()

#dados do usuário
dados=("Felipe","1234567")
cursor.execute('''
    insert into usuarios (nome,senha) values (?,?)
    ''',dados)
conexão.commit()

#atividade
dados=("Felipe","Teste para Felipe","2016-07-07 22:30")
cursor.execute('''
    insert into atividades (nome,atividade,data) values (?,?,?)
    ''',dados)
conexão.commit()

cursor.execute('''
    select * from usuarios,
    atividades where usuarios.nome=atividades.nome
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    print("Usuário Id: %d\nNome: %s\nSenha: %s\nAtividade Id: %d\nUsuário Id: %s\nAtividade: %s\nData: %s" % (registro))
    print(registro)
cursor.close()
conexão.close()
