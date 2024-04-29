# Décimo terceiro salário

"""salario = float(input("Informe o seu salário: "))
salario13 = salario 
print(f"O seu décimo terceiro salário é de {salario13} reais.")"""

import utils

# Entrada do usuário
salario_mensal = float(input("Digite o seu salário mensal: R$"))

# Calcula o valor a receber no mês do 13º
valor_recebido = utils.dobro(salario_mensal)


# Imprime o resultado
print(f"Seu salário mensal é de R${salario_mensal:.2f}. você receberá R${valor_recebido:.2f} como 13º salário.")
