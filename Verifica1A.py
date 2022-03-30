#
from flask import Flask, render_template, request, Response
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


stazioni=gpd.read_file("/workspace/flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv", sep=";")



@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/numero', methods=['GET'])
def home1():
    risultato=stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template("link1.html",risultato=risultato.to_html())

@app.route('/input', methods=['GET'])
def home2():
    return render_template("")

@app.route('/dropdown', methods=['GET'])
def home3():
    return render_template("")




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)