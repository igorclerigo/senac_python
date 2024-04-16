# Sistema de juros simples

"""emprestimo = float(input("Informe o valor do empréstimo: "))
taxa_de_juros = 8.33

valor = emprestimo * taxa_de_juros / 100 * 12
valor1 = valor + emprestimo
print(f"O juros será de {valor} reais!")
print(f"O valor total será de {valor1} reais!")"""

from utils import dobro


# Entrada do usuário
valor_emprestado = float(input("Digite o valor que deseja emprestar: R$"))

# cALCULA O TOTAL A PAGAR COM JUROS DE 100% ao ano
total_pagar = dobro(valor_emprestado)

# imprime o resultado
print(f"valor empresado: R${valor_emprestado:.2f}. Total a pagar após um ano: R${total_pagar:.2f}.")
























