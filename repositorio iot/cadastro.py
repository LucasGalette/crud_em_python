import os
import csv 

def cadastrar_cliente():
    dados = {} #criando o dicionário de dados, para armazenar cliente
    
    os.system('cls') or None #limpar tela
    print('-----------CADASTRO DE CLIENTES -------------')

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    
    dados[cpf] = [nome, rg]
    
    print(dados)

    coluna = ['cpf', 'nome', 'rg']
   
    files_exists = os.path.isfile("clientes.csv")

    with open('clientes.csv','a', newline='', encoding='utf-8') as clientes_csv:
        cadastrar = csv.DictWriter(clientes_csv, fieldnames=coluna, delimiter=';',lineterminator='\r\n')
        if not files_exists:
            cadastrar.writeheader()
        cadastrar.writerow({'cpf':cpf, 'nome':nome, 'rg':rg})
    
    print("Cadastro realizado com sucesso!")
 


def cadastrar_livro():
    livros = {}
    os.system('cls') or None
    print("-----------------CADASTRAR LIVROS ----------")
    codigo = int(input("Código: "))
    titulo_livro = input("Título: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    ano_lancamento = input("Ano: ")

    colunas = ['codigo', 'titulo_livro', 'autor', 'editora', 'ano_lancamento']
    files_exists = os.path.isfile('livros.csv')

    with open('livros.csv', 'a', newline='', encoding='utf-8') as livros_csv:
        cadastrar = csv.DictWriter(livros_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            cadastrar. writeheader()
        cadastrar.writerow({'codigo':codigo, 'titulo_livro':titulo_livro,'autor':autor,'editora':editora, 'ano_lancamento':ano_lancamento})
    print("Cadastro realizado com sucesso!")
