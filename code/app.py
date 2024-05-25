from flask import Flask, url_for, render_template, redirect, request, flash, jsonify, render_template_string
import mariadb
import database
import folium
from folium.plugins import HeatMap
import numpy as np
app = Flask(__name__)

#database.vytvor_db()
#database.vytvor_tabulky()
#database.nahraj_data('datafiles/ciselnik_obci.csv', ";")
#database.nahraj_data('datafiles/volby_obce.csv', ";")
#database.nahraj_data('datafiles/volby_okres.csv', ";")
#database.nahraj_data('datafiles/ciselnik_strany.csv', ";")
#database.nahraj_data('datafiles/souradnice_mesta_ok.csv', ";")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volby_1_data')
def volby_1_data():
    data = database.top_5_strany()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data],  # názvy stran
        "data": [row[2] for row in data]     # Celkem_hlasu
    }
    return jsonify(response)

@app.route('/volby_1')
def volby_1():
    return render_template('volby_1.html')

@app.route('/volby_2')
def volby_2():
    return render_template('volby_2.html')

@app.route('/min_prc_ucast_data')
def min_prc_ucast_data():
    data = database.min_prc_ucast()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data],  # názvy obcí
        "data": [row[1] for row in data]     # účast
    }
    return jsonify(response)

@app.route('/top_prc_ucast_data')
def top_prc_ucast_data():
    data = database.top_prc_ucast()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data], 
        "data": [row[1] for row in data]     
    }
    return jsonify(response)


@app.route('/obec_bez_vs_s_mcmo_data')
def obec_bez_vs_s_mcmo():
    data = database.obec_bez_vs_s_mcmo()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data],  
        "data": [row[1] for row in data]     
    }
    return jsonify(response)

@app.route('/volby_3')
def volby_3():
    return render_template('volby_3.html')

@app.route('/platne_vs_odevzdane_hlasy_data')
def platne_vs_odevzdane_hlasy():
    data = database.platne_vs_odevzdane_hlasy()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data], 
        "data": [row[1] for row in data]    
    }
    return jsonify(response)

@app.route('/vydane_vs_ztracene_hlasy_data')
def vydane_vs_ztracene_hlasy():
    data = database.vydane_vs_ztracene_hlasy()
    # Převést data do formátu vhodného pro JSON
    response = {
        "labels": [row[0] for row in data], 
        "data": [row[1] for row in data]    
    }
    return jsonify(response)

@app.route('/volby_4')
def volby_4():
    data = data_pro_mapu()
    
    # Vytvoření mapy pomocí folium
    m = folium.Map(location=[50.6612, 14.0532], zoom_start=11)  # Centrum ČR
    
    for row in data:
        folium.Marker(
            location=[row[0], row[1]],
            popup=(row[2]),
        ).add_to(m)

    

    folium.GeoJson('datafiles/UstiNadLabem.geojson', name='Ústecký kraj').add_to(m)
    
    # Uložení mapy do HTML
    map_html = m._repr_html_()
    # Zobrazení mapy v šabloně
    return render_template('volby_4.html', map_html=map_html)

@app.route('/data_pro_mapu')
def data_pro_mapu():
    data = database.data_pro_mapu()
    # Převést data do formátu vhodného pro JSON
    return data


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)