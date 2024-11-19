from flask import Flask, render_template

app_Uendel = Flask(__name__) #cria o objeto da aplicação

@app_Uendel.route("/") #rota para solicitação web
def homepage(): #função
    return render_template ("homepage.html")

@app_Uendel.route("/contato")
def contato():
    return render_template("contato.html")

@app_Uendel.route("/usuario")
def dados_usuario():
    nome_usuario ="Ambrósio"
    dados_usu ={"profissao": "Estudante", "curso": "Sistemas para Internet"}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)

#@app_Uendel.route("/usuarios/<nome_usuario>;<nome_profissao>")
#def usuarios (nome_usuario, nome_profissao):
#    dados_usu = {"profissao":nome_profissao, "curso":"Sistemas para Internet"}
#    return render_template("usuario.html", nome= nome_usuario, dados = dados_usu)

@app_Uendel.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>")
def usuarios (nome_usuario, nome_profissao, nome_disciplina):
    dados_usu = {"profissao":nome_profissao, "curso": nome_disciplina}
    return render_template("usuario.html", nome= nome_usuario, dados = dados_usu)



@app_Uendel.route('/<name>')
def saudacao(name):
    return render_template('homepage_nome.html', nome=name)

if __name__ == "__main__":
    app_Uendel.run(port = 8080, debug= True)