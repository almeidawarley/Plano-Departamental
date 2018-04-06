from flask import Blueprint
from extensions import mysql
import json
from dao import Disciplina

disciplina = Blueprint('disciplina', __name__)


@disciplina.route("/disciplina/", methods=['GET'])
def listar_disciplinas():
    comando = 'SELECT d.*, p.perfilNome FROM disciplina d JOIN perfil p ON d.perfil = p.codigo'
    conexao = mysql.connect()
    cursor = conexao.cursor()
    cursor.execute(comando)
    retorno = criar_json(cursor)
    return json.dumps(retorno)


@disciplina.route("/disciplina/", methods=['PUT'])
def atualizar_disciplina():
    requisicao = json.loads(request.data)
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'UPDATE disciplina SET nome = "' + requisicao['nome'] + '", perfil = ' + str(
        requisicao['perfil']) + ', chTeorica = ' + str(requisicao['chTeorica']) + ', chPratica = ' + str(
        requisicao['chPratica']) + ' WHERE codigo = "' + requisicao['codigo'] + '"'
    cursor.execute(comando)
    conexao.commit()
    return jsonify({'sucesso': True, 'mensagem': 'alor'})


@disciplina.route("/disciplina/<string:codigo>", methods=['DELETE'])
def remover_disciplina(codigo):
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'DELETE FROM disciplina WHERE codigo = "' + codigo + '"'
    cursor.execute(comando)
    conexao.commit()
    return jsonify({'sucesso': True, 'mensagem': 'alor'})


@disciplina.route("/disciplina/", methods=['POST'])
def adicionar_disciplina():
    token = 'abcdf'
    if token == request.headers.get('Authorization'):
        requisicao = json.loads(request.data)
        conexao = mysql.connect()
        cursor = conexao.cursor()
        comando = 'INSERT INTO disciplina (codigo, nome, perfil, chTeorica, chPratica)	VALUES ("' + requisicao[
            'codigo'] + '","' + requisicao['nome'] + '",' + str(requisicao['perfil']) + ',' + str(
            requisicao['chTeorica']) + ', ' + str(requisicao['chPratica']) + ')'
        cursor.execute(comando)
        conexao.commit()
        return jsonify({'sucesso': True, 'mensagem': 'alor'})
    else:
        return jsonify({'sucesso': False, 'mensagem': 'Erro ao validar usuario'})


@disciplina.route("/disciplina/<string:codigo>", methods=['GET'])
def recuperar_disciplina(codigo):
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'SELECT * FROM disciplina WHERE codigo = "' + codigo + '"'
    cursor.execute(comando)
    return json.dumps(criar_json(cursor))
