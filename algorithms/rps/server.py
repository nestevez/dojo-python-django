from flask import Flask, render_template, request, redirect, session
import random, emoji
app = Flask(__name__)

comp = 0
user = 0

options = {
0: 'Nuclear Bomb',
1: 'Cockroach',
2: 'Foot'
}
message = ''

@app.route('/')
def index():
    session['wins'] = 0
    session['losses'] = 0
    session['ties'] = 0
    return render_template("index.html", wins=session['wins'], losses=session['losses'], ties=session['ties'], message=message)

@app.route('/process_play', methods=['post'])
def process():
    print request.form
    comp = options[random.randint(0,2)]
    user = request.form['move']
    if (comp == options[0] and user == options[2]) or (comp == options[1] and user == options[0]) or (comp == options[2] and user == options[1]):
        message = 'You Win!! Congrats!'
        session['wins'] +=1
    elif (user == options[0] and comp == options[2]) or (user == options[1] and comp == options[0]) or (user == options[2] and comp == options[1]):
        message = emoji.emojize('You Loser! Sucks to suck! :v:', use_aliases=True)
        session['losses'] +=1
    elif comp == user:
        message = 'You Tie...'
        session['ties'] +=1
    print user, comp
    return render_template("index.html", wins=session['wins'], losses=session['losses'], ties=session['ties'], message=message)

app.secret_key = "secret key"
app.run(debug=True)
