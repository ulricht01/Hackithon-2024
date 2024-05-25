from flask import Flask, url_for, render_template, redirect, request, flash
import mariadb
import database

app = Flask(__name__)

config = {
        'user': 'root',
        'password': '123',
        'host': 'mariadb',
        #'host': 'localhost',
        'port': 3306,
        'database': 'hackithon_2024'
    }


@app.route('/')
def index():
    return render_template('index.html')

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