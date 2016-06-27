import sqlite3
import alarme

class Atividade:
    def __init__(self, usuario, titulo, descricao, dataehora):
        self.usuario = usuario
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.numero=numero

def read(identification):
            conn = sqlite3.connect('geraDB.db')
            cursor = conn.cursor()

            cursor.execute("""
            SELECT id,titulo,descricao,dia,mes,ano,hora,minuto FROM atividades
            WHERE idusuario=?
            """, (identification,))
            i=0
            for linha in cursor.fetchall():
                print(linha[0], linha[1], linha[2],
                linha[3],"/",linha[4],"/",linha[5],"as", linha[6],":",linha[7])
                i=1
            if i == 0:
            	print ("Nenhuma atividade encontrada!")
            conn.close()

def switch(logado,identification):
	if logado == 2:
		while True:
			print("\n______MENU______")
			print("[1] = Ver atividades")
			print("[2] = Criar atividade")
			print("[3] = Habilitar alarme")
			print("[4] = Editar atividade")
			print("[5] = Apagar atividade")
			print("[6] = Ver as horas")
			opcao = input("[7] = Sair do menu\n")
			if opcao == '1':
				read(identification)
			elif opcao == '2':
				titulo = input("Digite o título da atividade: ")
				descricao = input("Digite a descrição da atividade: ")
				dia = input("Digite o dia da atividade: ")
				mes = input("Digite o mes da atividade: ")
				ano = input("Digite o ano da atividade: ")
				hora = input("Digite a hora da atividade: ")
				minuto = input("Digite o minuto: ")
				lista = [(identification, titulo, descricao, ano, mes, dia, hora, minuto, 0)]

				conn = sqlite3.connect('geraDB.db')
				cursor = conn.cursor()
				cursor.executemany("""
				INSERT INTO atividades (idusuario,titulo,descricao,ano,mes,dia,hora,minuto,alarme)
				VALUES (?,?,?,?,?,?,?,?,?)
				""", lista)

				conn.commit()
				print('\nDados inseridos com sucesso.')
				conn.close()

			elif opcao == '3':
				read(identification)
				numero = input("\nDigite o numero da atividade: ")

				conn = sqlite3.connect('geraDB.db', timeout=10)
				cursor = conn.cursor()

				cursor.execute("""
				SELECT id,idusuario FROM atividades WHERE id=? AND idusuario=?"""
				, (numero,identification))

				j = 0
				for test in cursor.fetchall():
					print ("\nAtividade encontrada!")
					j = 1
				if j == 0:
					print ("\nNumero da atividade não encontrado")
					switch(2,identification)
				else:
					cursor.execute("""
					SELECT ano,mes,dia,hora,minuto FROM atividades WHERE id=? AND idusuario=?"""
					, (numero,identification))

					for test in cursor.fetchall():
						print("Alarme ativado.\n")
						alarme.Clock().set_alarm(test[0],test[1],test[2],test[3],test[4])
						
					cursor.execute("""
					UPDATE atividades SET alarme=1 WHERE id=?;""",(numero,))

					conn.commit()
				conn.close()

			elif opcao == '4':
				read(identification)
				numero = input("\nDigite o numero da atividade que deseja editar: ")

				conn = sqlite3.connect('geraDB.db', timeout=10)
				cursor = conn.cursor()

				cursor.execute("""
				SELECT id,idusuario FROM atividades WHERE id=? AND idusuario=?"""
				, (numero,identification))

				j = 0
				for test in cursor.fetchall():
					print ("\nAtividade encontrada!")
					j = 1
				if j == 0:
					print ("\nNumero da atividade não encontrado")
					switch(2,identification)
				else:
					titulo = input("\nDigite o novo título da atividade: ")
					descricao = input("Digite a nova descrição da atividade: ")
					dia = input("Digite o novo dia da atividade: ")
					mes = input("Digite o novo mes da atividade: ")
					ano = input("Digite o novo ano da atividade: ")
					hora = input("Digite a nova hora da atividade: ")
					minuto = input("Digite o novo minuto: ")
					lista = [(numero, titulo, descricao, ano, mes, dia, hora, minuto)]

					conn = sqlite3.connect('geraDB.db')
					cursor = conn.cursor()

					cursor.execute("""
					UPDATE atividades
					SET titulo=?,descricao=?,ano=?,mes=?,dia=?,hora=?,minuto=?
					WHERE id=?
					""",(titulo,descricao,ano,mes,dia,hora,minuto,numero))
					conn.commit()

					cursor.execute("""
					UPDATE atividades SET alarme=0 WHERE id=?;""",(numero,))
					conn.commit()

					print('\nDados atualizados com sucesso.')
				conn.close()
	            
			elif opcao == '5':
				read(identification)
				numero = input("\nDigite a ID da atividade a ser apagada: ")

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
					print ("\nNumero da atividade não encontrado")
					switch(2,identification)
				else:
					cursor.execute("""
					DELETE FROM atividades
					WHERE id = ?
					""", (numero,))

					conn.commit()
					print('Registro excluido com sucesso.')

					conn.close()

			elif opcao == '6':
				alarme.Clock().run()
			elif opcao == '7':
				print("Saiu com sucesso!")
				login()

			else:
				print("Insira uma opcao correta!")
				switch(0,identification)
switch(0,0)

def login():
	i = 0
	while True:
		print("\n[1] = cadastro de usuario")
		print("[2] = logar no sistema")
		value = input("[3] = Sair\n")
		if value == '1':
			nome = input("Digite o seu nome: ")
			email = input("Digite o seu email: ")
			password = input("Digite a sua senha: ")
			lista = [(nome,email,password)]

			conn = sqlite3.connect('geraDB.db', timeout=10)
			cursor = conn.cursor()

			cursor.execute("""
			SELECT email FROM usuarios WHERE email=?"""
			, (email,))

			for test in cursor.fetchall():
				if (email,) == test:
					print ("\nEste email ja possui cadastro!")
					i = 1
					login()
			if i == 0:
				cursor.executemany("""
				INSERT INTO usuarios (nome,email,senha)
				VALUES (?,?,?)
				""", lista)
				conn.commit()
				print("\nUsuario cadastrado!")
			conn.close()
		elif value == '2':
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
					print ("\nUsuario verificado!")
					i = 1
			if i == 0:
				print ("\nUsuario nao cadastrado!")
				login()
			elif i == 1:
				cursor.execute("""
				SELECT senha FROM usuarios WHERE email=?"""
				, (email,))

				for test in cursor.fetchall():
					if (password,) == test:
						print ("Seja bem vindo!")
						i = 2

						cursor.execute("""
						SELECT id FROM usuarios WHERE email=? AND senha=?"""
						, (email,password))

						for test in cursor.fetchall():
							(identify,) = test
						switch(i,identify)
						login()
				if i != 2:
					print("Senha incorreta!")
					login()
			conn.close()
		elif value == '3':
			quit()

		else:
			print("Insira uma opcao correta!")
login()
