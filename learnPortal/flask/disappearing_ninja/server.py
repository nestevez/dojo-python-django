from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja/')
def all():
    picture = 'img/ninjaturtles.jpg'
    return render_template('ninja.html', pic = picture)

@app.route('/ninja/<color>')
def ninjas(color):
    if color == 'blue':
        picture = 'img/leonardo.jpg'
    elif color == 'purple':
        picture = 'img/donatello.jpg'
    elif color == 'red':
        picture = 'img/raphael.jpg'
    elif color == 'orange':
        picture = 'img/michaelangelo.jpg'
    else:
        picture = 'img/notapril.jpg'

    return render_template('ninja.html',pic = picture)

app.run(debug=True)
