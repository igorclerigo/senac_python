cliente = input("Digite o nome do novo cliente para que ele seja cadastrado no sistema: ").lower()
arquivo = f"{cliente}_cadastro.txt"

campos = [
    "Nome completo",
    "Telefone",
    "e-mail",
    "CPF"
]

dados_cadastro = {}
for campo in campos:
    valor = input(f"Digite seu {campo.lower()}: ")
    if campo in ["Telefone", "CPF"]:
        valor = int(valor)
    dados_cadastro[campo] = valor

# Salva os dados no arquivo
with open(arquivo, 'w') as f:
    for campo, conteudo in dados_cadastro.items():
        f.write(f"{campo}: {conteudo}\n")
print(f"Currículo salvo em {arquivo}")

# R: Nome completo, telefone, e-mail e CPF
# R: Não, variados
# R: Sim, o CPF
