num_livros = int(input("Quantos títulos deseja guardar?"))

with open('UC3 - POO\Aula 05\livros.txt', "w") as documento:

    for _ in range(num_livros):
        nome_livro = input("Informe o nome do livro: ")
        nome_autor = input("Informe o nome do Autor: ")
        conteudo_livro = nome_livro
        conteudo_autor = nome_autor
        documento.write(f"Livro: {conteudo_livro}" + "\n")
        documento.write(f"Autor: {conteudo_autor}" + "\n")
print(f"Arquivo '{documento}' criado com sucesso.")  

"""
# Especificar o nome do arquivo e o conteúdo
nome_arquivo = 'exemplo.txt'
conteudo = 'Este é um exemplo de conteúdo.'

# Abrir o arquivo no modo de escrita e escrever o conteúdo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(conteudo)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
--------------------------------------------------------------------------------------
# Especificar o nome do arquivo e as informações dos livros
nome_arquivo = 'livros.txt'
num_novos_livros = input("\nDeseja adicionar livros? (sim/não): ").lower()

with open(nome_arquivo, 'a') as arquivo:
    while num_novos_livros != "não" or "n" or "no" or "nao":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        arquivo.write(f"Título: {titulo}, Autor: {autor}\n")
        num_novos_livros = input("\nDeseja adicionar mais livros? (sim/não): ").lower()

print(f"\nNovas informações adicionadas ao arquivo '{nome_arquivo}'.\n")"""