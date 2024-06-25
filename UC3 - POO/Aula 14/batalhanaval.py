import numpy as np

print("################################")
print("################################")
print("######## BATALHA NAVAL #########")
print("################################")
print("################################")
print()



def jogo_batalha_naval():
    tabuleiro = np.zeros((5, 5), dtype=int)
    posicao_navio = (np.random.randint(0, 5), np.random.randint(0, 5))
    tentativas = 0
    max_tentativas = 2
    acertou = False
    
    while not acertou and tentativas <= max_tentativas:
        print("\nTabuleiro:")
        print(tabuleiro)
        linha = int(input("Adivinhe a linha (0-4): "))
        coluna = int(input("Adivinhe a coluna (0-4): "))
        if linha <= 4 and coluna <= 4:
            max_tentativas -= 1
            if (linha, coluna) == posicao_navio:
                print(f"Você acertou o navio em {tentativas} tentativas!")
                acertou = True
            else:
                tabuleiro[linha, coluna] = -1
                print(f"Errou! restam {max_tentativas} tentativas")
        else: 
            print("Opção inválida, tente novamente.")
    



def pergunta():
    while True:
        pergunta_submarino = input("Foi criada uma matriz, o que deseja fazer? Digite 'jogar' para jogar ou 'sair' para fechar o jogo: ")

        if pergunta_submarino == 'jogar':
            jogo_batalha_naval()

        elif pergunta_submarino == "sair":
            print("Jogo encerrado.")
            quit()
        else:
            print("Opção inválida, tente novamente.")

pergunta()
