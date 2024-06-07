# trello.com - metodologia ágil
# to do, doing, done, backlog (sprints de desenvolvimento)

# trello = quadros com cards dentro usados para organização do projeto
# dentro do card, vou "abrir o cartão" e dentro dessa opção, há múltiplas possibilidades, como adicionar comentários sobre o andamento do projeto ou manipular checklists e etiquetas.

import random

print("################################")
print("######## BATALHA NAVAL #########")

# CRIAÇÃO DE MATRIZ DA CPU
matriz_cpu = []

# LOOP ANINHADO PARA CRIAR NOVA LISTA E ADICIONAR CINCO ZEROS DENTRO DELA E DEPOIS ADICIONAR ESSA LISTA À MATRIZ
for _ in range(5): # ESSE FOR LOOP REPRESENTA AS LINHAS DA MATRIZ
    linha_cpu = []
    for x in range(5): # ESSE FOR LOOP REPRESENTA AS COLUNAS DA MATRIZ
        linha_cpu.append(0)
    matriz_cpu.append(linha_cpu)

print() # QUEBRA DE LINHA ORGANIZACIONAL

# MATRIZ OUTPUT
print("Matriz CPU")
for linha in matriz_cpu:
    print(linha)


# SOLICITAÇÃO DE AÇÃO DO USUÁRIO
while True:
    pergunta_submarino = input("Foi criada uma matriz, o que deseja fazer? Digite '1' para adicionar um submarino à um local aleatório na matriz ou 'passar' para passar a vez ao jogador ou 'sair' para fechar o jogo: ")

    if pergunta_submarino == '1':
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


# CRIAÇÃO DE MATRIZ DO JOGADOR
matriz_player = []

# LOOP ANINHADO PARA CRIAR NOVA LISTA E ADICIONAR CINCO ZEROS DENTRO DELA E DEPOIS ADICIONAR ESSA LISTA À MATRIZ
for i in range(5): # ESSE FOR LOOP REPRESENTA AS LINHAS DA MATRIZ
    linha_player = []

    for y in range(5): # ESSE FOR LOOP REPRESENTA AS COLUNAS DA MATRIZ
        linha_player.append(0)
    matriz_player.append(linha_player)

# MATRIZ OUTPUT
print("Matriz Jogador")
for linha in matriz_player:
    print(linha)

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



