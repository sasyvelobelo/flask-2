from flask import Flask, render_template
app = Flask(__name__)
import random 


@app.route('/')
def hello_world():
    return render_template("esercizio1.html")

@app.route('/')
def random_number:
    numero_casuale = random.randint(0,8)
    if numero_casuale < 2:
        previsione = "pioggia"
    elif numero_casuale >3 & numero_casuale <5:
        meteo = "nuvoloso"
    else:
        meteo = "sole"
    return render_template("esercizio1.html")














if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)