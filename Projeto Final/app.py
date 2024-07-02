from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'moda'
}

# Rota para buscar os produtos
@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT nome, marca, caminho_imagem FROM produtos')
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)