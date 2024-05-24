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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)