import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flaskext.mysql import MySQL

app = Flask(__name__)
CORS(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'elementary#14'
app.config['MYSQL_DATABASE_DB'] = 'planodepartamental'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

if __name__ == '__main__':  
    app.run(host = '127.0.0.1', debug = True)

def criar_json(cursor):
	dados = cursor.fetchall();
	json = {'mensagem': [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in dados]}
	return json

@app.route("/perfil", methods=['GET'])
def listar_perfis():
	comando = 'SELECT * FROM perfil'
	conexao = mysql.connect()
	cursor = conexao.cursor()
	cursor.execute(comando)
	retorno = criar_json(cursor)
	return json.dumps(retorno)

@app.route("/disciplina", methods = ['GET'])
def listar_disciplinas():
	comando = 'SELECT d.*, p.perfilNome FROM disciplina d JOIN perfil p ON d.perfil = p.codigo'
	conexao= mysql.connect()
	cursor = conexao.cursor()
	cursor.execute(comando)
	retorno = criar_json(cursor)
	return json.dumps(retorno)

@app.route("/perfil/", methods = ['PUT'])
def atualizar_perfil():
	retorno = json.loads(request.data)
	conexao = mysql.connect()
	cursor = conexao.cursor()
	comando = 'UPDATE perfil SET nome = "' + retorno['nome'] + '", abreviacao = "' + retorno['abreviacao'] +'" WHERE codigo = ' + str(retorno['codigo'])
	cursor.execute(comando)
	return jsonify({'sucesso' : True, 'mensagem': 'alor'})

@app.route("/perfil/<string:codigo>", methods = ['DELETE'])
def remover_perfil(codigo):
	conexao = mysql.connect()
	cursor = conexao.cursor()
	comando = 'DELETE FROM perfil WHERE codigo = ' + str(codigo)
	cursor.execute(comando)
	conexao.commit()
	return jsonify({'sucesso' : True, 'mensagem': 'alor'})

@app.route("/perfil/", methods = ['POST'])
def adicionar_perfil():
	retorno = json.loads(request.data)
	comando = 'INSERT INTO perfil (nome, abreviacao) VALUES ("' + retorno['nome'] + '","' + retorno['abreviacao'] + '")'
	cursor.execute(comando)
	conexao.commit()
	return jsonify({'sucesso' : True, 'mensagem': 'alor'})

@app.route("/perfil/<string:codigo>", methods = ['GET'])
def recuperar_perfil(codigo):
	conexao = mysql.connect()
	cursor = conexao.cursor()	
	comando = 'SELECT * FROM perfil WHERE codigo = ' + codigo
	cursor.execute(comando)
	return json.dumps(criar_json(cursor))

@app.route("/disciplina/", methods = ['PUT'])
def atualizar_disciplina():
	requisicao = json.loads(request.data)
	conexao = mysql.connect()
	cursor = conexao.cursor()
	comando = 'UPDATE disciplina SET nome = "' + requisicao['nome'] + '", perfil = ' + str(requisicao['perfil']) + ', chTeorica = ' + str(requisicao['chTeorica']) + ', chPratica = ' + str(requisicao['chPratica']) + ' WHERE codigo = "' + requisicao['codigo'] + '"'
	cursor.execute(comando)
	conexao.commit()
	return jsonify({'sucesso' : True, 'mensagem': 'alor'})

@app.route("/disciplina/<string:codigo>", methods = ['DELETE'])
def remover_disciplina(codigo):
	conexao = mysql.connect()
	cursor = conexao.cursor()
	comando = 'DELETE FROM disciplina WHERE codigo = "' + codigo + '"'
	cursor.execute(comando)
	conexao.commit()
	return jsonify({'sucesso' : True, 'mensagem': 'alor'})

@app.route("/disciplina/", methods = ['POST'])
def adicionar_disciplina():
	token = 'abcdf'
	if token == request.headers.get('Authorization'):
		requisicao = json.loads(request.data)
		conexao = mysql.connect()
		cursor = conexao.cursor()
		comando = 'INSERT INTO disciplina (codigo, nome, perfil, chTeorica, chPratica)	VALUES ("' + requisicao['codigo'] + '","' + requisicao['nome'] + '",' + str(requisicao['perfil']) + ',' + str(requisicao['chTeorica']) + ', ' + str(requisicao['chPratica'])+')'
		cursor.execute(comando)
		conexao.commit()
		return jsonify({'sucesso' : True, 'mensagem': 'alor'})
	else:
		return jsonify({'sucesso' : False, 'mensagem': 'Erro ao validar usuario'})

@app.route("/disciplina/<string:codigo>", methods = ['GET'])
def recuperar_disciplina(codigo):	
	conexao = mysql.connect()
	cursor = conexao.cursor()
	comando = 'SELECT * FROM disciplina WHERE codigo = "' + codigo + '"'
	cursor.execute(comando)
	return json.dumps(criar_json(cursor))