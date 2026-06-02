## Import do framework,
## render_templete para leitura do HTML e reqest para captura de dados
from flask import Flask, render_template, request
## Conexão com sql e python
import mysql.connector 

bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}