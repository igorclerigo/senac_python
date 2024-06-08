solicitacao_nome = input("Informe seu nome: ")
nome_arquivo = f"{solicitacao_nome}_info.txt"

with open(nome_arquivo, "w") as documento: 
    # abrindo o arquivo com "w" ele vai sobreescrever toda vez, isto é, toda vez que eu executar o arquivo, ele vai ser cleanado para eu poder adicionar novas informaçoes.
    # abrindo o arquivo com "a" ele vai salvar a informação sem sobreescrever a anterior, as informações da execução anterior vão ser mantidas.
        solicitacao_experiencia = input("Informe suas experiências profissionais: ")
        solicitacao_endereco = input("Informe seu endereço: ")
        conteudo_nome = solicitacao_nome
        conteudo_experiencia = solicitacao_experiencia
        conteudo_endereco =  solicitacao_endereco 

        documento.write(f"Nome: {solicitacao_nome}" + "\n")
        documento.write(f"Experiência profissional: {solicitacao_experiencia}" + "\n")
        documento.write(f"Endereço: {solicitacao_endereco}" + "\n")            
print(f"Arquivo '{documento}' criado com sucesso.")  