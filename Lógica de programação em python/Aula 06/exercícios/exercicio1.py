# Sistema de passagem - usuário vip

cartao_black = input("Senhor, você possui o cartão black? (sim/não): ").lower()
ingresso_vip = input("Senhor, você comprou o ingresso vip? (sim/não): ").lower()

if cartao_black == "sim" or ingresso_vip == "sim":
    print("Você possui acesso a sala vip!")
else:
    print("Você não possui acesso a sala vip :(. Compre aqui: link o ingresso vip")