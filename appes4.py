#si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull andamento dell'epidemia di Covid-19 nel nostro paese
#a partire dai dati presenti nel file
#l' utente sceglie la regione da un elenco (menù a tendina)
#clicca su un bottone ed il sito deve visualizzare una tabella contenente le informazioni relative a quella regione
#i dati da inserire nel menù a tendina devono essere caricati automaticamente dalla pagina 

from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')

@app.route('/', methods=['GET'])
def home():
    reg = df['nome_area'].drop_duplicates().to_list()
    return render_template('formes4.html', reg=reg)

@app.route('/data', methods=['GET'])
def data():
    regione = request.args['Regioni']
    df_result = df[df['nome_area'] == regione]
    return render_template('risultatoes4.html', tables=[df_result.to_html()], titles=[''])


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)