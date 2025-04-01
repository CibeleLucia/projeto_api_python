from flask import Flask, jsonify, request
from bd import Alunos
from bd_cursos import Cursos

app = Flask(__name__)   

#Listar todos os alunos
@app.route('/Alunos', methods=['GET'])
def get_alunos():
    return jsonify (Alunos)

#Consultar um aluno pelo CPF
@app.route('/Alunos/<string:cpf>', methods=['GET'])
def consultar_aluno(cpf):
    for aluno in Alunos:
        if aluno.get('cpf') == cpf:
            return jsonify(aluno)
    
#Cadastrar um novo aluno
@app.route('/Alunos', methods=['POST'])
def create_novo_aluno():
    novo_aluno = request.get_json()
    Alunos.append(novo_aluno)
    
    return jsonify (novo_aluno)

#Listar todos os cursos
@app.route('/Cursos', methods=['GET'])
def get_cursos():
    return jsonify (Cursos)


#Consultar um curso pelo ID
@app.route('/Cursos/<int:id>', methods=['GET'])
def obter_curso_por_id(id):
    for curso in Cursos: 
        if curso.get('id') == id:
            return jsonify(curso)
            
            



app.run() 
