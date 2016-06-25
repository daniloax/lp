import sqlite3
conexão = sqlite3.connect("geraDB.db")
cursor = conexão.cursor()
cursor.execute('''
    update atividades set data=? where nome=?
    ''',("2016-07-02 18:21","Orlando"))
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
