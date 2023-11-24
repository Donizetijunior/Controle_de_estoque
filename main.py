from menu import exibir_menu
from produto import cadastrar_produto, consultar_produto, listar_produtos, atualizar_cadastro, excluir_cadastro

def main():
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            consultar_produto()
        elif escolha == '3':
            listar_produtos()
        elif escolha == '4':
            atualizar_cadastro()
        elif escolha == '5':
            excluir_cadastro()
        elif escolha == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
