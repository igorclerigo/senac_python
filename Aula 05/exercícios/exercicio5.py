# Sistema para calcular distância

categoria = int(input("Senhor(a), me informe o número da categoria de serviço que gostaria de contratar: "))
distancia = float(input("Insira aqui a distância da corrida: "))

# Condicional para determinar a categoria

if categoria == 1:
    nomedacategoria = "Black"
    preco_final = distancia * 2
    print(f"Você selecionou {nomedacategoria}")
    print(f"O valor da corrida será de R${preco_final}!")

elif categoria == 2:
    nomedacategoria = "Confort"
    preco_final = distancia * 1.5
    print(f"Você selecionou {nomedacategoria}")
    print(f"O valor da corrida será de R${preco_final}!")
elif categoria == 3:
    nomedacategoria = "Convencional"
    preco_final = distancia * 1
    print(f"Você selecionou {nomedacategoria}")
    print(f"O valor da corrida será de R${preco_final}!")
elif categoria == 4:
    nomedacategoria = "Taxi"
    preco_final = distancia * 3
    print(f"Você selecionou {nomedacategoria}")
    print(f"O valor da corrida será de R${preco_final}!")
else:
    nomedacategoria = "uma categoria inválida"
    print(f"Você selecionou {nomedacategoria}")
# Exibindo o resultado
    




