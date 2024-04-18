
quantidade_de_alunos = int(input("Quantos alunos possuem nesta turma? "))

lista = []


for i in range(quantidade_de_alunos):
    nome = input(f"A turma possui {quantidade_de_alunos} alunos. Digite o nome de cada um deles abaixo: \n").lower()
    lista.append(nome)


repetido1 = input("Informe o nome para saber quantas vezes ele foi posto na lista: ").lower()
repetido2 = input("Informe o nome para saber quantas vezes ele foi posto na lista:").lower()
contagem1 = lista.count(repetido1)
contagem2 = lista.count(repetido2)

print(f"Os elementos {repetido1} e {repetido2} aparecem {contagem1} e {contagem2} vezes na lista, respectivamente.")


"""
# Perguntar quantos alunos tem na turma
numero_alunos = int(input("Quantos alunos tem na turma? "))

# Criar uma lista para armazenar os nomes dos alunos
lista_alunos = []

# Inserir os nomes dos alunos na lista
print("Por favor, insira os nomes dos alunos:")
for i in range(numero_alunos):
    nome = input(f"Nome do aluno {i + 1}: ").lower() # Convertendo para minúsculas antes de adicionar
    lista_alunos.append(nome)

# Contar quantos "Enzo" e "Valentina" estão na lista
contagem_enzo = lista_alunos.count("enzo")
contagem_valentina = lista_alunos.count("valentina")

# Exibir resultados
print(f"Total de alunos na turma: {numero_alunos}")
print(f"Quantidade de alunos chamados Enzo: {contagem_enzo}")
print(f"Quantidade de alunos chamados Valentina: {contagem_valentina}") """