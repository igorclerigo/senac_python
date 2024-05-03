# TESTE FOR-ELSE (RESOLUÇÃO CHAT GPT)
lista_tesouro = [1,2,3,4,5,6,7,8,9,10] # ÍNDICES = 0 a 9
TESOURO = 5
tentativas = 3

for _ in range(tentativas):
    escolha = int(input("Informe a posição que deseja tentar: "))
    tentativas -= 1
    if escolha == TESOURO:
        print("Parabéns, você achou o tesouro!")
        break
    else:
        print(f"Você errou. {tentativas} chances sobrando!")
else:
    print("Você esgotou suas chances. Programa encerrando...")
