from flask import Flask, request, jsonify, render_template, redirect

contatos = [
    'Zezinho',
    'Luizinho'
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('contatos.html')

@app.route('/contatos')
def listar_contatos():
    return jsonify(contatos)


@app.route('/add', methods=['POST'])
def add_contato():
    nome = request.form['nome']

    if nome:
        contatos.append(nome)
        
    return redirect('/')


@app.route('/esquecer', methods=['DELETE'])
def del_contatos():
    nome = request.form['nome']
    
    if nome and (nome in contatos):
        i = contatos.index(nome)
        del contatos[i]

    return jsonify(contatos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
