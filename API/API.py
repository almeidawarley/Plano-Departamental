from flask import Flask, request, jsonify
from flask_cors import CORS
from extensions import mysql
from database import engine, Base

from disciplina.controller import disciplina
from perfil.controller import perfil

import json
import jwt

app = Flask(__name__)
CORS(app)


def criar_json(cursor):
    dados = cursor.fetchall();
    json = {'mensagem': [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in dados]}
    return json


@app.route("/criar")
def criar():
    Base.metadata.create_all(engine)
    return json.dumps({'opa': 'opa'})


@app.route("/login", methods=['POST'])
def login():
    retorno = json.loads(request.data)
    codificado = jwt.encode(retorno, 'amemJWT', algorithm='HS256')
    if retorno['login'] == 'almeida.warley@outlook.com' and retorno['senha'] == 'analuiza':
        return jsonify({'sucesso': True, 'token': codificado, 'expiraEm': 3000})
    else:
        return jsonify({'sucesso': False, 'token': codificado, 'expiraEm': 3000})


app.register_blueprint(disciplina)
app.register_blueprint(perfil)
