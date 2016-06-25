import sqlite3
conexao = sqlite3.connect("geraDB.db")
cursor = conexao.cursor()
cursor.execute('''
    select * from usuarios,
    usuario where usuarios.nome=usuario.nome
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    #print("usuario Id: %d\nNome: %s\nSenha: %s\nAtividade Id: %d\nusuario: %s\nAtividade: %s\nData: %s" % (registro))
    print(registro)

cursor.execute('''
    select  id,nome,atividade,date(data),time(data),datetime(data)
    from usuario
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    #print("Id: %d\nNome: %s\nAtividade: %s\ndata(data): %s\ntime(data): %s\ndatatime(data): %s" % (registro))
    print(registro)
cursor.close()
conexao.close()
