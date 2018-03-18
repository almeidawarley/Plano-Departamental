from flask import Flask, request
from flask_cors import CORS
import json
from flaskext.mysql import MySQL

app = Flask(__name__)
CORS(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'elementary#14'
app.config['MYSQL_DATABASE_DB'] = 'planodepartamental'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

document = {}

@app.route("/removerdisciplina", methods = ['POST'])
def removerdisc():
	retorno = json.loads(request.data)
	conn = mysql.connect()
	cursor = conn.cursor()
	command = 'DELETE FROM disciplina WHERE codigo = "' + retorno['codigo'] + '"'
	cursor.execute(command)
	conn.commit()
	return 'alo'

@app.route("/recuperar/<codigo>", methods = ['GET'])
def recuperardisc(codigo):
	conn = mysql.connect()
	cursor = conn.cursor()
	command = 'SELECT * FROM disciplina WHERE codigo = "' + codigo + '"'
	cursor.execute(command)
	data = cursor.fetchone()
	return json.dumps(data)

@app.route("/listadisciplina", methods = ['GET'])
def disciplinas():
	command = 'SELECT * FROM disciplina'
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(command)
	data = cursor.fetchall()
	return json.dumps(data)

@app.route("/disciplina", methods = ['GET'])
def disciplina():
	document['codigo'] = "DCC000"
	document['nome'] = "Teoria dos Grafos"
	document['perfil'] = "IC"
	document['chTeorica'] = 2
	document['chPratica'] = 2
	return json.dumps(document)

@app.route("/docente", methods = ['GET'])
def docente():
	document['nome'] = "Stenio"
	document['sobrenome'] = "Sa"
	document['perfil'] = "IC"
	return json.dumps(document)

@app.route("/json", methods = ['GET','POST'])
def hell():
	conn = mysql.connect()
	cursor = conn.cursor()
	command = 'SELECT * FROM disciplina'
	cursor.execute(command)
	data = cursor.fetchall()
	return data[0][0]

@app.route("/put", methods = ['PUT'])
def rect():
	retorno = json.loads(request.data)
	conn = mysql.connect()
	cursor = conn.cursor()
	command = 'INSERT INTO disciplina (codigo, nome, perfil, chTeorica, chPratica)	VALUES ("' + retorno['codigo'] + '","' + retorno['nome'] + '","' + retorno['perfil'] + '",' + str(retorno['chTeorica']) + ', ' + str(retorno['chPratica'])+')'
	cursor.execute(command)
	conn.commit()
	return 'alo'

@app.route("/rec", methods = ['GET','POST'])
def recebedor():
	retorno = json.loads(request.data)
	conn = mysql.connect()
	cursor = conn.cursor()
	command = 'INSERT INTO disciplina (codigo, nome, perfil, chTeorica, chPratica)	VALUES ("' + retorno['codigo'] + '","' + retorno['nome'] + '","' + retorno['perfil'] + '",' + str(retorno['chTeorica']) + ', ' + str(retorno['chPratica'])+')'
	cursor.execute(command)
	conn.commit()
	return 'alo'