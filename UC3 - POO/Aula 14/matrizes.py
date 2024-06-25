import random 

matriz = []
for _ in range(3):
    linha = []
    for _ in range(3):
        linha.append(random.randint(0,20))
    matriz.append(linha)

for linha in matriz:
    print(linha)

for linha in matriz:
    for _ in linha:
        if _ > 10:
            print(_)
    

"""
PROFESSOR:
pip install numpy

import numpy as np

#Cria uma matriz 3x3 com valores aleatórios entre 0 e 20
matriz = np.random.randint(0,21, size=(3,3))   

#Exibe a matriz completa
print("Matriz completa:")
print(matriz)

# Filtra e exibe os valores maiores que 10
valores_maiores_que_10 = matriz[matriz > 10]
print(valores_maiores_que_10)


"""