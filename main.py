from flask import Flask, render_template

app_Uendel = Flask (__name__)

@app_Uendel.route("/")
def raiz():
    return render_template("homepage.html")

@app_Uendel.route("/contato")
def contato():
    return render_template("contato.html")

@app_Uendel.route("/index")
def indice():
    nome_User = "Uêndel"
    return render_template("index.html", nome = nome_User)

@app_Uendel.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_curso>")
def usuario(nome_usuario, nome_profissao, nome_curso):
    dados_usu = {"Profissão": nome_profissao, "Curso":nome_curso}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)

@app_Uendel.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome=id)

if __name__ == "__main__":
    app_Uendel.run(port = 8080)