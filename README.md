# AgilStore
Gerenciamento de Produtos - AgilStore

	Este projeto consiste em uma aplicação de gerenciamento de produtos para a loja AgilStore.
	A aplicação permite cadastrar, listar, buscar, atualizar e excluir produtos, utilizando um arquivo JSON como base de dados.

Tecnologias Utilizadas

	Python: Linguagem de programação principal do projeto.
	JSON: Utilizado para armazenar os dados dos produtos.

Funcionalidades

	Adicionar Produto
	Listar Produtos com opções de filtragem e ordenação:
		Filtrar por categoria
		Ordenar por nome (A-Z ou Z-A)
		Ordenar por quantidade
		Ordenar por preço
	Atualizar Produto (nome, categoria, quantidade ou preço)
	Excluir Produto
	Buscar Produto pelo ID ou parte do nome

Pré-requisitos

	Você precisa ter o Python 3.7 ou superior instalado na sua máquina.

Como Rodar a Aplicação Localmente

	Clone o Repositório
	Instale o Python (caso não esteja instalado)
	Execute o Script (agilstore.py)
	Siga o Menu de Opções da aplicação. Você pode selecionar a funcionalidade desejada.

Estrutura do Projeto

	raiz_do_projeto/
	|-- agilstore.py    # Arquivo principal da aplicação
	|-- produtos.json   # Arquivo para armazenamento dos dados dos produtos

Observações

	O arquivo "produtos.json" é criado automaticamente caso não exista, mas pode ser editado manualmente se necessário.
	Em caso de erros ou comportamentos inesperados, certifique-se de que o arquivo JSON esteja instalado na mesma pasta do script ou não esteja corrompido.
