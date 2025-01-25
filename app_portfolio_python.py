from colorama import Fore, Back, Style, init #Importa uma biblioteca para cores do terminal. Instalação: " pip install colorama "
from googletrans import Translator #Esta biblioteca usada para traduzir mensagens. Instalação: " pip install googletrans==4.0.0-rc1 "
from argon2 import PasswordHasher #Argon2 usado para criptografar a senha para manter o sistema mais seguro. Instalação " pip install argon2-cffi "
from datetime import datetime #biblioteca para pegar data e tempo em tempo real, e validações
import mysql.connector #Importa a biclioteca do MYSQL. Instalação: " pip install mysql-connector-python "
from time import sleep #biblioteca time usada para dar uma curta pausa no sistema
import keyboard #A biblioteca keyboard em Python para capturar e simular eventos de teclado. Instalação: " pip install keyboard "
import os #A biblioteca os em Python fornece uma maneira de interagir com o sistema operacional.
from email_validator import validate_email, EmailNotValidError #Esta biblioteca foi usada para validação de emails. Instalação: " pip install email-validator "
import re #A biblioteca re em Python foi usada para trabalhar com expressões regulares.

# Configuração do Argon2
ph = PasswordHasher()

#Para usar o banco de dados MySQL com Python, você precisa de algumas ferramentas e bibliotecas.
#Passos:
#Instalar o MySQL Server (caso não tenha instalado): Você pode fazer o download e instalar o MySQL Server no seu computador. Acesse https://dev.mysql.com/downloads/installer/.
#Instalar a biblioteca mysql-connector-python: Essa biblioteca vai permitir que você se conecte ao MySQL diretamente do Python. Para instalar, basta rodar o seguinte comando no terminal: pip install mysql-connector-python

