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

def read(identification):
            conn = sqlite3.connect('geraDB.db')
            cursor = conn.cursor()
            #lendo os dados
            cursor.execute("""
            SELECT id,titulo,descricao,data,hora,conclusao FROM atividades
            WHERE idusuario=?
            """, (identification,))
            for linha in cursor.fetchall():
                print(linha)
            conn.close()    

def switch(logado,identification):
	if logado == 2:
		while True:
			print("______MENU______")
			print("[1] = Criar atividade")
			print("[2] = Editar atividade")
			print("[3] = Apagar atividade")
			opcao = input("[4] = Sair do menu\n")
			if opcao == '1':
				titulo = input("Digite o título da atividade: ")
				descricao = input("Digite a descrição da atividade: ")
				data = input("Digite a data da atividade: ")
				hora = input("Digite a hora da atividade: ")
				conclusao = input("Digite a conclusao da atividade:")

				lista = [(identification, titulo, descricao, data, hora, conclusao)]

				conn = sqlite3.connect('geraDB.db')
				cursor = conn.cursor()
				cursor.executemany("""
				INSERT INTO atividades (idusuario,titulo,descricao,data,hora,conclusao)
				VALUES (?,?,?,?,?,?)
				""", lista)

				conn.commit()

				print('\nDados inseridos com sucesso.\n')

				conn.close()

			elif opcao == '2':
				read(identification)
				print("\n__Atualizando atividade__")
				numero = input("Digite o número da atividade que deseja editar: ")


				conn = sqlite3.connect('geraDB.db', timeout=10)
				cursor = conn.cursor()

				cursor.execute("""
				SELECT id,idusuario FROM atividades WHERE id=? AND idusuario=?"""
				, (numero,identification))

				j = 0
				for test in cursor.fetchall():
					print ("\nAtividade encontrada!\n")
					j = 1
				if j == 0:
					print ("\nNúmero da atividade não encontrado\n")
					switch(2,identification)
				else:
					titulo = input("Digite o novo título da atividade: ")
					descricao = input("Digite a nova descrição da atividade: ")
					data = input("Digite a nova data da atividade: ")
					hora = input("Digite a nova hora da atividade: ")
					conclusao = input("Digite a nova conclusao da atividade: ")
					lista = [(numero, titulo, descricao, data, hora, conclusao)]
					print("\n")
					print(lista)

					##ATUALIZAR REGISTRO
					conn = sqlite3.connect('geraDB.db')
					cursor = conn.cursor()





					cursor.execute("""
					
					UPDATE atividades
					SET titulo=?,descricao=?,data=?,hora=?,conclusao=?
					WHERE id=?
					""",(titulo,descricao,data,hora,conclusao,numero))

					conn.commit()
					print('Dados atualizados com sucesso.\n')
				conn.close()
	            
			elif opcao == '3':
				read(identification)
	        
				print("\n__Apagando atividade__")
				numero = input("Digite a ID da atividade a ser apagada: ")
				print(numero)
				##EXCLUIR REGISTRO
				conn = sqlite3.connect('geraDB.db')
				cursor = conn.cursor()


				cursor.execute("""
				SELECT id,idusuario FROM atividades WHERE id=? AND idusuario=?"""
				, (numero,identification))

				j = 0
				for test in cursor.fetchall():
					print ("\nAtividade encontrada!")
					j = 1
				if j == 0:
					print ("\nNúmero da atividade não encontrado\n")
					switch(2,identification)
				else:
					cursor.execute("""
					DELETE FROM atividades
					WHERE id = ?
					""", (numero,))

					conn.commit()
					print('Registro excluido com sucesso.\n')

					conn.close()

			elif opcao == '4':
				print("Saiu com sucesso!\n")
				login()

			else:
				print("Insira uma opcao correta!\n")
				switch(0,identification)
switch(0,0)

def login():
	i = 0
	while True:
		print("\n[1] = cadastro de usuario")
		print("[2] = logar no sistema")
		value = input("[3] = Sair\n")
		if value == '1':
			email = input("Digite o seu email: ")
			password = input("Digite a sua senha: ")
			lista = [(email,password)]

			conn = sqlite3.connect('geraDB.db', timeout=10)
			cursor = conn.cursor()

			cursor.execute("""
			SELECT email FROM usuarios WHERE email=?"""
			, (email,))

			for test in cursor.fetchall():
				if (email,) == test:
					print ("\nEste email ja possui cadastro!\n")
					i = 1
					login()
			if i == 0:
				cursor.executemany("""
				INSERT INTO usuarios (email,senha)
				VALUES (?,?)
				""", lista)
				conn.commit()
				print("\nUsuario cadastrado!\n")
			conn.close()
		elif value == '2':
			email = input("\nDigite o seu email: ")
			password = input("Digite a sua senha: ")
			lista = [(email,password)]

			conn = sqlite3.connect('geraDB.db', timeout=10)
			cursor = conn.cursor()

			cursor.execute("""
			SELECT email FROM usuarios WHERE email=?"""
			, (email,))

			for test in cursor.fetchall():
				if (email,) == test:
					print ("\nUsuario verificado!")
					i = 1
			if i == 0:
				print ("\nUsuario nao cadastrado!\n")
				login()
			elif i == 1:
				cursor.execute("""
				SELECT senha FROM usuarios WHERE senha=?"""
				, (password,))

				for test in cursor.fetchall():
					if (password,) == test:
						print ("Seja bem vindo!\n")
						i = 2

						cursor.execute("""
						SELECT id FROM usuarios WHERE email=? AND senha=?"""
						, (email,password))

						for test in cursor.fetchall():
							(identify,) = test
						switch(i,identify)
						login()
				if i != 2:
					print("Senha incorreta!\n")
					login()
			conn.close()
		elif value == '3':
			quit()

		else:
			print("Insira uma opcao correta!\n")
login()
