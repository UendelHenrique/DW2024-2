"""
@author: Uendel
"""
from flask import Flask, render_template

app_Uendel = Flask (__name__)

@app_Uendel.route('/<id>')

def raiz(id):
    return render_template("homepage_nome.html", nome=id)


if __name__ == "__main__":
    app_Uendel.run(port = 8080, debug= True)