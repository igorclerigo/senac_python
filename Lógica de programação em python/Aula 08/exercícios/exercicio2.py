# Sistema de soma

# meu jeito
"""soma = 0

while True:
    num1 = int(input("Insira a opção desejada: (1, 2 ou 3) "))
    
    if num1 == 1:
        num2 = int(input("Digite um número que deseja somar com 1: "))
        soma = soma + num2
        print(soma)
    elif num1 == 2:
        print(soma)
    elif num1 == 3:
        break
    else:
        print("número inválido")"""

soma = 0 # inicializa a variável de soma dos números
continuar = True

while continuar:
    print("\nMenu:")
    print("1 - Adicionar um numero à soma: ")
    print("2 - Exibir soma atual: ")
    print("3 - Sair")
    opcao = input("Escolha sua opção (1, 2 ou 3): ") #recebe o valor do usuário

    if opcao == "1":
        numero = float(input("Digite um número para adicionar à soma: "))
        if numero > 0:
            soma += numero  # Adiciona o número à soma total
            print(f"Número {numero} adicionado à soma.")
        else:
            print("Numero invalido")
    
    elif opcao == "2":
        print(f"Soma atual: {soma}") # exibe a soma atual
    
    elif opcao == "3":
        continuar = False # altera o valor da variável de controle para false para sair do loop

    else:    
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.") # mensagem para opção errada.

print("Programa encerrado. Soma final: ", soma) # exibe a soma final quando o loop termina. 

            

