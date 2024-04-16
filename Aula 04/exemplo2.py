# Aqui acontece entrada de dados informando ao PC que o tipo de dado atribuido a variável idade será um inteiro
# teste de condição com if e else

nome = input ("digite seu nome: ")
sobrenome = input ("digite seu sobrenome: ")
assento = input ("Entre com o número do assento: ") 
idade = int(input("Entre com a idade: "))

if idade > 16: #operador aritmético
    print(f"Ticket para o filme Velozes e Furiosos\nCliente: {nome} {sobrenome}\nAssento: {assento}")

else:
    print("Ingresso não poderá ser emitido")

# caso a condição apresentada não seja respeitada, o programa irá mostrar na tela o valor (cadeia de caracteres, tipo literal) 
# printado após o else.

# O uso do f facilita tudo, com isso, não precisarei abrir e fechar aspas a todo momento e não vou necessitar concatenar as variáveis.
# O uso de chaves {} serve para chamar as variáveis dentro do print, isto é, no momento de saída de dados.
# o \n é a quebra de linha.

