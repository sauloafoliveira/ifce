from flask import Flask, render_template, request, jsonify, redirect
from banco_mundo import listar_todas, alterar_cidade, buscar_id, deletar_cidade, inserir_cidade


app = Flask(__name__)

@app.route('/')
def home():
  return jsonify(listar_todas())

@app.route('/buscar')
def buscar():
  
  nome = request.values.get('nome')  

  return jsonify( buscar_id(nome) )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)