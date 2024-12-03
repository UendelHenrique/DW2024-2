from flask import Flask

app_Uendel = Flask (__name__) #cria objeto da aplicação.

@app_Uendel.route('/') #rota para solicitação web
@app_Uendel.route('/rota1') #rota para solicitação web
def rota1(): #função a ser executada quando chamar rotas acima.
    return 'Olá, turma!'

@app_Uendel.route('/rota2')
def rota2():
    resposta = "<H3>Essa é outra página da rota 2 <H3>"
    return resposta

def saudacoes (nome):
    return f'Olá, {nome}'

if __name__ == "__main__":
    app_Uendel.run() #executa aplicação.