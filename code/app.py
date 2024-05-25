from flask import Flask, url_for, render_template, redirect, request, flash, jsonify
import mariadb
import database

app = Flask(__name__)

database.vytvor_db()
database.vytvor_tabulky()
database.nahraj_data('datafiles/ciselnik_obci.csv', ";")
database.nahraj_data('datafiles/volby_obce.csv', ";")
database.nahraj_data('datafiles/volby_okres.csv', ";")
database.nahraj_data('datafiles/ciselnik_strany.csv', ";")

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

@app.route('/volby_3')
def volby_3():
    return render_template('volby_3.html')

@app.route('/volby_4')
def volby_4():
    return render_template('volby_4.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)