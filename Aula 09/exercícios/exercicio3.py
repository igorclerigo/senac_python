# Sistema de juros simples
"""
emprestimo = float(input("Informe o valor do empréstimo: "))
taxa_de_juros = 8.33

taxa_anual = emprestimo * taxa_de_juros / 100 * 12
valor_com_taxa = taxa_anual + emprestimo
print(f"A taxa anual de juros será de R${taxa_anual} reais!")
print(f"O total a pagar ao longo de 12 meses será o valor de R${valor_com_taxa} reais!")
"""
from utils import dobro


# Entrada do usuário
valor_emprestado = float(input("Digite o valor que deseja emprestar: R$"))

# CALCULA O TOTAL A PAGAR COM JUROS DE 100% AO ANO
total_pagar = dobro(valor_emprestado)

# imprime o resultado
print(f"valor emprestado: R${valor_emprestado:.2f}. Total a pagar após um ano: R${total_pagar:.2f}.")
























