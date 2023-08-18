import csv, os
from datetime import datetime

def relatorio_atrasados():
    emprestimo_csv = open('emprestimo.csv')

    dados_emprestimo = csv.DictReader(emprestimo_csv, delimiter=';')

    os.system('cls') or None
    print("--------------------------------------RELATÓRIO DE LIVROS ATRASADOS--------------------------------------")
    print(f'{"CPF":15}',f'{"NOME":20}',f'{"TITULO":20}',f'{"EMPRESTIMO":20}',f'{"SITUAÇÃO":20}',f'{"DIAS"}')
    for emprestados in dados_emprestimo:
        data_empretimo = datetime.strptime(emprestados['data_emprestimo'], '%Y-%m-%d')
        # data_emprestimo = datetime.strptime(emprestados['data_emprestimo'], '%d/%m/%Y')
        data_hoje = datetime.today()
        dias_atrasados = (data_hoje - data_empretimo).days
        
        if dias_atrasados > 7:
            situacao = str("atrasado")
            print(f'{emprestados["cpf"]:15}',
                  f'{emprestados["nome_usuario"]:20}',
                  f'{emprestados["titulo_livro"]:20}',
                  f'{emprestados["data_emprestimo"]:20}',
                  f'{situacao:20}',
                  f'{dias_atrasados}')
        




    

relatorio_atrasados()