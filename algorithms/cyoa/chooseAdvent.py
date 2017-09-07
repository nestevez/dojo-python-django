from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/brown')
def brawn():
    return render_template("brown.html")

@app.route('/yellow')
def yalo():
    return render_template("yellow.html")

@app.route('/flames')
def flaim():
    return render_template("flames.html")

@app.route('/goop')
def goop():
    return render_template("goop.html")

@app.route('/dead')
def ded():
    return render_template("dead.html")


app.run(debug=True)
