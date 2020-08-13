from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    headline="Home";
    return render_template('index.html',title=headline)

@app.route('/home')
def home():
    headline="Home";
    return render_template('layouts.html',title=headline)

@app.route('/docs')
def docs():
    headline='Docs';
    return render_template('docs.html',title=headline)

@app.route('/projects')
def projects():
    headline="Projects";
    return render_template('projects.html',title=headline)

@app.route('/tutorials')
def tutorials():
    headline='Tutorials';
    return render_template('tutorials.html',title=headline)

@app.route('/docs/css')
def css():
    headline="Cascading Style Sheets";
    return render_template('css.html',title=headline)

@app.route('/docs/pwa')
def pwa():
    headline="Progressive Web App";
    return render_template('pwa.html',title=headline)

@app.route('/docs/sql')
def sql():
    headline="Structured Query Language";
    return render_template('sql.html',title=headline)

@app.route('/docs/introtodeeplearning')
def itdp():
    headline="Intro To Deep Learning";
    return render_template('tensorflow.html',title=headline)

@app.route('/projects/traditionalfacedetection')
def facedetection():
    headline="Traditional Face Detection";
    return render_template('facedetection.html',title=headline)

@app.route('/docs/html')
def html():
    headline="Hyper Text Markup Language";
    return render_template("hypertml.html",title=headline)

@app.route('/tutorials/php')
def php():
    headline="Hypertext Preprocessor";
    return render_template("php.html",title=headline)

@app.route('/tutorials/fundamentalsofprogramminglanguage')
def fopl():
    headline="Fundamentals of Programming Languages";
    return render_template("fopl.html",title=headline)

@app.route('/projects/angular')
def angular():
    headline="Angular.js";
    return render_template("angularjs.html",title=headline)

@app.route('/tutorials/fundamentalsofprogramminglanguage/usingpython')
def usingpython():
    headline="Using Python";
    return render_template("usingpython.html",title=headline)

@app.route('/tutorials/fundamentalsofprogramminglanguage/usingclang')
def usingclang():
    headline="Using C";
    return render_template("usingclang.html",title=headline)

@app.route('/tutorials/fundamentalsofprogramminglanguage/pre-requisite')
def requisite():
    headline="Pre-requisite";
    return render_template("requisite.html",title=headline)
