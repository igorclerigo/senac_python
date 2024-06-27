import google.generativeai as genai
import PIL.Image

genai.configure(api_key="AIzaSyAUjnJX5IetZFKMss7J6PuXfQQapKZuKB0")

def analyze_image(image_path):

    img = PIL.Image.open(image_path)


    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    response = model.generate_content(["O que tem na foto?", img])

    return response.text

if __name__ == "__main__":
    image_path = 'C:/Users/62129532024.1/Documents/GitHub/senac_python/UC3 - POO/Aula 15/image.png'  # Caminho para a imagem carregada
    analysis_result = analyze_image(image_path)
    print("Resultado da análise:", analysis_result)
