# Classificatória FORMULA 1

lista_corredores1, lista_tempo1 = [], []
lista_corredores2, lista_tempo2 = [], []
lista_corredores3, lista_tempo3 = [], []

sessoes = 0
corredores = 0

print("### CLASSIFICATÓRIA FORMULA 1 MAIO 2024 ###\n")

while sessoes == 0:
    print("OQ1")
    for itens in range(1,8):
        entrada_nome = input(f"Informe o nome do corredor de número {itens}: ")
        entrada_tempo = input(f"Informe o tempo recorde em horas conquistado pelo corredor {entrada_nome}: ")
        lista_corredores1.append(entrada_nome)
        lista_tempo1.append(entrada_tempo)
        lista_tempo1.sort()
        print(lista_corredores1, lista_tempo1)
        sessoes += 1

print()
while sessoes == 1:
    print("OQ2")
    for itens in range(1,6):
        entrada_nome = input(f"Informe o nome do corredor de número {itens}: ")
        entrada_tempo = input(f"Informe o tempo recorde em horas conquistado pelo corredor {entrada_nome}: ")
        lista_corredores2.append(entrada_nome)
        lista_tempo2.append(entrada_tempo)
        print(lista_corredores2, lista_tempo2)
        sessoes += 1

print()
while sessoes == 2:
    print("OQ3")
    for itens in range(1,4):
        entrada_nome = input(f"Informe o nome do corredor de número {itens}: ")
        entrada_tempo = input(f"Informe o tempo recorde em horas conquistado pelo corredor {entrada_nome}: ")
        lista_corredores3.append(entrada_nome)
        lista_tempo3.append(entrada_tempo)
        print(lista_corredores3, lista_tempo3)
        sessoes +=1

print(f"OQ1 {lista_corredores1,lista_tempo1}, OQ2 {lista_corredores2,lista_tempo2}, OQ3 {lista_corredores3,lista_tempo3}" )


# EXEMPLO DO PROFESSOR

""" 
print("Bem vindo ao Programa de Classificação")

lista_classificacion,lista_tempo = [], []
lista_classificacion1,lista_tempo1 = [], []
lista_classificacion2,lista_tempo2 = [], []

print("Digite o nome dos 7 primeiros pilotos e tempo da Q1")
for i in range(7):
    nome = input(f"Q1 Piloto {i+1}:")
    tempo = input(f"Q1 Tempo {i+1}:")
    lista_classificacion.append(nome)
    lista_tempo.append(tempo)
    print(f"O {lista_classificacion[i]} Ficou com o Tempo de {lista_tempo[i]}m")

print("Digite o nome dos 5 primeiros pilotos e tempo da Q2 ")
for i in range(5):
    nome = input(f"Q2 Piloto {i+1}:")
    tempo = input(f"Q2 Tempo {i+1}:")
    lista_classificacion1.append(nome)
    lista_tempo1.append(tempo)
    print(f"O {lista_classificacion1[i]} Ficou com o Tempo de {lista_tempo1[i]}m")

print("Digite o nome dos 3 primeiros pilotos e tempo da Q3 ")
for i in range(3):
    nome = input(f"Q3 Piloto {i+1}:")
    tempo = input(f"Q3 Tempo {i+1}:")
    lista_classificacion2.append(nome)
    lista_tempo2.append(tempo)
    print(f"O {lista_classificacion2[i]} Ficou com o Tempo de {lista_tempo2[i]}m")

print("\nResultados da Primeira Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo:
    print(f"{tempo:.2f} segundos", end=", ")

print("\nResultados da Segunda Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion1:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo1:
    print(f"{tempo:.2f} segundos", end=", ")

print("\nResultados da Terceira Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion2:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo2:
    print(f"{tempo:.2f} segundos", end=", ")
"""