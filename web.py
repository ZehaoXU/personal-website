# -*- coding: utf-8 -*-
import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    #return flask.render_template("home.html")
    return flask.render_template('home.html')

@app.route('/author')
def author():
    # return /author
    return flask.render_template('author.html')

@app.route('/project')
def project():
    # return /project
    return flask.render_template('project.html')

@app.route('/demo')
def demo():
    # return /demo
    return flask.render_template('demo.html')

@app.route('/contact')
def contact():
    # return /contact
    return flask.render_template('contact.html')

@app.route('/demo1')
def demo1():
    return flask.render_template('demo1.html')

@app.route('/demo2')
def demo2():
    return flask.render_template('demo2.html')

@app.route('/demo3')
def demo3():
    return flask.render_template('demo3.html')

@app.route('/pyFile')
def pyFile():
    return flask.render_template('pyFile.html')

if __name__ == '__main__':
    app.run()
