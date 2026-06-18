## Import do framework,
## render_templete para leitura do HTML e reqest para captura de dados

from flask import Flask, render_template, request

## Conexao com sql e python

import mysql.connector 

app = Flask(__name__)

## Cria conexao com MySQL

bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cadastro1'
}

## Criacao de rota para arquivo html principal

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def criar_cadastro():
    cpf = request.form['cpf']
    primeiro_nome= request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    idade = request.form['idade']

    conexao = mysql.connector.connect(**bd_config)
    curso = conexao.cursor()

    query = "INSERT INTO cliente1 (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES (%s, %s, %s, %s)"
