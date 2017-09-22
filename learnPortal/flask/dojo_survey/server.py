from flask import Flask, render_template,session, request, flash

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['post'])
def result():
    session['name']=request.form['name']
    session['loc']=request.form['location']
    session['lang']=request.form['language']
    session['com']=request.form['comment']
    error = False
    if len(session['name']) < 1:
        flash("Name cannot be empty!")
        error = True
    if len(session['com']) < 1:
        flash("Comment cannot be empty!")
        error = True
    elif len(session['com']) > 120:
        flash("Comment cannot be longer than 120 characters.")
        error = True
    if error == True:
        return render_template("index.html")
    else:
        return render_template("result.html")

app.secret_key='key'
app.run(debug=True)
