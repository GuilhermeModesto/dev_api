from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Guilherme', 'habilidades': ['Python', 'Flask']
     },
    {'nome': 'Modesto', 'habilidades': ['Python', 'Django']}
]

# devolve um desenvolvedor pelo ID, altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Comando não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)
        except Exception:
            mensagem = 'Erro desconhecido.'
            response = {'status': 'erro', 'mensagem': mensagem}
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Usuário inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)