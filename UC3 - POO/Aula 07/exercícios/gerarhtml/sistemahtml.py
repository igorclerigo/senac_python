nome_arquivo = "index.html"

with open(nome_arquivo, "w") as documento: 
        conteudo = """<!DOCTYPE html>\n <html lang="pt-br">\n <head>\n <meta charset="UTF-8">\n <meta name="viewport" content="width=device-width,initial-scale=1.0">\n <title></title>\n </head>"""
        titulo = """\n <body>\n <h1>CONSEGUI</h1>\n <body>"""

        documento.write(conteudo)
        documento.write(titulo)
                  
print(f"Arquivo '{documento}' criado com sucesso.")  