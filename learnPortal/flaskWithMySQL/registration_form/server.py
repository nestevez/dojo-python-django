from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

NAME_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'user' in session:
        return render_template("loggedin.html")
    else:
        session.clear()
        return render_template("index.html")

@app.route('/register', methods=['post'])
def register():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['pw'] = request.form['pw']
    message = False
    if NAME_REGEX.search(session['fname']):
        flash(u'First name can only include letters', 'fname')
        message=True
    if NAME_REGEX.search(session['lname']):
        flash(u'Last name can only include letters', 'lname')
        message=True
    if len(session['pw']) < 8:
        flash(u'Password must be longer than 8 characters', 'pw')
        message=True
    if pw != request.form['cpw']:
        flash(u'Passwords do not match! Try again', 'pw')
        message = True
    if message==True:
        return render_template("index.html")
    query = ''
    query_data = {}
    return redirect('/')

@app.route('/login', methods=['post'])
def login():
    return render_template("loggedin.html")

app.secret_key = 'key'
app.run(debug=True)
