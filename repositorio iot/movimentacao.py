import os, csv
import pesquisar as p
from datetime import date

def realizar_emprestimos():
    emprestimos = []

    print("-------------EMPRESTIMO DE LIVROS --------")
    os.system('cls') or None

    nome_usuario = input("Nome do usuário:")
    retorno = p.pesquisar_cliente(nome_usuario)


    if retorno[0] == True:
        codigo_livro = int(input("Codigo livro: "))
        existe = p.pesquisar_livro()
        if existe[0] != True:
            print("Livro não existe")
        else:
            data_emprestimo = date.today()

        colunas = ['cpf', 'nome_usuario', 'codigo_livro', 'titulo_livro', 'data_emprestimo']
        files_exists = os.path.isfile("emprestimo.csv")

        with open('emprestimo.csv', 'a', newline='', encoding='utf-8') as emprestimo_csv:
            cadastrar = csv.DictWriter(emprestimo_csv, fieldnames=colunas, delimiter=';', lineterminator="\r\n")
            if not files_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'cpf': retorno[2], 'nome_usuario': retorno[1], 'codigo_livro':existe[1],
                                 'titulo_livro':existe[2], 'data_emprestimo':data_emprestimo})
        print("emprestimo realizado com sucesso!")
    else:
        print("Usário não cadastrado")
            


realizar_emprestimos()