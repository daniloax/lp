import sqlite3


class Atividade:
    def __init__(self, usuario, titulo, descricao, dataehora, conclusao):
        self.usuario = usuario
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.conclusao = conclusao
        self.numero=numero

def read():
            conn = sqlite3.connect('atividades.db')
            cursor = conn.cursor()
            #lendo os dados
            cursor.execute("""
            SELECT * FROM atividades;
            """)
            for linha in cursor.fetchall():
                print(linha)
            conn.close()    
def switch():
    while True:
        print("______MENU______")
        print("[1] = criar atividade")
        print("[2] = atualizar atividade")
        print("[3] = apagar atividade")
        opcao = input("[4] = Sair do menu\n")
        if opcao == '1':
            ##Troque loguin pela variável usada para guardar o nome
            usuario = 'loguin'
            titulo = input("digite o título da atividade: ")
            print(titulo)
            descricao = input("digite a descrição da atividade: ")
            print(descricao)
            data = input("digite a data da atividade: ")
            print(data)
            hora = input("digite a hora da atividade: ")
            print(hora)
            conclusao = input("digite a conclusao da atividade:")
            print(conclusao)
            numero = input("digite uma ID da atividade:")
            print(numero)
            lista = [(usuario, titulo, descricao, data, hora, conclusao,numero)]
            print(lista)
            ##INSERIR NO REGISTRO
            conn = sqlite3.connect('atividades.db')
            cursor = conn.cursor()
            cursor.executemany("""
			INSERT INTO atividades (usuario,titulo,descricao,data,hora,conclusao,numero)
			VALUES (?,?,?,?,?,?,?)
			""", lista)

            conn.commit()

            print('Dados inseridos com sucesso.')

            conn.close()

        elif opcao == '2':
            read()
            ##Troque loguin pela variável usada para guardar o nome
            usuario='loguin'
            print("Atualizar atividade")
            numero = input("digite a ID da atividade a ser atualizada:")
            print(numero)
            titulo = input("digite o novo título da atividade: ")
            print(titulo)
            descricao = input("digite a nova descrição da atividade: ")
            print(descricao)
            data = input("digite a nova data da atividade: ")
            print(data)
            hora = input("digite a nova hora da atividade: ")
            print(hora)
            conclusao = input("digite a nova conclusao da atividade:")
            print(conclusao)
            lista = [(usuario, titulo, descricao, data, hora, conclusao,numero)]
            print(lista)

            ##ATUALIZAR REGISTRO
            conn = sqlite3.connect('atividades.db')
            cursor = conn.cursor()
            cursor.execute("""

            UPDATE atividades
            
            SET usuario=?,titulo=?,descricao=?,data=?,hora=?,conclusao=?
            WHERE numero=?
            """,(usuario,titulo,descricao,data,hora,conclusao,numero))
            
            conn.commit()
            print('Dados atualizados com sucesso.')
            conn.close()
            
        elif opcao == '3':
            read()
        
            print("apague atividade")
            numero = input("digite a ID da atividade a ser apagada:")
            print(numero)
            ##EXCLUIR REGISTRO
            conn = sqlite3.connect('atividades.db')
            cursor = conn.cursor()

            cursor.execute("""
            DELETE FROM atividades
            WHERE numero = ?
            """, (numero,))

            conn.commit()
            print('Registro excluido com sucesso.')

            conn.close()
            
        elif opcao == '4':
            print("Saiu com sucesso!")
            break

        else:
            print("ERROR")


switch()
