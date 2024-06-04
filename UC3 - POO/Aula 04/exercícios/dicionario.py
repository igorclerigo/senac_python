# Criando o dicionário de inventário
inventario = {"maçãs": 30, "bananas": 45, "laranjas": 25}

while True:
    acao = input("Digite 'adicionar' para acrescentar o estoque, 'mostrar' para ver o inventário, 'remover' para remover um produto, 'adição' para adicionar um novo produto, 'diminuir' para diminuir o estoque de um produto em específico e 'sair' para sair: ")
    
    if acao == 'sair':
        break
    elif acao == 'adicionar':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        
        if produto in inventario:
            inventario[produto] += quantidade
            print(f"Estoque de {produto} atualizado para {inventario[produto]}.")
        else:
            print("Produto não encontrado no inventário.")

    elif acao == 'remover':
        produto = input("Digite o nome do produto que deseja remover completamente do inventário: ")

        if produto in inventario:
            del inventario[produto]
            print(f"{produto} foi removido do inventário.")
        else:
            print("Produto não encontrado no inventário.")

    elif acao == 'adição':
        produto = input("Digite o nome do produto que deseja adicionar ao inventário: ")
        inventario[produto] = dict()
        print(f"{produto} foi adicionado ao inventário.")

        quantidade = input("Digite a quantidade do produto que deseja adicionar ao inventário: ")
        inventario[produto] = quantidade
        print(f"Estoque de {produto} atualizado para {inventario[produto]}.")

    elif acao == 'mostrar':
        print("Inventário Atualizado:")
        for produto, estoque in inventario.items():
            print(f"{produto}: {estoque} unidades")

    elif acao == 'diminuir':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        
        if produto in inventario:
            inventario[produto] = 0  # ou [quantidade] -= quantidade
            print(f"Estoque de {produto} atualizado para {inventario[produto]}.")


# Exibindo o inventário final
print("Inventário Final:")
for produto, estoque in inventario.items():
    print(f"{produto}: {estoque} unidades")
