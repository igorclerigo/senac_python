# Sistema para loja de tapete

tipo_de_tapete = input("Qual tipo de tapete você deseja comprar? ")

# gambiarra
#if tipo_de_tapete != "convencional" or "premium" or "maxpremium":
    #print("não existe este tipo de tapete")
    #exit()
metragem = int(input("Quantos metros de tapete você deseja comprar? "))

if tipo_de_tapete == "convencional":
    metragem = metragem * 10
    print(f"O valor do orçamento desejado para a compra do tapete {tipo_de_tapete} é de R${metragem}!")

elif tipo_de_tapete == "premium":
    metragem = metragem * 20
    print(f"O valor do orçamento desejado para a compra do tapete {tipo_de_tapete} é de R${metragem}!")

elif tipo_de_tapete == "maxpremium":
    metragem = metragem * 30
    print(f"O valor do orçamento desejado para a compra do tapete {tipo_de_tapete} é de R${metragem}!")

else:
    print("Não será possível realizar um orçamento, visto que não vendemos este tipo de tapete!")









