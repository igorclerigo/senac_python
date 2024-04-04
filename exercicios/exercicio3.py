#status aluno

nome = input ("Insira seu nome: ")
nome_disciplina = input ("Insira o nome da disciplina aqui:")
nota1 = float(input("Insira aqui a nota do primeiro bimestre: "))
nota2 = float(input("Insira aqui a nota do segundo bimestre: "))
nota3 = float(input("Insira aqui a nota do terceiro bimestre: "))
nota4 = float(input("Insira aqui a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#devo indicar o tipo de dado variavel no momento da declaração dela, pois ao tentar indicar tipo de dado já na média, ou seja, no resultado, não será uma indicação e sim uma conversão
#que ocorrerá de forma errada.
    
