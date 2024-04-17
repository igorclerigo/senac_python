# Sistema de votação

idade = int(input("Por favor, informe sua idade: "))

if idade < 16:
    print("Você ainda não está elegível para votar.")

elif 18 <= idade < 70: 
    print("Você é obrigado a votar.")

else:
    print("Você está elegível para votar, mas não é obrigatório.")

 