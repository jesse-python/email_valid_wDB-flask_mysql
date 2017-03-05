from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

app = Flask(__name__)
mysql = MySQLConnector('email_validation')
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print request.form['email']

    submit = True

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        submit = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email, try again')
        submit = False

    if submit:
        session['email'] = request.form['email']
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(request.form['email'])
        # print query
        mysql.run_mysql_query(query)

        flash('The email address you entered ' + session['email'] +' is a VALID email address! Thank you!')

    emails = mysql.fetch('SELECT * FROM emails')
    print emails
    return render_template('success.html', emails=emails)



app.run(debug=True)
