from armazenamento import ler_dados, salvar_dados
from validacao import entrada_obrigatoria, entrada_segura
import time

def cadastrar_produto():
    dados = ler_dados()
    id_produto = entrada_obrigatoria("Digite o ID do produto: ")
    if id_produto in dados:
        print("Produto já cadastrado!")
        return

    nome = entrada_obrigatoria("Digite o nome do produto: ")
    especificacoes = input("Digite as especificações do produto (opcional): ")
    quantidade = entrada_segura("Digite a quantidade do produto em estoque: ", int)
    descricao = entrada_obrigatoria("Digite uma descrição para o produto: ")
    
    dados[id_produto] = {
        'nome': nome,
        'especificações': especificacoes,
        'quantidade': quantidade,
        'descrição': descricao
    }

    salvar_dados(dados)
    print("Produto cadastrado com sucesso!")
    time.sleep(5)

def consultar_produto():
    dados = ler_dados()
    id_produto = input("Digite o ID do produto: ")
    produto = dados.get(id_produto)

    if produto:
        print(f"Detalhes do Produto:\n{json.dumps(produto, indent=4)}")
        time.sleep(5)
    else:
        print("Produto não encontrado!")
        time.sleep(5)

def listar_produtos():
    dados = ler_dados()
    if dados:
        print("Produtos Cadastrados:")
        for id_produto, produto in dados.items():
            print(f"{id_produto}: {produto['nome']}")
    else:
        
        print("Nenhum produto cadastrado.")
        time.sleep(5)

def atualizar_cadastro():
    dados = ler_dados()
    id_produto = input("Digite o ID do produto: ")
    
    if id_produto not in dados:
        print("Produto não encontrado!")
        time.sleep(5)
        return

    nome = input("Digite o novo nome do produto: ")
    especificacoes = input("Digite as novas especificações do produto: ")
    quantidade = input("Digite a nova quantidade do produto em estoque: ")
    descricao = input("Digite uma nova descrição para o produto (opcional): ")
    
    dados[id_produto] = {
        'nome': nome,
        'especificações': especificacoes,
        'quantidade': quantidade,
        'descrição': descricao
    }

    salvar_dados(dados)
    print("Cadastro atualizado com sucesso!")

def excluir_cadastro():
    dados = ler_dados()
    id_produto = input("Digite o ID do produto: ")
    if id_produto in dados:
        del dados[id_produto]
        salvar_dados(dados)
        print("Produto excluído com sucesso!")
        time.sleep(5)
    else:
        print("Produto não encontrado!")
        time.sleep(5)
    pass

# Funções restantes para consultar_produto, listar_produtos, etc.

