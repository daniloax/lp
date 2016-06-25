import sqlite3
conexao = sqlite3.connect("geraDB.db")
cursor = conexao.cursor()

#deletar usuario

cursor.execute('''
    delete from usuarios where nome=?
    ''',("Felipe",))
conexao.commit()

#deletar as atividades do usuario
cursor.execute('''
    delete from atividades where nome=?
    ''',("Felipe",))
conexao.commit()

#deletar uma determinada atividade do usuario
cursor.execute('''
    delete from atividades where nome=? and data=?
    ''',("Felipe","2016-07-02 18:22"))
conexao.commit()

cursor.execute('''
    select * from usuarios,
    atividades where usuarios.nome=atividades.nome
    ''')
resultado=cursor.fetchall()
for registro in resultado:
    print("usuario Id: %d\nNome: %s\nSenha: %s\nAtividade Id: %d\nusuario: %s\nAtividade: %s\nData: %s" % (registro))
    print(registro)
cursor.close()
conexao.close()
