#
from flask import Flask, render_template, request, Response, redirect,url_for
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


stazioni=pd.read_csv("/workspace/flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv", sep=";")



@app.route('/', methods=['GET'])
def home():
    return render_template("homepageRaDbuT.html")

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
        return redirect(url_for("/numero"))
    elif scelta == "es2":
        return redirect(url_for("/numero"))
    else:
        return redirect(url_for("/dropdown"))
        
    

@app.route('/numero', methods=['GET'])
def home1():
    global risultato
    risultato=stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template("link1.html",risultato=risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    #costruzione del grafico

    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")

    #visualizzazione grafico
    output = io.BytesIO()#stabilire canale comunicazione
    FigureCanvas(fig).print_png(output)#stampare l'immagine o figura sull output
    return Response(output.getvalue(), mimetype='image/png')# gli diciamo di mandare in risposta quello che c'è in output però bisogna specificare cosa gli mandiamo con ad esempio 'mimetype='image/png'

@app.route('/input', methods=['GET'])
def home2():
    return render_template("")

@app.route('/dropdown', methods=['GET'])
def home3():
    return render_template("")




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)