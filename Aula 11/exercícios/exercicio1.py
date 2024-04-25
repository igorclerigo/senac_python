lista_tesouro = []

tesouro = 0
tentativas = 3

while tesouro != 3:
    tesouro = int(input("Informe a posição que deseja tentar: "))
    tentativas -= 1
    print(f"Você errou. {tentativas} chances sobrando!")
    lista_tesouro.append(tesouro)
    print(lista_tesouro)
    if tentativas == 0:
        print("Você esgotou as tentativas. programa encerrando...")
        exit()
