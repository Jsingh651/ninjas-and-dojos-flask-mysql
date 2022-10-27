from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo

@app.route('/ninja')
def ninjapage():
    return render_template('ninja.html',ninjas = Ninja.get_all_ninjas(),dojos = Dojo.get_all())

@app.route('/create/ninja',methods = ['POST'])
def create_ninja():
    data = {
        'dojos_id': request.form['dojos_id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save_ninjas(data)
    return redirect(f"/show/dojo/{request.form['dojos_id']}")

@app.route('/delete/<int:id>/<int:dojos_id>')
def delete (id,dojos_id):
    data = {'id':id}
    Ninja.delete_ninja(data)
    return redirect(f'/show/dojo/{dojos_id}')


@app.route('/edit/<int:id>')
def edit (id):
    data = {'id':id}
    ninjass = Ninja.getone(data)
    return render_template('ninjaedit.html',ninjass = ninjass)

@app.route('/update/ninja/<int:ninja_id>',methods=['POST'])
def update(ninja_id):
    data = {
        'ninja_id': ninja_id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.update(data)
    return redirect(f'/show/dojo/{request.form["dojos_id"]}')