# Sistema para transporte de aplicativo

categoria = int(input("Senhor(a), me informe o número da categoria de serviço que gostaria de contratar: "))

# Condicional para determinar a categoria

if categoria == 1:
    nomedacategoria = "Black"

elif categoria == 2:
    nomedacategoria = "Confort"

elif categoria == 3:
    nomedacategoria = "Convencional"

elif categoria == 4:
    nomedacategoria = "Taxi"

else:
    nomedacategoria = "Erro, categoria inválida"

# Exibindo o resultado
    
print(f"Você selecionou {nomedacategoria}")



