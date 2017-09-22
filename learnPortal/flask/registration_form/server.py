from flask import Flask, render_template, redirect, request, session, flash
import re
app=Flask(__name__)

NAME_REGEX = re.compile(r'[^a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS1_REGEX = re.compile(r'[A-Z]')
PASS2_REGEX = re.compile(r'[0-9]')

@app.route('/')
def index():
    if 'success' in session:
        if session['success'] == True:
            flash(u'Thanks for submitting your information!','success')
            session['success'] = False
    else:
        session.clear()
    session['fname']=''
    session['lname']=''
    session['email']=''
    session['pw']=''
    session['cpw']=''
    return render_template('index.html',fname=session['fname'], lname=session['lname'], email=session['email'], pw=session['pw'], cpw=session['cpw'])

@app.route('/process', methods=['post'])
def process():
    session['fname']=request.form['fname']
    session['lname']=request.form['lname']
    session['email']=request.form['email']
    session['pw']=request.form['password']
    session['cpw']=request.form['confirmation']
    message=False
    for i in session.keys():
        if i != 'success':
            if len(session[i]) < 1:
                flash(u'This field is required', str(i))
                message=True
    if NAME_REGEX.search(session['fname']):
        flash(u'First name can only include letters', 'fname')
        message=True
    if NAME_REGEX.search(session['lname']):
        flash(u'Last name can only include letters', 'lname')
        message=True
    if len(session['pw']) < 8:
        flash(u'Password must be longer than 8 characters', 'pw')
        message=True
    elif (not PASS1_REGEX.search(session['pw'])) or (not PASS2_REGEX.search(session['pw'])):
        flash(u'Password must include at least 1 uppercase letter and 1 number', 'pw')
        message=True
    elif session['pw'] != session['cpw']:
        flash(u'Password and confirmation must match', 'pw')
        message=True
    if not EMAIL_REGEX.match(session['email']):
        flash(u'Please enter a valid email', 'email')
        message=True
    if message == True:
        return render_template('index.html',fname=session['fname'], lname=session['lname'], email=session['email'], pw=session['pw'], cpw=session['cpw'])
    else:
        session['success']=True
        return redirect('/')

app.secret_key = 'key'
app.run(debug=True)
