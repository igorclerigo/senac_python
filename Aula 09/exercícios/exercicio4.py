from utils import soma
from utils import multiplicacao
from utils import divisao
from utils import subtracao

while True:
    opcao = int(input("Informe a opção desejada: (1/2/3/4/5)"))

    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))

    if opcao == 1:
        resultado = soma(num1, num2)
        print(resultado)

    elif opcao == 2:
        resultado = multiplicacao(num1, num2)
        print(resultado)

    elif opcao == 3:      
        resultado = divisao(num1, num2)
        print(resultado)

    elif opcao == 4:   
        resultado = subtracao(num1, num2)
        print(resultado)

    elif opcao == 5:
        print("Saindo do programa...")
        break

    else:
        print("Erro, opção inválida!")


