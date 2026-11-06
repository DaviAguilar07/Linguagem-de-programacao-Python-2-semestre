# !ngrok authtoken 2YE2L21rdpK3IO8oTpHoTCL9z7h_xxsYeAHKwXUzQjWLZduY

# usar esse código de autenticação

# Em outra célula rodar:

from flask import Flask
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def index():
    return 'Olá, esta é a rota principal do back-end!'

if __name__ == '__main__':
    app.run()
