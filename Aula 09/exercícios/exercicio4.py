# tem como chamar as funções pelo nome do arquivo.
# 



from utils import dobro
from utils import soma
from utils import multiplicacao
from utils import divisao
from utils import subtracao


while True:
    
    opcao = int(input("Informe a opção desejada: (1/2/3/4/5)"))

    if opcao == 1:
        num1 = int(input("Informe o primeiro número: "))
        num2 = int(input("Informe o segundo número: "))
        resultado = soma(num1, num2)
        print(resultado)

    elif opcao == 2:
        num1 = int(input("Informe o primeiro número: "))
        num2 = int(input("Informe o segundo número: "))
        resultado = multiplicacao(num1, num2)
        print(resultado)

    elif opcao == 3:
        num1 = int(input("Informe o primeiro número: "))
        num2 = int(input("Informe o segundo número: "))
        resultado = divisao(num1, num2)
        print(resultado)

    elif opcao == 4:
        num1 = int(input("Informe o primeiro número: "))
        num2 = int(input("Informe o segundo número: "))
        resultado = subtracao(num1, num2)
        print(resultado)

    elif opcao == 5:
        break

    else:
        print("Erro, número inválido!")


