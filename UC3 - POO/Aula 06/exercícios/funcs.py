def exibir():
    print("Olá")

exibir()

def exibir1(nome):
    print(nome)

exibir1(nome="igor")

def exibir2(nome ="igor"):
    print(nome)

exibir2("pikaa")


def total(numeros):
    return sum(numeros)

print(total([10, 1]))


def carros(tipo, nome):
    print(tipo, nome)

carros(**{"tipo":"BMW", "nome":"320i"   })      