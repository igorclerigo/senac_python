
entrada_de_dados = input("Informe cinco nomes para preencher a tupla: ").lower()
nomes = entrada_de_dados.split(",") # O split é um comando que leva a inferir que estamos tratando de uma lista
tupla_de_nomes = tuple(nomes)

if len(tupla_de_nomes) != 5:
    print("Você não respeitou a quantidade de elementos, refaça!")
else:
    
    checar_nomes = input("Informe o nome para checar se ele está presente na lista: ")

    if checar_nomes in tupla_de_nomes:
        print("O nome está na tupla.")
    else:
        print("O nome não está na tupla.")



# Esse código é uma representação do que um site faz, que é buscar no banco de dados se o usuário é válido, assim como o teste de validação de outras informações
        