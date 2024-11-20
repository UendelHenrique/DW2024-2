from flask import Flask

app_Uendel = Flask(__name__)

@app_Uendel.route('/')
def raiz():
    return 'Olá, turma!'

app_Uendel.run()