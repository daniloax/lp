import sqlite3
conexão = sqlite3.connect("geraDB.db")
cursor = conexão.cursor()

#deletar usuário

cursor.execute('''
    delete from usuarios where nome=?
    ''',("Felipe",))
conexão.commit()

#deletar as atividades do usuário
cursor.execute('''
    delete from atividades where nome=?
    ''',("Felipe",))
conexão.commit()

#deletar uma determinada atividade do usuário
cursor.execute('''
    delete from atividades where nome=? and data=?
    ''',("Felipe","2016-07-02 18:22"))
conexão.commit()

cursor.execute('''
    select * from usuarios,
    atividades where usuarios.nome=atividades.nome
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    print("Usuário Id: %d\nNome: %s\nSenha: %s\nAtividade Id: %d\nUsuário: %s\nAtividade: %s\nData: %s" % (registro))
    print(registro)
cursor.close()
conexão.close()
