# Sistema de prova de lançamento


# declaração de variáveis
lista_atletas = []
numeroAtleta = 1
numero_rodadas = 0

# entrada de dados do usuário
print("Por favor, insira a distância dos lançamentos: \n")

# loops


while numero_rodadas == 0:
# no range de 1 a 10 vai pedir a distância e sempre loopando "i" que é a variável temporária que representa o número de atletas de 1 até 10 (sao 10 atletas)
    print("round 01")
    for i in range(1,11):
        distancia = float(input(f"O atleta {i} fez o lançamento a qual distância?: "))
        lista_atletas.append(distancia)
    
# espaço
    print()

# percorre cada item da lista, que é a distância informada no loop anterior e passada pra dentro da lista pelo método append.
    for distanciaporatleta in lista_atletas:
        print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
        numeroAtleta += 1
    numero_rodadas += 1
    

    lista_atletas.sort()
    lista_atletas.reverse()
    print("Lançamentos ordenados:", lista_atletas)

while numero_rodadas == 1:
    print("round 02")
    for i in range(1,7):
        distancia = float(input(f"O atleta {i} fez o lançamento a qual distância?: "))
        lista_atletas.append(distancia)

    print()
    
    for distanciaporatleta in lista_atletas:
        print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
        numeroAtleta += 1
        numero_rodadas += 1
    
    lista_atletas.sort()
    lista_atletas.reverse()
    print("Lançamentos ordenados:", lista_atletas[:6])

else:
    print("round 03")
    for i in range(1,5):
        distancia = float(input(f"O atleta {i} fez o lançamento a qual distância?: "))
        lista_atletas.append(distancia)

    print()
    
    for distanciaporatleta in lista_atletas:
        print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
        numeroAtleta += 1
        
    lista_atletas.sort()
    lista_atletas.reverse()
    print("Lançamentos ordenados:", lista_atletas[:4])
