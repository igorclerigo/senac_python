while True: #loop infinito
    entrada = input("Digite cinco nomes separados por vírgulas: ")
    nomes = entrada.split(",")

    if len(nomes) == 5:
        nome_inserido = input("Digite um nome para verificar se está na tupla: ")
        if nome_inserido in nomes:
            print("O nome está na tupla.")
            break
        else:
            print("O nome não está na tupla.")
            break
    else:
        print("Erro. Por favor, insira 5 nomes")