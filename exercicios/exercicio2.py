#sistema de cadastro de turma

nome_curso = input ("Insira aqui o nome do curso: ")
quantidade_alunos = int(input("Insira aqui a quantidade alunos presentes no curso: "))

if quantidade_alunos >= 5:
    print(f"O curso de {nome_curso} iniciará no prazo de 05 dias, visto que {quantidade_alunos} pessoas se cadastraram para tal!")

else:
    print(f"O curso de {nome_curso} não iniciará, pois não obtivemos a quantidade mínima de {quantidade_alunos} alunos.")

    