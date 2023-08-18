import cadastro as c #definindo um alias para cadastro
import listar, movimentacao, relatorio, remover

resposta = 's'

while resposta == 's':
    menu = '''----------- BIBLIOTECA TDS 10 --------------
    \r[1] Cadastrar cliente
    \r[2] Listar clientes
    \r[3] Cadastrar livro
    \r[4] Listar livros
    \r[5] Realizar empréstimo
    \r[6] Listar empréstimos
    \r[7] Relatório de livros atrasados
    \r[8] Remover cliente
    \r[9] Remover livro
    '''
    print(menu)

    opcao = int(input('Entre com uma opção: ')) #escolher a opção digitada

    if opcao == 1:
        c.cadastrar_cliente()
    elif opcao == 2:
        listar.listar_cliente()
    elif opcao == 3:
        c.cadastrar_livro()
    elif opcao == 4:
        listar.listar_livros()
    elif opcao == 5:
        movimentacao.realizar_emprestimos()
    elif opcao == 6:
        listar.listar_emprestimos()
    elif opcao == 7:
        relatorio.relatorio_atrasados()
    elif opcao == 8:
        remover.remover_cliente()
    elif opcao == 9:
        remover.remover_livro() 


    reposta = input("\nDeseja continuar? [s/n]")