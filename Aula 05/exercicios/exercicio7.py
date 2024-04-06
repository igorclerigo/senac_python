# Sistema de votação

idade = int(input("Por favor, informe sua idade: "))

if idade >= 16:
    print("Você pode votar, mas não é obrigado!")

elif 18 <= idade < 70: 
    print("Você é obrigado a votar.")

else:
    print("Você pode votar, mas não há o dever.")

 