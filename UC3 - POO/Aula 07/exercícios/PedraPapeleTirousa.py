import random

def gerar_aleatorio():
    lista = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    escolha = random.choice(lista)
    return escolha
    
print("### PVP ###")

escolha1 = input("Informe se quer jogar (sim/nao): ")
if escolha1 == "sim":
   x = gerar_aleatorio()
else:
    print("Informe o comando correto!")

escolha2 = input("Informe se quer jogar (sim/nao): ")
if escolha2 == "sim":
   y = gerar_aleatorio()
else:
    print("Informe o comando correto!")


def determinar_vencedor(jogador1, jogador2):
    combinacoes_vencedoras = {
        "tesoura":["lagarto","papel"],
        "pedra":["lagarto","tesoura"],
        "papel":["pedra","spock"],
        "lagarto":["spock","papel"],
        "spock":["tesoura", "pedra"]                        
    }
        
    #if jogador1 in combinacoes_vencedoras[jogador1]:
        #print("O jogador 1 venceu!")
    #if jogador2 in combinacoes_vencedoras[jogador2]:
        #print("O jogador 2 venceu!")

    if jogador1 == jogador2:
        print("Empate!")
    elif jogador2 in combinacoes_vencedoras[jogador1]:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

determinar_vencedor(x,y)


    

    
