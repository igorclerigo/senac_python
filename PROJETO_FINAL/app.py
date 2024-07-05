from flask import Flask, request, render_template, redirect, url_for
import google.generativeai as genai
from PIL import Image

# Configurar a chave da API para a API Gemini
genai.configure(api_key="AIzaSyAUjnJX5IetZFKMss7J6PuXfQQapKZuKB0")

app = Flask(__name__)

# Dicionário de mapeamento de recomendações para links de compra
recommendation_links = {
    "camiseta casual": "https://www.zara.com/",
    "calça jeans": "https://www.uniqlo.com/",
    "vestido formal": "https://www.nordstrom.com/",
    "tênis esportivo": "https://www.nike.com/",
    # Adicione mais itens conforme necessário
}

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def analyze_image(image_stream, occasion):
    img = Image.open(image_stream)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = f"Analise a imagem e faça uma recomendação de outra peça de roupa baseado no resultado da análise e se necessário, para combinar com a {occasion}, pode até sugerir uma substituição. Responda em português"
    response = model.generate_content([prompt, img])
    recommendation = response.text  # Ajuste conforme necessário
    return recommendation

def get_purchase_link(recommendation):
    # Obtém o link de compra correspondente à recomendação
    return recommendation_links.get(recommendation.lower(), "Link de compra não disponível")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files or 'occasion' not in request.form:
            return redirect(request.url)
        file = request.files['file']
        occasion = request.form['occasion']
        if file.filename == '' or occasion == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            recommendation = analyze_image(file.stream, occasion)
            purchase_link = get_purchase_link(recommendation)
            return render_template('recommendation.html', recommendation=recommendation, purchase_link=purchase_link)
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
