from flask import Flask, request, render_template, send_file
import os
import PIL.Image
import google.generativeai as genai
import mysql.connector

app = Flask(__name__)

# Configuração do GemAI
genai.configure(api_key="AIzaSyAUjnJX5IetZFKMss7J6PuXfQQapKZuKB0")

# Função para análise de imagem
def analyze_image(image_path):
    img = PIL.Image.open(image_path)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["O meu banco de dados está estruturado com uma tabela chamada produtos e possui duas colunas, são elas: categoria de roupa e cor de roupa. eu quero que você analise a cor e a categoria da roupa, se é um casaco, calça ou tênis e qual é a cor. Me devolva uma consulta em mysql que mostre roupas que combinem", img])
    return response.text

# Função para executar a consulta SQL no banco de dados
def execute_query(query):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="moda"
    )
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

# Rota para a página inicial com o formulário de upload
@app.route("/")
def index():
    return render_template("index.html")

# Rota para processar o upload da imagem
@app.route("/upload", methods=["POST"])
def upload_file():
    # Verifica se foi enviado um arquivo
    if 'file' not in request.files:
        return "Nenhum arquivo enviado!"

    file = request.files['file']

    # Verifica se o arquivo é um arquivo de imagem
    if file.filename == '':
        return "Nenhum arquivo selecionado!"

    # Diretório para salvar o arquivo
    upload_folder = os.path.join(app.root_path, "uploads")

    # Cria o diretório se não existir
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Caminho completo do arquivo
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Realiza a análise da imagem
    analysis_result = analyze_image(file_path)

    # Executa a consulta no banco de dados
    query = analysis_result.strip()  # Certifique-se de que a consulta está no formato correto
    db_results = execute_query(query)

    # Verifica se há resultados
    if not db_results:
        return "Nenhuma roupa encontrada que combine."

    # Busca o caminho da imagem da primeira roupa que combina
    image_path = db_results[0][2]  # Assumindo que o caminho da imagem está na terceira coluna

    # Retorna a imagem da roupa que combina
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)


# TIPOS DE ROUPA
roupa1_tipo = "camisa"
roupa2_tipo = "calça"
roupa3_tipo = "tênis"

# CORES
cor1_ton1 = "vermelho"
cor1_ton2 = "verde"
cor1_ton3 = "azul"

# Peças de roupa e cores a serem avaliadas
peca1_tipo = "camisa"
cor1 = "vermelho"
peca2_tipo = "calça"
cor2 = "verde"
peca3_tipo = "tênis"
cor3 = "azul"

# Avaliação de tipo de roupa
tipo_combina = False

if (peca1_tipo == roupa1_tipo and peca2_tipo == roupa2_tipo) or (peca1_tipo == roupa2_tipo and peca2_tipo == roupa3_tipo) or (peca1_tipo == roupa1_tipo and peca2_tipo == roupa3_tipo):
    tipo_combina = True
elif (peca2_tipo == roupa1_tipo and peca3_tipo == roupa2_tipo) or (peca2_tipo == roupa2_tipo and peca3_tipo == roupa3_tipo) or (peca2_tipo == roupa1_tipo and peca3_tipo == roupa3_tipo):
    tipo_combina = True
elif (peca1_tipo == roupa1_tipo and peca3_tipo == roupa2_tipo) or (peca1_tipo == roupa2_tipo and peca3_tipo == roupa3_tipo) or (peca1_tipo == roupa1_tipo and peca3_tipo == roupa3_tipo):
    tipo_combina = True

# Avaliação de cor
cor_combina = False

if (cor1 == cor1_ton1 and cor2 == cor1_ton2) or (cor1 == cor1_ton2 and cor2 == cor1_ton3) or (cor1 == cor1_ton1 and cor2 == cor1_ton3):
    cor_combina = True
elif (cor2 == cor1_ton1 and cor3 == cor1_ton2) or (cor2 == cor1_ton2 and cor3 == cor1_ton3) or (cor2 == cor1_ton1 and cor3 == cor1_ton3):
    cor_combina = True
elif (cor1 == cor1_ton1 and cor3 == cor1_ton2) or (cor1 == cor1_ton2 and cor3 == cor1_ton3) or (cor1 == cor1_ton1 and cor3 == cor1_ton3):
    cor_combina = True

# Resultado da avaliação
if tipo_combina and cor_combina:
    resultado = "Combinação Ideal!"
elif tipo_combina:
    resultado = "Combinação de Tipo Ok"
elif cor_combina:
    resultado = "Combinação de Cor Ok"
else:
    resultado = "Combinação Não Recomendada"

print(resultado)

