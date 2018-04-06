from flask import Blueprint
from extensions import mysql
import json

perfil = Blueprint('perfil', __name__)


@perfil.route("/perfil/", methods=['GET'])
def listar_perfis():
    comando = 'SELECT * FROM perfil'
    conexao = mysql.connect()
    cursor = conexao.cursor()
    cursor.execute(comando)
    retorno = criar_json(cursor)
    return json.dumps(retorno)


@perfil.route("/perfil/", methods=['PUT'])
def atualizar_perfil():
    retorno = json.loads(request.data)
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'UPDATE perfil SET nome = "' + retorno['nome'] + '", abreviacao = "' + retorno[
        'abreviacao'] + '" WHERE codigo = ' + str(retorno['codigo'])
    cursor.execute(comando)
    return jsonify({'sucesso': True, 'mensagem': 'alor'})


@perfil.route("/perfil/<string:codigo>", methods=['DELETE'])
def remover_perfil(codigo):
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'DELETE FROM perfil WHERE codigo = ' + str(codigo)
    cursor.execute(comando)
    conexao.commit()
    return jsonify({'sucesso': True, 'mensagem': 'alor'})


@perfil.route("/perfil/", methods=['POST'])
def adicionar_perfil():
    retorno = json.loads(request.data)
    comando = 'INSERT INTO perfil (nome, abreviacao) VALUES ("' + retorno['nome'] + '","' + retorno['abreviacao'] + '")'
    cursor.execute(comando)
    conexao.commit()
    return jsonify({'sucesso': True, 'mensagem': 'alor'})


@perfil.route("/perfil/<string:codigo>", methods=['GET'])
def recuperar_perfil(codigo):
    conexao = mysql.connect()
    cursor = conexao.cursor()
    comando = 'SELECT * FROM perfil WHERE codigo = ' + codigo
    cursor.execute(comando)
    return json.dumps(criar_json(cursor))
