import os, json
from datetime import datetime, date

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.json")


def carregar_produtos():
    
    #Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo):

        #Ler o conteudo existente
        with open(caminho_arquivo, "r") as file:
            dados = json.load(file)
            return dados
        
    else:
        #Retorna um dicionario vazio
        dados = {}
        return dados


def cadastrar_produto():
    
    os.system("cls")
    nome = preencher_nome()
    os.system("cls")
    categoria = preencher_categoria()
    os.system("cls")
    quantidade = preencher_quantidade()
    os.system("cls")
    preco = preencher_preco()


    data = str(date.today()).replace("-", "")
    hora = datetime.now().strftime("%H%M")
    
    id = f"{data[2:]}{hora}{categoria[:3]}{nome[:3]}"

    while True:
        try:
            os.system("cls")

            print(f"ID: {id}")
            print(f"Nome do Produto: {nome}")
            print(f"Categoria: {categoria}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço: {preco}")
            print("************************************************\n")

            cadastrar = int(input("Deseja cadastrar o novo produto?\n(1)Sim\n(2)Não\n"))

            match cadastrar:
                case 1:
                    dic_produto = {
                        id:{
                            "ID": id,
                            "NOME": nome,
                            "CATEGORIA": categoria,
                            "QUANTIDADE": quantidade,
                            "PRECO": preco
                        }                        
                    }

                    dados_produtos = carregar_produtos()

                    #Adiciona o novo produto ao dicionario extraido do JSON
                    dados_produtos.update(dic_produto)

                    #Salva o dicionario no JSON sobrescrevendo
                    with open(caminho_arquivo, "w") as file:
                        json.dump(dados_produtos, file, indent=4)

                    os.system('cls') 
                    print("Produto Cadastrado com Sucesso!\n\n")
                    break

                case 2:
                    break

                case __:
                    print("Formato invalido! Por favor, insira 1 ou 2.")

        except ValueError:
            opcao_invalida()

    
def preencher_nome():

    nome = input("Informe o nome do produto: ").upper()

    while True:
        try:
            #valida se o nome escrito pelo funcionario esta correto, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'O NOME esta correto?\n\n{nome}\n\n(1)Sim\n(2)Não\n'))

            match validar:
                case 1:
                    return nome
                case 2:
                     nome = input("Informe o nome do produto: ").upper()
                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido! Por favor, insira 1 ou 2.")


def preencher_categoria():

    categoria = input("Informe a categoria do produto: ").upper()

    while True:
        try:
            #valida se a categoria escrita pelo funcionario esta correta, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'A CATEGORIA esta correta?\n\n{categoria}\n\n(1)Sim\n(2)Não\n'))

            match validar:
                case 1:
                    return categoria
                case 2:
                     categoria = input("Informe a categoria do produto: ").upper()
                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido! Por favor, insira 1 ou 2.")


def preencher_quantidade():

    while True:
        try:
            quantidade = int(input("Informe a quantidade do produto: "))

            #valida se a quantidade escrita pelo funcionario esta correta, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'A QUANTIDADE esta correta?\n\n{quantidade}\n\n(1)Sim\n(2)Não\n'))

            match validar:
                case 1:
                    return quantidade
                case 2:
                     continue
                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido!")


def preencher_preco():

    while True:
        try:
            preco = float(input("Informe o preço da unidade do produto: "))

            #valida se a quantidade escrita pelo funcionario esta correta, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'O PREÇO esta correto?\n\n{preco}\n\n(1)Sim\n(2)Não\n'))

            match validar:
                case 1:
                    return preco
                case 2:
                     continue
                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido!")


def montar_tabela(dicionario, filtro, busca, valor):

    # Definir as colunas da tabela
    colunas = ["ID", "NOME", "CATEGORIA", "QUANTIDADE", "PRECO"]

    # Calcular a largura máxima para cada coluna
    larguras = {coluna: len(coluna) for coluna in colunas}
    for produto in dicionario.values():
        for coluna in colunas:
            larguras[coluna] = max(larguras[coluna], len(str(produto[coluna])))

    # Criar uma linha divisória
    linha_divisoria = "-+-".join("-" * larguras[coluna] for coluna in colunas)

    # Exibir o cabeçalho da tabela
    cabecalho = " | ".join(f"{coluna:<{larguras[coluna]}}" for coluna in colunas)
    print(cabecalho)
    print(linha_divisoria)

    # Exibir os dados dos produtos
    for produto in dicionario.values():
        if filtro == True:
            if valor in produto["CATEGORIA"]:
                linha = " | ".join(f"{str(produto[coluna]):<{larguras[coluna]}}" for coluna in colunas)
                print(linha)

        elif busca == True:
            if valor in produto["NOME"] or valor in produto["ID"]:
                linha = " | ".join(f"{str(produto[coluna]):<{larguras[coluna]}}" for coluna in colunas)
                print(linha)

        else:
            linha = " | ".join(f"{str(produto[coluna]):<{larguras[coluna]}}" for coluna in colunas)
            print(linha)

    print("\n")


