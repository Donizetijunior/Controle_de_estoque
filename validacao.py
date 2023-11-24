def entrada_obrigatoria(prompt):
    """ Solicita ao usuário uma entrada que não pode ser vazia. """
    while True:
        entrada = input(prompt)
        if entrada.strip():
            return entrada
        print("Este campo é obrigatório. Por favor, preencha-o.")
    pass

def entrada_segura(prompt, tipo=str):
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print(f"Por favor, insira um valor válido de tipo {tipo.__name__}.")
    pass
