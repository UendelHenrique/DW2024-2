from flask import Flask, render_template, request

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
@app_Uendel.route("/usuario", defaults={"nome_usario":"usuario?","nome_profissao":""})
def usuario(nome_usuario, nome_profissao, nome_curso):
    dados_usu = {"Profissão": nome_profissao, "Curso":nome_curso}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)

@app_Uendel.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome=id)

@app_Uendel.route("/login")
def login():
    return render_template("login.html")

@app_Uendel.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    usuario = request.args.get('nome_usuario')
    senha = request.args.get('senha')
    return f"usuario: {usuario} e senha: {senha}"

if __name__ == "__main__":
    app_Uendel.run(port = 8080)