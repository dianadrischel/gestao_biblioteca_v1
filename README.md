## 📚 Sistema de Gestão de Bibliotecas ##

Este projeto foi idealizado e desenvolvido para o curso de Desenvolvimento de Software no SENAI.

Se trata da implementação de um sistema de gerenciamento de biblioteca comunitária com funcionalidades de cadastro de usuários, login, cadastro e empréstimo de livros. O sistema armazena as informações de usuários e livros em arquivos CSV e oferece uma interface interativa no terminal para facilitar o gerenciamento dos dados.

## 🚀 Funcionalidades ##

### 1. Cadastro e Login de Usuários

- **Criação de usuário**: Permite a criação de novos usuários com nome, e-mail e senha.<br>
- *A senha é armazenada de forma segura utilizando SHA-256.*

**Login de usuário**: Usuários podem fazer login fornecendo seu e-mail e senha.

### 2. Gerenciamento de Livros

- **Listar livros**: Exibe uma lista de livros cadastrados na biblioteca.

- **Cadastrar livro**: Permite o cadastro de novos livros na biblioteca com informações como nome, autor e ano de publicação.

- **Emprestar livro**: Permite que um livro seja emprestado a um cliente, registrando o nome do cliente e a data/hora do empréstimo.

- **Devolver livro**: Permite que um livro seja devolvido, marcando-o como "disponível".

## 🛠 Arquivos Utilizados

- **usuarios.csv**: Armazena os dados de usuários cadastrados, como nome, e-mail e senha (hash).

- **livros.csv**: Armazena os dados dos livros cadastrados, incluindo ID, nome, autor, ano de publicação e status (disponível/emprestado).

## 📌 Requisitos

- Python 3.x

- Bibliotecas padrão: `csv`, `os`, `time`, `datetime`, `hashlib`
