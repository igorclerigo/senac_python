import random
def matriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(0)
        matriz.append(linha)
    return matriz

def pergunta(matriz_cpu):
    while True:
        pergunta_submarino = input("Foi criada uma matriz, o que deseja fazer? Digite '1' para adicionar um submarino à um local aleatório na matriz ou 'passar' para passar a vez ao jogador ou 'sair' para fechar o jogo: ")

        if pergunta_submarino == '1':
            matriz_cpu = matriz()
            linha_submarino = random.randint(0,4)
            coluna_submarino = random.randint(0,4)

            matriz_cpu [linha_submarino][coluna_submarino] = "submarino"

            print() # QUEBRA DE LINHA ORGANIZACIONAL
            print("Matriz CPU")
            for linha in matriz_cpu:
                print(linha)
            break

        elif pergunta_submarino == "passar":
            print("Esta foi a matriz da CPU, passando a vez ao jogador...")
            break

        elif pergunta_submarino == "sair":
            print("Jogo encerrado.")
            quit()
        else:
            print("Opção inválida, tente novamente.")



def numero_de_submarinos(matriz_player):
    num_submarinos = 0
    while num_submarinos < 4:

        print("Player round - informe as coordenadas...")
        linha = int(input("Informe a linha (0-4): "))
        coluna = int(input("Informe a coluna (0-4): "))

        if (linha <= 4) and (coluna <= 4):
            if matriz_player[linha][coluna] == 0:
                print("Você indicou as coordenadas corretamente, o submarino se encontra na posição informada, conforme abaixo:")
                matriz_player [linha][coluna] = "submarino"
                num_submarinos += 1
            else:
                print("Já existe um submarino nesta posição, escolha outra posição.")

        else:
            print("Informe as coordenadas corretamente, isto é, de 0 a 4!")

# MATRIZ OUTPUT
        print("Matriz Jogador")
        for linha in matriz_player:
            print(linha)

        if num_submarinos < 4:
            continuar = input(f"Deseja adicionar outro submarino à matriz? (s/n) - Você pode adicionar mais {4 - num_submarinos} submarinos: ")
        if continuar.lower() != 's':
            break

    if num_submarinos == 4:
        print("Você chegou ao limite de submarios, portanto, não pode adicionar mais")


def ataque_player(matriz_cpu):
    print("Round de Ataque do Jogador")
    print("informe as coordenadas para selecionar o espaço na matriz...")
    linha = int(input("Informe a linha (0-4): "))
    coluna = int(input("Informe a coluna (0-4): "))

    if (linha <= 4) and (coluna <= 4):
        if matriz_cpu [linha][coluna] == "submarino":
            print("Você acertou o submarino do inimigo (CPU)!")
            matriz_cpu [linha][coluna] = "X"
            for linha in matriz_cpu:
                print(linha)
        else:
            print("Você errou, não havia submarino nesta posicão!")
            matriz_cpu [linha][coluna] = "A"
            for linha in matriz_cpu:
                print(linha)


def ataque_cpu(matriz_player):
    print("Round de Ataque do CPU")
    linha = random.randint(0,4)
    coluna = random.randint(0,4)

    if (linha <= 4) and (coluna <= 4):
        if matriz_player [linha][coluna] == "submarino":
            print("Você acertou o submarino do inimigo (Jogador)!")
            matriz_player [linha][coluna] = "X"
            for linha in matriz_player:
                print(linha)
        else:
            print("A CPU errou, não havia submarino do jogador nesta posicão!")
            matriz_player [linha][coluna] = "A"
            for linha in matriz_player:
                print(linha)