def listar_produtos():

    dados_produtos = carregar_produtos()    

    if not dados_produtos:
        print("Nenhum produto cadastrado.")
        return

    montar_tabela(dados_produtos, False, False, "")

    while True:
        try:
            opcao = int(input("(1)Filtrar por Categoria\n(2)Ordenação por Nome A-Z\n(3)Ordenação por Nome Z-A\n(4)Ordenação por quantidade\n(5)Ordenação por Preço\n(6)Voltar\n"))

            match opcao:
                case 1:
                    os.system("cls")
                    filtro_categoria()

                case 2:
                    os.system("cls")
                    ordenacao('NOME', False)

                case 3:
                    os.system("cls")
                    ordenacao('NOME', True)

                case 4:
                    os.system("cls")
                    ordenacao('QUANTIDADE', True)

                case 5:
                    os.system("cls")
                    ordenacao('PRECO', True)

                case 6:
                    os.system("cls")
                    break

                case __:
                    print("Opção invalida!")
                    continue
        
        except ValueError:
            opcao_invalida()


def filtro_categoria():

    fil_categoria = preencher_categoria()

    dados_produtos = carregar_produtos() 

    montar_tabela(dados_produtos, True, False, fil_categoria)


def ordenacao(chave, valor):

    dados_produtos = carregar_produtos()

    ord_az_produtos = dict(sorted(dados_produtos.items(), key=lambda item: item[1][chave], reverse=valor))

    montar_tabela(ord_az_produtos, False, False, "")


def atualizar_produto():

    print("ATUALIZAR\n")
    dados_produtos = carregar_produtos()

    id = input("Informe o ID do produto: ").upper()

    while True:
        try:
            #valida se o nome escrito pelo funcionario esta correto, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'O ID esta correto?\n\n{id}\n\n(1)Sim\n(2)Não\n(3)Voltar\n'))

            match validar:
                case 1:
                    if id in dados_produtos:
                        os.system('cls')
                        escolher_dado(id)
                    else:
                        print("ID não cadastrado no sistema!")

                case 2:
                     id = input("Informe o ID do produto: ").upper()
                
                case 3:
                    os.system('cls')
                    break

                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido!")


def escolher_dado(id):

    dados_produtos = carregar_produtos()

    while True:
        try:
            opcao = int(input("Alterar:\n(1)Nome\n(2)Categoria\n(3)Quantidade\n(4)Preço\n(5)Voltar\n"))

            match opcao:
                case 1:
                    os.system("cls")
                    #Preenche o novo nome
                    novo_nome = preencher_nome()

                    os.system("cls")
                    print(f"ID: {dados_produtos[id]["ID"]}")
                    print(f"NOME: {novo_nome}")
                    print(f"CATEGORIA: {dados_produtos[id]["CATEGORIA"]}")
                    print(f"QUANTIDADE: {dados_produtos[id]["QUANTIDADE"]}")
                    print(f"PRECO: {dados_produtos[id]["PRECO"]}")

                    salvar_dado(id,"NOME", novo_nome)

                case 2:
                    os.system("cls")
                    #Preenche a nova categoria
                    nova_categoria = preencher_categoria()

                    os.system("cls")
                    print(f"ID: {dados_produtos[id]["ID"]}")
                    print(f"NOME: {dados_produtos[id]["NOME"]}")
                    print(f"CATEGORIA: {nova_categoria}")
                    print(f"QUANTIDADE: {dados_produtos[id]["QUANTIDADE"]}")
                    print(f"PRECO: {dados_produtos[id]["PRECO"]}")

                    salvar_dado(id,"CATEGORIA", nova_categoria)

                case 3:
                    os.system("cls")
                    #Preenche a nova quantidade
                    nova_quantidade = preencher_quantidade()

                    os.system("cls")
                    print(f"ID: {dados_produtos[id]["ID"]}")
                    print(f"NOME: {dados_produtos[id]["NOME"]}")
                    print(f"CATEGORIA: {dados_produtos[id]["CATEGORIA"]}")
                    print(f"QUANTIDADE: {nova_quantidade}")
                    print(f"PRECO: {dados_produtos[id]["PRECO"]}")

                    salvar_dado(id,"QUANTIDADE", nova_quantidade)

                case 4:
                    os.system("cls")
                    #Preenche a nova quantidade
                    novo_preco = preencher_preco()

                    os.system("cls")
                    print(f"ID: {dados_produtos[id]["ID"]}")
                    print(f"NOME: {dados_produtos[id]["NOME"]}")
                    print(f"CATEGORIA: {dados_produtos[id]["CATEGORIA"]}")
                    print(f"QUANTIDADE: {dados_produtos[id]["QUANTIDADE"]}")
                    print(f"PRECO: {novo_preco}")

                    salvar_dado(id,"PRECO", novo_preco)

                case 5:
                    os.system("cls")
                    break
                
                case __:
                    os.system("cls")
                    print("Opção invalida!")
                    continue


        except ValueError:
            print("Formato invalido!")


