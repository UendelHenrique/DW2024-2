from flask import Flask, render_template

app_Uendel = Flask (__name__)

@app_Uendel.route('/')
def raiz():
    return render_template("homepage.html")

@app_Uendel.route('/contato')
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app_Uendel.run(port = 8080, debug= True)