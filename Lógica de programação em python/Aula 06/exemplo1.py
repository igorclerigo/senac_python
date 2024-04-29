# Sistema de assinatura


idade = int(input("Digite sua idade: "))
assinante = input("Você é assinante do game pass (sim/não): ").lower()

if idade >= 18 and assinante == "sim":
    print("Você tem acesso ao game pass!")
else:
    print("Você não tem acesso ao game pass.")

# .lower() é uma função que vai transformar o que o usuário digitar em letras minúsculas, fazendo com que dê match com o valor esperado
# na variável assinante.