class Unifecaf:
    # Se conecta ao MySQL
    con = mysql.connector.connect(
        host = "localhost", #Coloque seu hostname aqui
        user = "root", #Usuario do seu banco de dados
        password = "", #Senha do seu banco de dados (caso não tenha deixe o campo vazio)
        database = "" #Aqui vai o nome do banco de dados criado
    )
    
    # Tela de Login incial.
    def login(self):
        while True:
            self.header_terminal("Sistema UniFECAF")
            print("\n1 - Login\n2 - Ainda não tem uma conta? Se cadastre!\n0 - Sair")
            option = self.validate(f"\n{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}", 'digit').strip()
            sleep(1)
            if option == "1": #opcao 1 para abrir painel de logar como aluno
                while True:
                    self.header_terminal("LOGIN")
                    self.username = input("\nUsuário: ").strip().lower()
                    cursor = self.con.cursor()
                    cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{self.username}'")
                    findUser = cursor.fetchone()
                    if findUser == None:
                        self.message_error("Usuário incorreto.")
                        continue
                    else:
                        while True:
                            self.password = input("\nSenha: ").strip()
                            searchPasswordHash = findUser[8]
                            try:
                                if ph.verify(searchPasswordHash, self.password) and findUser[10] == 0:
                                    while True:
                                        self.header_terminal(f"Seja bem vindo {findUser[2].title()}!")
                                        print(f"\n1 - Se inscrever em um evento")
                                        print("2 - Listar eventos")
                                        print("3 - Procurar por eventos")
                                        print("4 - Voltar")
                                        print("0 - Sair")
                                        option = self.validate(f"\n{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}", 'digit').strip()
                                        if option == "1":
                                            self.event_register()
                                        elif option == "2":
                                            self.show_all_events()
                                        elif option == "3":
                                            self.search_event()
                                        elif option == "4":
                                            self.login()
                                            sleep(1)
                                        elif option == "0":
                                            print("Saindo...")
                                            sleep(1)
                                            exit()
                                elif ph.verify(searchPasswordHash, self.password) and findUser[10] == 1:
                                        self.header_terminal(f" bem vindo {findUser[2].title()}!")
                                        while True:
                                            print("\n1 - Cadastrar Evento\n2 - Atualizar Evento\n3 - Listar Eventos\n4 - Procurar por Eventos\n5 - Listar Inscritos\n6 - Excluir Eventos\n7 - Voltar\n0 - Sair")
                                            option = self.validate(f"\n{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}", 'digit').strip()
                                            if option == "1": #opcao que chama funcao cadastrar evento
                                                self.create_event()
                                            elif option == "2": #opcao que chama funcao para atualizar eventos
                                                self.update_event()
                                            elif option == "3":#opcao que chama funcao listar evento
                                                self.show_all_events()
                                            elif option == "4":
                                                self.search_event()
                                            elif option == "5": #opcao que chama funcao listar inscritos
                                                self.registered_students()
                                            elif option == "6": #opcao que chama funcao para excluir eventos
                                                self.drop_event()
                                            elif option == "7":
                                                self.login()
                                                sleep(1)
                                            elif option == "0": #opcao que chama funcao para sair do sistema
                                                print("Saindo...")
                                                sleep(1)
                                                self.clear()
                                                exit()
                                elif ph.verify(searchPasswordHash, self.password) and findUser[10] == 2:
                                    self.header_terminal(f"Seja bem vindo {findUser[2].title()}!")
                                    self.header_terminal("ADMIN")
                                    while True:
                                        print("\n1 - Cadastrar Evento\n2 - Atualizar Evento\n3 - Listar Eventos\n4 - Procurar por Eventos\n5 - Listar Inscritos\n6 - Excluir Eventos\n7 - Alterar Permissão\n8 - Voltar\n0 - Sair")
                                        option = self.validate(f"\n{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}", 'digit').strip()
                                        if option == "1": #opcao que chama funcao cadastrar evento
                                            self.create_event()
                                        elif option == "2": #opcao que chama funcao para atualizar eventos
                                            self.update_event()
                                        elif option == "3":#opcao que chama funcao listar evento
                                            self.show_all_events()
                                        elif option == "4":
                                            self.search_event()
                                        elif option == "5": #opcao que chama funcao listar inscritos
                                            self.registered_students()
                                        elif option == "6": #opcao que chama funcao para excluir eventos
                                            self.drop_event()
                                        elif option == "7":
                                            self.alter_permission()
                                        elif option == "8":
                                            System.login()
                                        elif option == "0": #opcao que chama funcao para sair do sistema
                                            print("Saindo...")
                                            sleep(1)
                                            self.clear()
                                            exit()    
                            except Exception:
                                self.message_error("Senha incorreta.")
                                continue
            elif option == "2": # opcao 2 cadastrar conta.
                self.create_account()
            elif option == "0":
                print("Saindo...")
                sleep(1)
                self.clear()
                exit()

    # Cria o banco de dados e o usa caso ainda não exista.
    def create_schema(self):
        cursor = self.con.cursor() #Cria um cursor para executar comandos SQL
        #Executa comandos em SQL
        cursor.execute("CREATE DATABASE IF NOT EXISTS db_unifecaf")
        cursor.execute("USE db_unifecaf") #Passa a usar o banco de dados
        
    # Cria a tabela caso ainda não exista.
    def create_table_users(self): 
        cursor = self.con.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(100) NOT NULL UNIQUE,
            nome VARCHAR(100) NOT NULL,
            sobrenome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            ra INT NOT NULL UNIQUE,
            telefone VARCHAR(20),
            data_nascimento DATE,
            senha VARCHAR(255) NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            rank INT
        )
        """)
        self.con.commit() # Salva o banco de dados.
        
    # Cria a tabela caso ainda não exista.
    def create_table_event(self): 
        cursor = self.con.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS eventos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(150) NOT NULL,
            descricao TEXT,
            data_inicio DATE NOT NULL,
            hora_inicio TIME NOT NULL,
            data_fim DATE NOT NULL,
            hora_fim TIME NOT NULL,
            local VARCHAR(255),
            vagas INT,
            max_vagas INT,
            data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            id_criador INT NOT NULL,
            FOREIGN KEY (id_criador) REFERENCES usuarios(id) ON DELETE CASCADE
        )
        """)
        self.con.commit()
        
    def create_table_registrations(self):
        cursor = self.con.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS inscricoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_usuario INT NOT NULL,
            id_evento INT NOT NULL,
            data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (id_evento) REFERENCES eventos(id) ON DELETE CASCADE,
            UNIQUE (id_usuario, id_evento)
        )
        """)
    
    #Cria o Administrador do sistema.
    def create_admin(self):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE usuario = 'root'")
        findAdmin = cursor.fetchone()
        if findAdmin == None:
            cursor.execute(
            f"INSERT INTO usuarios(usuario, nome, senha, rank) VALUES ('root','admin', '{ph.hash('admin')}', '2')")
            self.con.commit()
        else:
            pass
    
    #Função de criação de conta.
    def create_account(self):
        try:
            self.header_terminal("CRIAR CONTA")
            user = self.validate("\nUsuario: ", 'empty').strip().lower()
            cursor = self.con.cursor()
            cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario = '{user}'")
            searchUsuario = cursor.fetchone()
            if searchUsuario == None: # verifica se o usuario existe.
                pass
            else:
                self.message_error("\nEste usuário já existe!")
                return
            name = self.validate("Nome: ", 'fullname').strip().lower()
            lastname = self.validate("Sobrenome: ", 'fullname').strip().lower()
            email = self.validate("Email: ", 'email')
            cursor.execute(f"SELECT email FROM usuarios WHERE email = '{email}'")
            searchEmail = cursor.fetchone()
            if searchEmail == None: # Verifica se o email já esta sendo usado.
                pass
            else:
                self.message_error("\nEste email já está sendo usado!")
                return
            ra = self.validate("RA: ", 'ra')
            cursor.execute(f"SELECT ra FROM usuarios WHERE ra = '{ra}'")
            searchRa = cursor.fetchone()    
            if searchRa == None: # RA único para cada aluno, verifica se já não esta sendo usado.
                pass
            else:
                self.message_error("\nEste RA já está sendo usado!")
                return
            phone = self.validate("Telefone: ", 'phone').strip()
            date = self.validate("Data de nascimento Dia/Mês/Ano: ", 'birth')
            password = self.validate("Senha: ", 'password').strip()
            passwordconfirm = self.validate("Repita a senha: ", 'empty').strip()
            
            firstLetter = email[0] #Pega a primeira letra do campo email
            find_server = email.find('@') #Encontra o caractere especifico.
            server = email[find_server:] #Pega do @ em diante.
            lengthEmail = (len(email[:find_server])-1) * "*" #Do @ para trás transforma em * vezes o tamando do nome.
            
            if password == passwordconfirm: # Confifrma se a senha coincide com o repetir senha.
                password_hash = ph.hash(password) #Criptografa a senha.
                cursor.execute(
                f"INSERT INTO usuarios(usuario, nome, sobrenome, email, ra, telefone, data_nascimento, senha, rank) VALUES ('{user}','{name}', '{lastname}', '{email}', '{ra}', '{phone}', STR_TO_DATE('{date}', '%d/%m/%Y'), '{password_hash}', '0')")
                self.con.commit()
                self.message_approved(f"Olá {name.title()} sua conta foi criada com sucesso! Enviamos um link de confirmação para o email {firstLetter.lower()}{(lengthEmail)}{server}")
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            else:
                self.message_error("\nSenhas não coincidem.")
        except Exception as e: #Captura um erro
            translator = Translator()
            translateError = translator.translate(e, src='en', dest='pt').text #Traduz o erro de inglês para português.
            self.message_error(f"{translateError}")
            
    #Função de criação de eventos            
    def create_event(self):
        try:            
            self.header_terminal("CRIAR EVENTO")
            # Abaixo, validadte é uma função para validar o maximo possivel para evitar burlar sistema e cometer erros.
            name = self.validate("\nNome do evento: ", 'empty').strip()
            description = self.validate("Descrição do evento: ", 'empty').strip()
            date = self.validate("Data do evento Dia/Mês/Ano: ", 'date')
            initialHour = self.validate("Horário HH:MM: ", 'hour')
            endDate = self.validate("Data do encerramento do evento Dia/Mês/Ano: ", 'date')
            endHour = self.validate("Horário de encerramento HH:MM: ", 'hour')
            locale = self.validate("Local: ", 'empty').strip()
            vacancy = self.validate("Quantidade de vagas: ", 'vacancy')
            
            cursor = self.con.cursor()
            cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{self.username}'")
            findUser = cursor.fetchone()
            cursor.execute(f"INSERT INTO eventos(titulo, descricao, data_inicio, hora_inicio, data_fim, hora_fim, local, vagas, max_vagas, id_criador) VALUES ('{name}', '{description}', STR_TO_DATE('{date}', '%d/%m/%Y'), '{initialHour}', STR_TO_DATE('{endDate}', '%d/%m/%Y'), '{endHour}', '{locale}', '{vacancy}', '{vacancy}', {findUser[0]})")
            self.con.commit()
            self.message_approved(f"\nEvento criado com sucesso!")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        except Exception as e:
            translator = Translator()
            translateError = translator.translate(e, src='en', dest='pt').text
            self.message_error(f"{translateError}")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
    
    #Função para se registrar em eventos existentes.
    def event_register(self):
        self.header_terminal("REGISTRAR EM EVENTOS")
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        events = cursor.fetchall()
        if events == []:
            self.message_error("\nAinda não existe eventos.")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
            return
        else:
            self.event_list()
            try:
                eventId = self.validate("\nSelecine o ID do evento que deseja se registrar: ", 'digit')
                cursor.execute(f"SELECT id FROM usuarios WHERE usuario = '{self.username}'")
                findUser = cursor.fetchone()
                cursor.execute(f"SELECT titulo FROM eventos WHERE id = '{eventId}'")
                findEventTittle = cursor.fetchone()
                cursor.execute(f"SELECT vagas FROM eventos WHERE id = '{eventId}'")
                findEventVagas = cursor.fetchone()
                if findEventVagas[0] == 0:
                    self.message_error("\nNão há mais vagas para este evento")
                    keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                    self.clear()
                    return
                else:
                    newVacancy = (findEventVagas[0] - 1)
                    cursor.execute(f"UPDATE eventos SET vagas = '{newVacancy}' WHERE id = '{eventId}'")
                    cursor.execute(f"INSERT INTO inscricoes(id_usuario, id_evento) VALUES ('{findUser[0]}', '{eventId}')")
                    self.con.commit()
                    self.message_approved(f"Parabéns, você se inscreveu no evento {findEventTittle[0].title()}.")
                    keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                    self.clear()
            except Exception as e:
                self.message_error("Usuário já registrado.")
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                self.clear()
    
    #Função para mostrar todos eventos existentes.
    def show_all_events(self):
        self.header_terminal("EVENTOS LISTADOS")
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        events = cursor.fetchall()
        if events == []:
            self.message_error("\nAinda não existe eventos.")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        else:
            self.event_list()
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
    
    #Função para procurar algum evento existente.
    def search_event(self):
        self.header_terminal("PROCURAR EVENTOS")
        title = self.validate("\nDigite o nome do evento: ", 'empty')
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        event = cursor.fetchall()
        if event == []:
            self.message_error("\nAinda não existe eventos.")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        else:
            cursor.execute(f"SELECT * FROM eventos WHERE titulo LIKE '%{title}%'")
            events = cursor.fetchall()
            if events == []:
                self.message_error("\nEvento não encontrado!")
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                self.clear()
            else:
                for event in events:
                    print(f"\n{Fore.LIGHTMAGENTA_EX}ID: {Fore.LIGHTCYAN_EX}{event[0]} - {event[1]}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTMAGENTA_EX}Descrição: {Fore.LIGHTCYAN_EX}{event[2]}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTMAGENTA_EX}Data: {Fore.LIGHTCYAN_EX}{event[3]} {event[4]}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTMAGENTA_EX}Encerra: {Fore.LIGHTCYAN_EX}{event[5]} {event[6]}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTMAGENTA_EX}Local: {Fore.LIGHTCYAN_EX}{event[7]}{Style.RESET_ALL}")
                    print(f"{Fore.LIGHTMAGENTA_EX}vagas: {Fore.LIGHTCYAN_EX}{event[8]}/{event[9]}{Style.RESET_ALL}")
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
    
    #Função para registrar estudantes nos eventos.
    def registered_students(self):
        self.header_terminal("USUÁRIOS REGISTRADOS")
        try:
            cursor = self.con.cursor()
            cursor.execute(f"SELECT * FROM eventos")
            event = cursor.fetchall()
            if event == []:
                self.message_error("\nAinda não existe eventos.")
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                self.clear()
            else:
                self.event_list()
                eventId = self.validate("\nSelecine o ID do evento que deseja se visualizar: ", 'digit')
                self.clear()
                cursor.execute(f"SELECT titulo FROM eventos WHERE id = '{eventId}'")
                eventTitle = cursor.fetchone()
                cursor.execute(f"""
                SELECT u.nome, u.sobrenome AS usuario, e.titulo AS evento
                FROM inscricoes i
                JOIN usuarios u ON i.id_usuario = u.id
                JOIN eventos e ON i.id_evento = e.id
                WHERE e.id = '{eventId}'
                """)
                students = cursor.fetchall()
                if students == []:
                    self.message_error("Ninguém se inscreveu ainda.")
                    keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                    self.clear()
                else:
                    print(f"{Fore.LIGHTMAGENTA_EX}{eventTitle[0].title()}:")
                    for student in students:
                        print(f"{Fore.LIGHTCYAN_EX}{student[0].title()} {student[1].title()}")
                    keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                    self.clear()
        except Exception as e:
            translator = Translator()
            translateError = translator.translate(e, src='en', dest='pt').text
            self.message_error(f"{translateError}")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
            
    #Função para deletar eventos.
    def drop_event(self):
        self.header_terminal("DELETAR EVENTO")
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        events = cursor.fetchall()
        if events == []:
            self.message_error("\nAinda não existe eventos.")
            self.clear()
        else:
            self.event_list()
            eventId = self.validate("Digite o ID do evento que desejar deletar: ", 'digit')
            cursor.execute(f"SELECT titulo FROM eventos WHERE id = '{eventId}'")
            info = cursor.fetchone()
            cursor.execute(f"DELETE FROM eventos WHERE id = '{eventId}'")
            self.con.commit()
            self.message_approved(f"O evento {info[0]} foi excluido!")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        
    #Função para atualizar informações de um evento.
    def update_event(self):
        self.header_terminal("EDITAR EVENTOS")
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        events = cursor.fetchall()
        if events == []:
            self.message_error("\nAinda não existe eventos.")
            self.clear()
            return
        else:
            self.event_list()
        try:
            eventId = self.validate("Digite o ID do evento que desejar editar: ", 'digit')
            newTitle = self.validate("Novo titulo: ",'empty').strip().lower()
            newDescription = self.validate("Nova descrição: ", 'empty').strip()
            newDate = self.validate("Nova data de inicio do evento Dia/Mês/Ano: ", 'date')
            newHour = self.validate("Novo horário de inicio HH:MM: ", 'hour')
            newEndDate = self.validate("Nova data de fim do evento Dia/Mês/Ano: ", 'date')
            newEndHour = self.validate("Novo horário de fim do evento HH:MM: ", 'hour')
            newLocale = self.validate("Novo local: ", 'empty').strip()
            newVacancy = self.validate("Nova quantidade de vagas: ", 'vacancy')
            
            cursor.execute(f"SELECT id FROM usuarios WHERE usuario = '{self.username}'")
            findUser = cursor.fetchone()
            cursor.execute(
            f"UPDATE eventos SET titulo = '{newTitle}', descricao = '{newDescription}', data_inicio = STR_TO_DATE('{newDate}', '%d/%m/%Y'), hora_inicio = '{newHour}', data_fim = STR_TO_DATE('{newEndDate}', '%d/%m/%Y'), hora_fim = '{newEndHour}', local = '{newLocale}', vagas = '{newVacancy}', max_vagas = '{newVacancy}', id_criador = '{findUser[0]}' WHERE id = '{eventId}'")
            self.con.commit()
            self.message_approved("\nO evento foi alterado.")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        except Exception as e:
            self.message_error(e)
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
    
    #Esta função  altera permissão, aqui a conta de Administrador pode tornar um usuário MODERADOR, ou um MODERADOR em um Usuário.
    def alter_permission(self):
        self.header_terminal("ALTERAR RANK DE USUÁRIOS")
        usuario = self.validate("\nDigite o nome do usuário: ", 'empty')
        cursor = self.con.cursor()
        cursor.execute(f"SELECT usuario FROM usuarios WHERE usuario = '{usuario}'")
        searchUsuario = cursor.fetchone()
        cursor.execute(f"SELECT nome FROM usuarios WHERE usuario = '{usuario}'")
        searchName = cursor.fetchone()
        if searchUsuario == None:
            self.message_error("\nUsuário não encontrado")
            keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
            self.clear()
        else:
            cursor.execute(f"SELECT rank FROM usuarios WHERE usuario = '{usuario}'")
            rank = cursor.fetchone()
            if rank[0] == 0:
                cursor.execute(
                f"UPDATE usuarios SET rank = '1' WHERE usuario = '{usuario}'")
                self.message_approved(f"{searchName[0].title()} agora é um moderador.")
                self.con.commit()
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                self.clear()
            elif rank[0] == 1:
                cursor.execute(
                f"UPDATE usuarios SET rank = '0' WHERE usuario = '{usuario}'")
                self.message_approved(f"{searchName[0].title()} agora é um usuário.")
                self.con.commit()
                keyboard.wait('enter', print(f"{Fore.LIGHTGREEN_EX}\nPressione 'Enter' para continuar...{Style.RESET_ALL}"))
                self.clear()
            else:
                self.message_error("\nUsuário inexistente.")
                self.clear()
                return
            
    def event_list(self):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT * FROM eventos")
        events = cursor.fetchall()
        for event in events:
            print(f"\n{Fore.LIGHTMAGENTA_EX}ID: {Fore.LIGHTCYAN_EX}{event[0]} - {event[1]}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}Descrição: {Fore.LIGHTCYAN_EX}{event[2]}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}Data: {Fore.LIGHTCYAN_EX}{event[3]} {event[4]}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}Encerra: {Fore.LIGHTCYAN_EX}{event[5]} {event[6]}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}Local: {Fore.LIGHTCYAN_EX}{event[7]}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}vagas: {Fore.LIGHTCYAN_EX}{event[8]}/{event[9]}{Style.RESET_ALL}")
    
    #Aqui é uma função usada para validar todo o código.
    def validate(self, response, type):
        while True:
            dateFormat = "%d/%m/%Y"
            hourFormat = "%H:%M"
            res = input(response).strip()
                    
            if type == 'email':
                translator = Translator()
                try:
                    validate_email(res)
                    return res
                except EmailNotValidError as e:
                    translateError = translator.translate(e, src='en', dest='pt').text
                    self.message_error(f"{translateError}")
                    continue

            elif type == 'password':
                if len(res) < 8:
                    self.message_error("A senha deve ter pelo menos 8 caracteres.")
                    continue
                if not re.search(r'[A-Z]', res):
                    self.message_error("A senha deve conter pelo menos uma letra maiúscula.")
                    continue
                if not re.search(r'[a-z]', res):
                    self.message_error("A senha deve conter pelo menos uma letra minúscula.")
                    continue
                if not re.search(r'\d', res):
                    self.message_error("A senha deve conter pelo menos um número.")
                    continue
                if not re.search(r'[!@#$%^&*(),.?":{}|<>]', res):
                    self.message_error("A senha deve conter pelo menos um caractere especial.")
                    continue
                return res
            
            elif type == 'date':
                try:
                    date = datetime.strptime(res, dateFormat).date()
                    if date < datetime.today().date():
                        self.message_error(f"A data do evento não pode ser anterior à data atual.")
                        continue
                    return date.strftime(dateFormat)
                except ValueError:
                    self.message_error("Data inválida. Use o formato adequeado, exemplo: Dia/Mês/Ano.")
                    
            elif type == 'birth':
                try:
                    date = datetime.strptime(res, dateFormat).date()
                    return date.strftime(dateFormat)
                except ValueError:
                    self.message_error("Data inválida. Use o formato adequeado, exemplo: Dia/Mês/Ano.")
                    continue
                
            elif type == 'hour':
                try:
                    hour = datetime.strptime(res, hourFormat).time()
                    return hour
                except ValueError:
                    self.message_error("Horário inválido. Use o formato adequeado, exemplo: HH:MM.")
                    
            elif type == 'fullname':
                pattern = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,50}$'
                try:
                    if re.match(pattern, res):
                        return res
                except Exception:
                    self.message_error("Nome inválido. Nomes precisam conter letras de a-z e no mínimo 2 caracteres")
                continue
                
            elif type == 'empty':
                if res == "":
                    self.message_error("Este campo não pode ficar vazio.")
                else:
                    return res
                
            elif type == 'ra':
                try:
                    if re.fullmatch(r'\d+', res):
                        if len(res) == 6:
                            return res
                        else:
                            self.message_error("RA inválido, precisa conter 6 digitos")
                            continue
                    else:
                        self.message_error("RA inválido, use apenas números.")
                except ValueError as e:
                    self.message_error(e)
                continue
                
            elif type == 'digit':
                try:
                    if re.fullmatch(r'\d+', res):
                        self.clear()
                        return res
                    else:
                        self.message_error("Use apenas números.")
                except ValueError as e:
                    self.message_error(e)
                
            elif type == 'float':
                try:
                    pattern = r'^-?\d+(\.\d+)?$'
                    if re.match(pattern, res):
                        return res
                except ValueError:
                    self.message_error("Use apenas números.")
                    continue
                
            elif type == 'vacancy':
                try:
                    if re.fullmatch(r'\d+', res):
                        return res
                    else:
                        self.message_error("Quantidade inválida, utilize apenas números.")
                except ValueError as e:
                    self.message_error(e)
                continue
                    
            elif type == 'phone':
                pattern = r'^\(?\+?[0-9]*\)?[-.\s]?\(?[0-9]+\)?[-.\s]?[0-9]+[-.\s]?[0-9]+$'
                if re.match(pattern, res):
                    if len(res) >= 8:
                        return res
                    else:
                        self.message_error("O número precisa conter no minimo 8 digitos")
                        continue
                else:
                    self.message_error("Número inválido!")
                    continue
        
    # Função para as mensagens de erro
    def message_error(self, message):
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")
        sleep(1)
        
    # Função para as mensagens de feito com sucesso.
    def message_approved(self, message):
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
        sleep(1)
        
    # Função para limpar o terminal.
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Cabeçalho do sistema
    def header_terminal(self, titulo, largura=50):
        self.clear()
        if len(titulo) > largura - 4:
            largura = len(titulo) + 4
        print(Fore.LIGHTBLUE_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + "+" + "-" * (largura - 2) + "+")
        print("|" + titulo.center(largura - 2) + "|")
        print("+" + "-" * (largura - 2) + "+" + Style.RESET_ALL)

System = Unifecaf() # Cria a conexão com banco de dados.
System.create_schema() # Cria o banco de dados e o usa.
System.create_table_users() # Cria  a tabela.
System.create_table_event() # Cria  a tabela.
System.create_table_registrations() # Cria  a tabela.
System.create_admin() # Cria a conta Admin
System.login()

Unifecaf.con.close() # Fechar o banco de dados.