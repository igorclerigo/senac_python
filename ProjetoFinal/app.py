from flask import Flask, request, render_template, send_file
import os
import PIL.Image
import google.generativeai as genai

app = Flask(__name__)

# Configuração do GemAI
genai.configure(api_key="AIzaSyAUjnJX5IetZFKMss7J6PuXfQQapKZuKB0")

# Função para análise de imagem
def analyze_image(image_path):
    img = PIL.Image.open(image_path)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["O meu banco de dados está estruturado com uma tabela chamada produtos e possui duas colunas, são elas: categoria de roupa e cor de roupa. eu quero que você analise a cor e a categoria da roupa, se é um casaco, calça ou tênis e qual é a cor. Me devolva uma consulta em mysql que mostre roupas que combinem", img])
    return response.text

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

    # Retorna o resultado da análise
    return f"Resultado da análise: {analysis_result}"

if __name__ == "__main__":
    app.run(debug=True)