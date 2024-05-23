print("Sistema de avaliação de revenda")
nota = 0
valor = 0
fipe = 10000
carro = int(input("Avalie o carro com notas de 0 a 100: "))

if (carro >= 0) and (carro <= 50):
    valor = fipe - fipe * (30/100)
    print(valor)

elif (carro > 50) and (carro <= 80):
    valor = fipe
    print(fipe)
    
elif (carro > 80) and (carro <= 100):
    valor = fipe + fipe * (20/100)
    print(valor)

else:
    print("Programa encerrado, digite um valor de 0 a 100!")