def salvar_dado(id, dado, valor):
     
    dados_produtos = carregar_produtos()
    
    while True:
        try:
            salvar = int(input("\nDeseja salvar?\n(1)Sim\n(2)Não\n"))

            match salvar:
                case 1:
                    #Adiciona o novo dado ao dicionario
                    dados_produtos[id][dado]=valor
                    
                    #Salva o dicionario atualizado
                    with open(caminho_arquivo, "w") as file:
                        json.dump(dados_produtos, file, indent=4)
                    
                    os.system("cls")
                    print("Produto atualizado!")
                    break

                case 2:
                    os.system("cls")
                    break

                case __:
                    print("Opção invalida!")
                    continue

        except ValueError:
            print("Formato invalido!")


def excluir_produto():

    print("EXCLUIR\n")
    dados_produtos = carregar_produtos()

    id = input("Informe o ID do produto: ").upper()

    while True:
        try:
            #valida se o nome escrito pelo funcionario esta correto, caso não, o programa solicita uma nova entrada até o funcionario confirma 
            validar = int(input(f'O ID esta correto?\n\n{id}\n\n(1)Sim\n(2)Não\n(3)Voltar\n'))

            match validar:
                case 1:
                    if id in dados_produtos:
                        os.system('cls')
                        excluir_id(id)
                    else:
                        print("ID não cadastrado no sistema!")

                case 2:
                     id = input("Informe o ID do produto: ").upper()
                
                case 3:
                    os.system('cls')
                    break

                case __:
                    print("Opção invalida!")
                    continue
        except ValueError:
            print("Formato invalido!")


def excluir_id(id):

    dados_produtos = carregar_produtos()

    print(f"ID: {dados_produtos[id]["ID"]}")
    print(f"NOME: {dados_produtos[id]["NOME"]}")
    print(f"CATEGORIA: {dados_produtos[id]["CATEGORIA"]}")
    print(f"QUANTIDADE: {dados_produtos[id]["QUANTIDADE"]}")
    print(f"PRECO: {dados_produtos[id]["PRECO"]}")

    while True:
        try:
            deletar = int(input("\nDeseja EXCLUIR?\n(1)Sim\n(2)Não\n"))

            match deletar:
                case 1:
                    #remove do dicionario os dados setado pelo ID
                    dados_produtos.pop(id)

                    #Salva o dicionario atualizado
                    with open(caminho_arquivo, "w") as file:
                        json.dump(dados_produtos, file, indent=4)

                    os.system("cls")
                    print("Produto excluido!")
                    break

                case 2:
                    os.system("cls")
                    break

                case __:
                    print("Opção invalida!")
                    continue

        except ValueError:
            print("Formato invalido!")


def buscar_produto():

    dados_produtos = carregar_produtos()

    while True:
        try:
            palavra = input("Informe o ID ou parte do nome do produto: ").upper()


            for produto in dados_produtos.values():
                if palavra in produto["ID"] or palavra in produto["NOME"]:
                    validar = True
                    break
                
                    
            if validar == True:
                montar_tabela(dados_produtos, False, True , palavra)

            else:
                os.system("cls")
                print("Produto não encontrado!\n")

            busca = int(input("Nova busca?\n(1)Sim\n(2)Não\n"))

            match busca:
                case 1:
                    os.system("cls")
                    continue
                case 2:
                     os.system("cls")
                     break
                case __:
                    print("Opção invalida!")
                    continue

        except ValueError:
            print("Formato invalido!")


def opcao_invalida():
    
    print("Opção Invalida!")
    input("Digite qualquer tecla para voltar ao menu principal.\n")


def main():

    while True:
        try:
            os.system("cls")

            print("""
            *********************************************************************
                Bem-Vindo ao Gerenciamento de Produtos para a Loja AgilStore!
            *********************************************************************
            """)

            opcao = int(input("Escolha uma opção:\n (1)Adicionar Produto.\n (2)Listar Produtos.\n (3)Atualizar Produto.\n (4)Excluir Produto.\n (5)Buscar Produto.\n (6)Encerrar Programa.\n"))

            match opcao:
                case 1:
                    #Adiciona um novo produto
                    os.system("cls")
                    cadastrar_produto()
                
                case 2:
                    #Lista todos os produtos com opcao de filtragem
                    os.system("cls")
                    listar_produtos()

                case 3:
                    #Atualiza um produto já cadastrado
                    os.system("cls")
                    atualizar_produto()

                case 4:
                    #Exclui um produto já cadastrado
                    os.system("cls")
                    excluir_produto()

                case 5:
                    #Busca um produto já cadastrado pelo ID ou Nome
                    os.system("cls")
                    buscar_produto()

                case 6:
                    #Encerra a aplicação
                    os.system("cls")
                    print("Encerrando o programa...")
                    break

                case __:
                    opcao_invalida()

        except ValueError:
            opcao_invalida()


if __name__ == "__main__":
    main()