"""
@author: Uendel
"""
from flask import Flask

app_Uendel = Flask (__name__)

@app_Uendel.route('/')
@app_Uendel.route('/ola')

def raiz():
    return 'Olá, turma!'

def saudacoes(nome):
    return f'Olá, {nome}'

if __name__ == "__main__":
    app_Uendel.run(port = 8080, debug= True)