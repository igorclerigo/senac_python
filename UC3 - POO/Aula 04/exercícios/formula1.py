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
        print(lista_corredores1, lista_tempo1)
    sessoes = sessoes + 1

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
    sessoes += 1

print(f"OQ1 {lista_corredores1,lista_tempo1}, OQ2 {lista_corredores2,lista_tempo2}, OQ3 {lista_corredores3,lista_tempo3}" )


# EXEMPLO DO PROFESSOR

""" 
classificatoria1= [], []
classificatoria2= [], []
classificatoria3 =[], []

# Coletando dados para a primeira classificatória com 7 pilotos
print("Digite o nome e o melhor tempo dos 7 pilotos da primeira classificatória (nome:tempo):")
for i in range(3):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]# matrizes para armazenar os dados das classificatórias

    tempo = float(entrada[1])
    classificatoria1.append(nome,tempo)


# Coletando dados para a segunda classificatória com 5 pilotos
print("Digite o nome e o melhor tempo dos 5 pilotos da segunda classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    classificatoria2.append(nome,tempo)

# Coletando dados para a terceira classificatória com 3 pilotos
print("Digite o nome e o melhor tempo dos 3 pilotos da terceira classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    classificatoria3.append(nome,tempo)

# Imprimindo as matrizes das classificatórias
print("\nResultados da Primeira Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria1:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria1:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Segunda Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria2:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria2:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Terceira Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria3:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria3:
    print(f"{tempo:.2f} segundos", end=", ")



"""