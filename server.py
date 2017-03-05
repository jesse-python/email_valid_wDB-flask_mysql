from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector('email_validation')
@app.route('/')
def index():
    emails = mysql.fetch("SELECT * FROM emails")
    return render_template('index.html')

@app.route('/process')
def process():
    return redirect('/')


app.run(debug=True)
