#realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera ed uno per la notte

from flask import Flask, render_template
import datetime
from datetime import date, timedelt


app = Flask(__name__)

today = date.today()



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 