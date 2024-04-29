# exercício horário

hora_atual = int(input("Me informe as horas abaixo: "))

# verficando se está fora do horário do expediente
if hora_atual < 8 or hora_atual >= 18:
    print("Erro. você está fora do expediente e não pode acessar o sistema.")
else:
    # se estiver dentro do horário de expediente, preosseguir com a agenda
    for hora in range(hora_atual, 18):
        atividade = input(f"O que você vai fazer às {hora} horas? ")

# eu tinha feito o for com 8, 18 e ta errado pois o horário fica fixo e não de acordo com a hora que o usuário chega no trabalho.