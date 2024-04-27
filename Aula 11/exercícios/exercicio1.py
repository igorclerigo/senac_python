tentativas = 3
tesouro = 0
contador = 0

while contador < tentativas:
    contador += 1
    tesouro = int(input("Informe a posição que deseja tentar: "))
    if tesouro == 3:
        print("Você achou! O tesouro estava na casa 3!")
        break
    
    print(f"Você errou. {tentativas} chances sobrando!")
    
if tentativas == 0:
    print("Você esgotou as tentativas. programa encerrando...")
        
    












"""
tesouro = 0
tentativas = 3

while tesouro != 3:
    for tentativas in range(4,0,-1):
        print(tentativas)
        if tentativas == 1:
            print("Você esgotou as tentativas. programa encerrando...")
            quit()
        else:
            tesouro = int(input("Informe a posição que deseja tentar: "))
            tentativas -= 1
            print(f"Você errou. {tentativas} chances sobrando!")
            lista_tesouro.append(tesouro)
    #print(lista_tesouro)

print("Você achou! O tesouro estava na casa 3!")"""