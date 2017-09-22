from flask import Flask, render_template, redirect, request, session
import random
app=Flask(__name__)


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    if 'message' not in session:
        session['message'] = ''
    if 'win' not in session:
        session['win'] = False
    return render_template('index.html', win=session['win'], message=session['message'], number=session['number'] )

@app.route('/entry', methods=['post'])
def entry():
    entry = int(request.form['entry'])
    if entry > session['number']:
        session['message'] = 'Too High!'
        session['win'] = False
    elif entry < session['number']:
        session['message'] = 'Too Low!'
        session['win'] = False
    elif entry == session['number']:
        session['win'] = True
    return redirect('/')

@app.route('/try_again', methods=['post'])
def try_again():
    session.clear()
    return redirect('/')

app.secret_key = 'secret'
app.run(debug=True)
