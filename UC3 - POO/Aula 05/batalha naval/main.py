# trello.com - metodologia ágil
# to do, doing, done, backlog (sprints de desenvolvimento)

# trello = quadros com cards dentro usados para organização do projeto
# dentro do card, vou "abrir o cartão" e dentro dessa opção, há múltiplas possibilidades, como adicionar comentários sobre o andamento do projeto ou manipular checklists e etiquetas.


import funcs

print("################################")
print("################################")
print("######## BATALHA NAVAL #########")
print("################################")
print("################################")
print()

# criação das matrizes globais que vão ser modificadas localmente dentro da função
matriz_cpu = funcs.matriz()
matriz_player = funcs.matriz()

funcs.pergunta(matriz_cpu)
funcs.numero_de_submarinos(matriz_player)
funcs.ataque_player(matriz_cpu)
funcs.ataque_cpu(matriz_player)








