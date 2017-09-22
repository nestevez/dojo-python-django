from flask import Flask, render_template, redirect, request, session
import random, datetime

app=Flask(__name__)

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = ''
    return render_template('index.html')

@app.route('/process_money',methods=['post'])
def process():
    losegold = 1
    session['location'] = request.form['location']
    if session['location'] == 'farm':
        earn = random.randint(10,20)
    elif session['location'] == 'cave':
        earn = random.randint(5,10)
    elif session['location'] == 'house':
        earn = random.randint(2,5)
    elif session['location'] == 'casino':
        losegold = random.randint(0,1)
        earn = random.randint(0,50)
    date = datetime.datetime.now()
    if losegold == 0:
        session['gold'] -= earn
        session['log'] = '<p class="lose">Entered a casino and lost {} golds... Ouch... {:%Y/%m/%d %I:%M %p}</p>'.format(earn,date) + session['log']
    else:
        session['gold'] += earn
        session['log'] = '<p class="earn">Earned {} golds from the {} {:%Y/%m/%d %I:%M %p}</p>'.format(earn,session['location'],date) + session['log']
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

app.secret_key = 'key'
app.run(debug=True)
