# Limite do cartão de crédito

"""saldo_do_usuario = float(input("Informe o seu saldo: "))
limite_do_cartao = saldo_do_usuario * 2
print(f"O limite do seu cartão é de {limite_do_cartao} reais.")"""

# Aprendendo funções
from utils import dobro

# Entrada do usuário
limite_atual = float(input("Digite o limite atual do se ucartão de crédito: R$"))

# Calcula o novo limite
novo_limite = dobro(limite_atual)

# Imprime os resultados
print(f"Seu limite atual é de R${limite_atual:.2f}. Seu novo limite seria R${novo_limite:.2f}.")
