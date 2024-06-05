matriz_player = []
linha_player = [0] * 5

for y in range(5):
    matriz_player.append(linha_player)

print("Player round - informe as coordenadas...")
linha = int(input("Informe a linha (0-5): "))
coluna = int(input("Informe a coluna (0-5): "))

if (linha <= 4) and (coluna <= 4):
    matriz_player [linha][coluna] = "submarino"

else:
    print("Informe as coordenadas corretamente, isto é, de 0 a 5!")