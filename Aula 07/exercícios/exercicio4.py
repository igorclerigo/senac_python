# Sistema de nascimento

nascimento = int(input("Informe aqui o ano de nascimento da pessoa: "))
ano_atual = int(input("Informe o ano em que estamos: "))
idade_atual = ano_atual - nascimento
 

for x in range (1, idade_atual + 1):
        idade_dinamica = nascimento + x
        print(f"Fulano tinha {x} ano(s) {idade_dinamica}")


"""ano = int(input("Qual o ano que vc nasceu?: "))
anoat = int(input("Qual o ano atual?"))
resultado = (anoat - ano)
atual = 0

for atual in range(1,resultado):
    print(f"No ano de {ano + atual} voce tinha {(atual-1)+ 1}")
"""