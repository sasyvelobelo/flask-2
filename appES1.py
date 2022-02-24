from flask import Flask, render_template
app = Flask(__name__)
import random 


@app.route('/')
def hello_world():
    return render_template("esercizio1.html")

@app.route('/meteo')
def random_number():
    numero_casuale = random.randint(0,8)
    if numero_casuale < 2:
        meteo1 = "pioggia"
        immagine ='static/pioggia.jpg'
    elif numero_casuale >3 & numero_casuale <5:
        meteo1 = "nuvoloso"
        immagine ='static/nuvoloso.jpg'
    else:
        meteo1 = "sole"
        immagine ='static/soleggiato.jpg'
    return render_template("meteo.html",meteo = meteo1,immagine1 = immagine )














if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)