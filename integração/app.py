## Import do framework,
## render_templete para leitura do HTML e reqest para captura de dados
from flask import Flask, render_template, request
## Conexão com sql e python
import mysql.connector 

app = Flask(__name__)

## Cria conexão com MySQL
bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cadastro1'
}

## Criação de rota para arquivo html principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
