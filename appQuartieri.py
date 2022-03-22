#realizzare un sito web che restituisca la mappa dei queartieri di milano
#ci deve essere una homepage con un link "quartieri di Milano", cliccando su questo link si deve visualizzare la mappa coi quartieri di Milano
from flask import Flask, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)


import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

quartieri = gpd.read_file('/workspace/flask/ds964_nil_wm.zip')

@app.route('/', methods=['GET'])
def home():
    return render_template("homepage.html")


@app.route('/quartieri', methods=['GET'])
def quartieri1():

    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot', methods=['GET'])
def plot():
    return render_template("homepage.html")





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 