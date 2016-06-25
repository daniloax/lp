import sqlite3
conexao = sqlite3.connect("geraDB.db")
cursor = conexao.cursor()

#dados do usuario
dados=("Felipe","1234567")
cursor.execute('''
    insert into usuarios (nome,senha) values (?,?)
    ''',dados)
conexao.commit()

#atividade
dados=("Felipe","Teste para Felipe","2016-07-07 22:30")
cursor.execute('''
    insert into usuario (nome,atividade,data) values (?,?,?)
    ''',dados)
conexao.commit()

cursor.execute('''
    select * from usuarios,
    usuario where usuarios.nome=usuario.nome
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    print("Usuário Id: %d\nNome: %s\nSenha: %s\nAtividade Id: %d\nUsuário Id: %s\nAtividade: %s\nData: %s" % (registro))
    print(registro)
cursor.close()
conexao.close()
