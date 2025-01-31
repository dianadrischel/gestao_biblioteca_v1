import csv
import time
import os
from datetime import datetime
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

class Ferramenta:
    def limpar_tela(self):  
        sistema = os.name
        os.system('cls' if sistema == 'nt' else 'clear')

    def continuar_menu(self):
        input("\nPressione Enter para continuar...")
        time.sleep(1)

class Usuario:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
        print("\nBem-vindo à criação de usuário!")
        time.sleep(1)

        nome = input("Digite seu nome: ").strip()
        email = input("Digite seu e-mail: ").strip()

        while True:
            senha = input("Crie uma senha para acessar o sistema: ").strip()
            senha_confirmada = input("Confirme a senha: ").strip()

            if senha == senha_confirmada:
                print("Senha confirmada com sucesso.")
                time.sleep(1)
                break
            else:
                print("As senhas não coincidem. Tente novamente.")
                time.sleep(1)

        senha_hash = hash_senha(senha)

        try:
            with open("usuarios.csv", mode="a", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([nome, email, senha_hash])
                print(f"O usuário '{nome}' foi criado com sucesso.\n")
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao criar o usuário: {e}")

    def autenticar_usuario(self):
        print("\nInsira o e-mail cadastrado:")
        email_digitado = input("E-mail: ").strip()

        print("Digite sua senha:")
        senha_digitada = input("Senha: ").strip()

        senha_digitada_hash = hash_senha(senha_digitada)

        try:
            with open("usuarios.csv", mode="r", newline="", encoding="utf-8") as arquivo:
                leitores = csv.reader(arquivo)
                for linha in leitores:
                    if len(linha) == 3:
                        nome, email, senha_armazenada = linha
                        if email == email_digitado and senha_digitada_hash == senha_armazenada:
                            print(f"Bem-vindo, {nome}!\n")
                            time.sleep(1)
                            return nome
                print("E-mail ou senha incorretos. Tente novamente.")
                time.sleep(1)
        except FileNotFoundError:
            print("Não há registros")
        except Exception as e:
            print(f"Erro ao autenticar o usuário: {e}")
        
        return None

    def existem_usuarios_cadastrados(self):
        try:
            with open("usuarios.csv", mode="r", newline="", encoding="utf-8") as arquivo:
                leitores = list(csv.reader(arquivo))
                return len(leitores) > 0
        except FileNotFoundError:
            return False

class Biblioteca:
    def listar_livros(self):
        try:
            with open("livros.csv", mode="r", newline="", encoding="utf-8") as arquivo:
                livros = csv.reader(arquivo)
                print("\nLista de livros disponíveis:")
                time.sleep(1)
                for livro in livros:
                    if len(livro) >= 5:
                        id_livro, nome, autor, ano, status = livro[:5]
                        detalhes = ", ".join(livro[5:]) if len(livro) > 5 else ""
                        print(f"ID: {id_livro}, Nome: {nome}, Autor: {autor}, Ano: {ano}, Status: {status}, {detalhes}")
                        time.sleep(1)
        except FileNotFoundError:
            print("Nenhum livro cadastrado ou arquivo 'livros.csv' não encontrado.")
        except Exception as e:
            print(f"Erro ao listar os livros: {e}")

    def cadastrar_livro(self):
        try:
            nome = input("Digite o nome do livro: ").strip()
            autor = input("Digite o autor do livro: ").strip()
            ano = input("Digite o ano de publicação: ").strip()

            with open("livros.csv", mode="a", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([len(open("livros.csv").readlines()) + 1, nome, autor, ano, "Disponível"])
                print(f"Livro '{nome}' cadastrado com sucesso!\n")
                time.sleep(1)
        except Exception as e:
            print(f"Erro ao cadastrar o livro: {e}")

    def emprestar_livro(self):
        cliente_nome = input("Digite o nome do cliente: ").strip()
        livro_id = input("Digite o ID do livro que deseja emprestar: ").strip()
        try:
            with open("livros.csv", mode="r", newline="", encoding="utf-8") as arquivo:
                livros = list(csv.reader(arquivo))

            for livro in livros:
                if livro[0] == livro_id and livro[4] == "Disponível":
                    livro[4] = "Emprestado"
                    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    livro.append(f"Emprestado por {cliente_nome} em {data_hora}")

                    with open("livros.csv", mode="w", newline="", encoding="utf-8") as arquivo:
                        escritor = csv.writer(arquivo)
                        escritor.writerows(livros)
                    print(f"O livro '{livro[1]}' foi emprestado com sucesso para {cliente_nome} em {data_hora}!\n")
                    time.sleep(1)
                    return
            print("Livro não encontrado ou já emprestado.")
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao emprestar o livro: {e}")

    def devolver_livro(self):
        livro_id = input("Digite o ID do livro que deseja devolver: ").strip()
        try:
            with open("livros.csv", mode="r", newline="", encoding="utf-8") as arquivo:
                livros = list(csv.reader(arquivo))

            for livro in livros:
                if livro[0] == livro_id and livro[4] == "Emprestado":
                    livro[4] = "Disponível"
                    if len(livro) > 5:
                        livro.pop()

                    with open("livros.csv", mode="w", newline="", encoding="utf-8") as arquivo:
                        escritor = csv.writer(arquivo)
                        escritor.writerows(livros)
                    print(f"O livro '{livro[1]}' foi devolvido com sucesso!\n")
                    time.sleep(1)
                    return
            print("Livro não encontrado ou não emprestado.")
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao devolver o livro: {e}")

class Sistema:
    def __init__(self):
        self.utils = Ferramenta()
        self.usuario = Usuario()
        self.biblioteca = Biblioteca()

    def tela_inicial(self):
        while True:
            print("\nBem-vindos à Biblioteca Comunitária Carne de Gaivota!\n")
            time.sleep(1)
            print("Acesse o nosso sistema para se cadastrar e tenha uma excelente leitura.\n")
            time.sleep(1)

            if self.usuario.existem_usuarios_cadastrados():
                print("1 - Criar Usuário")
                print("2 - Fazer Login")
                print("3 - Sair")
            else:
                print("1 - Criar Usuário")
                print("2 - Sair")
            
            try:
                opcao = input("Escolha uma opção: ").strip()

                if opcao == '1':
                    self.usuario.criar_usuario()
                    self.login_tela()
                elif opcao == '2':
                    if self.usuario.existem_usuarios_cadastrados():
                        self.login_tela()
                    else:
                        print("Saindo do sistema...")
                        time.sleep(1)
                        break
                elif opcao == '3' and self.usuario.existem_usuarios_cadastrados():
                    print("Saindo do sistema...")
                    time.sleep(1)
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    time.sleep(1)
            except OSError:
                print("Erro de I/O detectado. Tente novamente.")

    def login_tela(self):
        while True:
            self.utils.limpar_tela()
            print("\nBem-vindos à Biblioteca Comunitária Carne de Gaivota!")
            time.sleep(1)
            print("Acesse o nosso sistema para e tenha uma excelente leitura.\n")
            time.sleep(1)

            print("1 - Fazer login")
            print("2 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                usuario_nome = self.usuario.autenticar_usuario()
                if usuario_nome:
                    self.sistema_biblioteca()
                    break
            elif opcao == '2':
                print("Saindo do sistema...")
                time.sleep(1)
                break
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)

    def sistema_biblioteca(self):
        while True:
            self.utils.limpar_tela()
            print("\n=== Sistema de Biblioteca ===")
            time.sleep(1)
            print("1. Listar livros")
            print("2. Cadastrar livro")
            print("3. Emprestar livro")
            print("4. Devolver livro")
            print("5. Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.biblioteca.listar_livros()
                self.utils.continuar_menu()
            elif opcao == '2':
                self.biblioteca.cadastrar_livro()
            elif opcao == '3':
                self.biblioteca.emprestar_livro()
            elif opcao == '4':
                self.biblioteca.devolver_livro()
            elif opcao == '5':
                print("Saindo do sistema da biblioteca...\n")
                time.sleep(1)
                break
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)

if __name__ == "__main__":
    sistema = Sistema()
    sistema.tela_inicial()
