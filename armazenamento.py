import json

ARQUIVO_DADOS = 'produtos.json'

def ler_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de dados. Verifique o formato do arquivo.")
        return {}
    except Exception as e:
        print(f"Erro desconhecido ao ler o arquivo: {e}")
        return {}
    pass

def salvar_dados(dados):
    try:
        with open(ARQUIVO_DADOS, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
    pass
