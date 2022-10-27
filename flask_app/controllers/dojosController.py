from logging import lastResort
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route ('/')
def index():
    return redirect ('/dojos')


@app.route('/dojos')
def home():
    return render_template('dojo.html', dojos = Dojo.get_all())


@app.route('/create/dojo', methods = ['POST'])
def create():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect ('/dojos')

@app.route('/show/dojo/<int:id>')
def show(id):
    data = {
        'id':id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojoshow.html',dojo = dojo)