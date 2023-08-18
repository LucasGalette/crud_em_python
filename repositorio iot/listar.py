import os, csv

def listar_cliente():
    clientes_csv = open('clientes.csv', encoding='utf-8')
    dados = csv.DictReader(clientes_csv,delimiter=';')
    os.system('cls') or None
    print("-----------LISTAGEM DE CLIENTES------------")
    print(f'{"CPF":15}',f'{"NOME":25}',f'{"RG"}')
    for clientes in dados:
        print(f'{clientes["cpf"]:15}', f'{clientes["nome"]:25}',f'{clientes["rg"]}')
    clientes_csv.close()



def listar_livros():
    livros_csv = open('livros.csv', encoding='utf-8')
    dados = csv.DictReader(livros_csv,delimiter=';')
    os.system('cls') or None
    print("---------------------------------LISTAGEM DE LIVROS---------------------------------")
    print(f'{"CODIGO":15}',f'{"TITULO LIVRO":20}',f'{"AUTOR":15}',f'{"EDITORA":15}',f'{"ANO LANÇAMENTO"}')
    for livros in dados:
        print(f'{livros["codigo"]:15}', f'{livros["titulo_livro"]:20}',f'{livros["autor"]:15}',f'{livros["editora"]:15}',f'{livros["ano_lancamento"]}')
    livros_csv.close()



def listar_emprestimos():
    #cpf;"nome_usuario";codigo_livro;titulo_livro;data_emprestimo
    emprestimo_csv = open('emprestimo.csv', encoding='utf-8')
    dados = csv.DictReader(emprestimo_csv,delimiter=';')
    os.system('cls') or None
    print("---------------------------------LISTAGEM DE EMPRESTIMOS---------------------------------")
    print(f'{"CPF":15}',f'{"NOME USUARIO":20}',f'{"CODIGO LIVRO":20}',f'{"TITULO LIVRO":20}',f'{"DATA EMPRESTIMO"}')
    for livros in dados:
        print(f'{livros["cpf"]:15}', f'{livros["nome_usuario"]:20}',f'{livros["codigo_livro"]:20}',f'{livros["titulo_livro"]:20}',f'{livros["data_emprestimo"]}')
    emprestimo_csv.close()

listar_emprestimos()
    