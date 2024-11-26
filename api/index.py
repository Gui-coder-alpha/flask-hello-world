from flask import Flask, request, jsonify

app = Flask(__name__)

comidas = [ #lista de doces, com listas de dicionários
    {'id' : 1, 'name' : "paçoca", 'informação' : "Doce de amendoim, doce e salgado."},
    {'id' : 2, 'name' : "chocolate", 'informação' : "Doce de cacau, doce e amargo."}
]

#Pega os valores de comida
@app.route('/comidas', methods=['GET'])
def get_comida():                                      
    return jsonify(comidas)

#Pega os valores de comida pelo id
@app.route('/comidas/<int:id>', methods=['GET'])
def get_comida_id(id):
    comida = next((u for u in comidas if u['id'] == id), None) 
    return jsonify(comida) if comida else ('', 404) 

@app.route('/comidas', methods=['POST']) 
def adicionar_comida():
    nova_comida = request.get_json()
    comidas.append(nova_comida)
    return jsonify(nova_comida), 201

@app.route('/comidas/<int:id>', methods=['DELETE']) 
def remover_comdia(id):
        comida = next((u for u in comidas if u['id'] == id), None)
        if comida:
            comidas.remove(comida)
            return ('', 204) 
        else:
            return ('', 404) 
        
@app.route('/comidas/<int:id>', methods=['PUT'])
def atualizar_comida(id):
    comida = next((u for u in comidas if u['id'] == id), None)
    if comida:
         informação_a_atualizar = request.get_json()
         comidas.update(informação_a_atualizar)
         return jsonify(comida)
    else:
        return ('', 404)
    
if __name__ == '__main__':
    app.run(debug=True)