from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)


@app.route('/')
def index():
    if 'times' not in session:
        session['times'] = 0
    else:
        session['times'] += 1
    return render_template('index.html', visits=session['times'])

@app.route('/twice', methods=['post'])
def twice():
    session['times'] +=1
    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

app.secret_key = 'secret'
app.run(debug=True)
