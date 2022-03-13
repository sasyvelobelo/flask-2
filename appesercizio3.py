#per realizzare un server web che permetta di conoscere capoluoghi di region. 
#L'utente inserisce il nome della regione ed il programma restituisce il nome del capoluogo di regione.
#caricare i capoluoghi di regioni in una opportuna struttura dati.

#una volta fatto ciò, modificare poi l'es precedente per permettere all'utente di inserire un capuoluogo e di avere la regione in cui si trova.
#l'utente scegli se avere la regione o il capuoluogo selezionando un radiobutton

from flask import Flask, render_template, request
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo':'L\'Aquila', 'Basilicata':'Potenza', 'Calabria':'Catanzaro', 'Campania':'Napoli', 'Emilia-Romagna':'Bologna', 'Friuli-Venezia Giulia':'Trieste', 'Lazio':'Roma', 'Liguria':'Genova', 'Lombardia':'Milano', 'Marche':'Ancona', 'Molise':'Campobasso', 'Piemonte':'Torino', 'Puglia':'Bari', 'Sardegna':'Cagliari', 'Sicilia':'Palermo', 'Toscana':'Firenze', 'Trentino-Alto Adige':'Trento', 'Umbria':'Perugia', 'Valle dAosta':'Aosta', 'Veneto':'Venezia'}

@app.route('/', methods=['GET'])
def home():
    return render_template('homees3.html')

@app.route("/data", methods=["GET"])
def data():
    scelta = request.args["Scelta"]
    if scelta == "R":
        return render_template("regionees3.html")
    else:
        return render_template("capoluogoes3.html")

@app.route('/regione', methods=['GET'])
def regioni():
    regione = request.args['Regione']
    for key, value in capoluoghiRegione.items():
        if regione == key:
            capoluogo = value
            return render_template('regionees3.html', risposta = capoluogo)
    return render_template('erroreregione.html')

@app.route('/capoluoghi', methods=['GET'])
def capoluoghi():
    capoluogo = request.args['Capoluogo']
    for key, value in capoluoghiRegione.items():
        if capoluogo == value:
            regione = key
            return render_template('capoluogoes3.html', risposta = regione)
    return render_template('errorecapoluogo.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)





