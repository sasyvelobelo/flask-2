#realizzare un sito web che permetta la registrazione degli utenti, l'utente inserisce il nome, uno username, una password, la conferma della password ed il sesso
#se le informazioni sono corrette il sito salva le informazoni in una struttura dati opportuna(lista di dizionari)
#prevedere la possibilità di fare il login inserendo username e password, se sono corrette fornire un messaggio di benvenuto diverso a secondo del sesso

from flask import Flask, render_template,request
utenti = []

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("form3.html")
    

@app.route('/data', methods=['GET'])
def data():
    Name = request.args["Name"]
    username = request.args["Username"]
    password = request.args["Password"]
    conferma_password = request.args["Conferma_Password"]
    sesso =  request.args["Sex"]
    if password == conferma_password:
        if sesso == 'M':
            msg = 'Benvenuto' + Name
        else:
            msg = 'Benvenuta' + Name
        #inserimento nella lista degli utenti
        utenti.append({"name": Name, "username": username, "password": password, "conferma_password": conferma_password, "sesso": sesso})
        return render_template("welcome1.html",messaggio = msg)
    else:
        return ('Errore')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 