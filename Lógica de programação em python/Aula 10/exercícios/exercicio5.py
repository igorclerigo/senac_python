lista_atletas = []
numeroAtleta = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(10):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas.append(distancia)

for distanciaporatleta in lista_atletas:
    print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta += 1

lista_atletas.sort()
lista_atletas.reverse()
print("Lançamentos ordenados:", lista_atletas)

lista_atletas = []
numeroAtleta = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(6):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas.append(distancia)

for distanciaporatleta in lista_atletas:
    print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta += 1
lista_atletas.sort()
lista_atletas.reverse()
print("Lançamentos ordenados:", lista_atletas)

# final diferente, sem criar uma nova lista!
lista_atletas = []
numeroAtleta = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(4):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas.append(distancia)

for distanciaporatleta in lista_atletas:
    print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta += 1
lista_atletas.sort()
lista_atletas.reverse()
print("Lançamentos ordenados:", lista_atletas)
