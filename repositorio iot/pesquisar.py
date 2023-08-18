import csv
def pesquisar_cliente(nome_cliente):
    cliente_csv = open('clientes.csv') #abrindo o arquivo CSV
    dados_cliente = csv.DictReader(cliente_csv, delimiter=";") #lendo conteudo

    for cliente in dados_cliente: #percorrendo as linhas do arquivo
        if(cliente["nome"].lower() == nome_cliente.lower()):
            nome =  (cliente["nome"]) #listar o nome do cliente, a partir da chave ["nome"]
            cpf =  (cliente["cpf"])
            return (True,nome, cpf)
            break
    return (False,)



def pesquisar_livro():
    return (True,90, "Nome do livro", "ioio")