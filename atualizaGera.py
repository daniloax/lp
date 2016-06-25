import sqlite3
conexao = sqlite3.connect("geraDB.db")
cursor = conexao.cursor()
cursor.execute('''
    update atividades set data=? where nome=?
    ''',("2016-07-02 18:21","Orlando"))
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
