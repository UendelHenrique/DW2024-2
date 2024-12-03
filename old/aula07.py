from flask import Flask, render_template

app_Uendel = Flask(__name__) #cria o objeto da aplicação

@app_Uendel.route('/<name>')
def saudacao(name):
    return render_template('homepage_nome.html', nome=name)