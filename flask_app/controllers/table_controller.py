from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/brew')
def Brew():
    return render_template('brew.html')

@app.route('/region')
def region_page():
    return render_template('region.html')


@app.route('/recipe')
def recipe_page():
    return render_template('recipe.html')
    

@app.route('/recipe2')
def recipe2_page():
    return render_template('recipe2.html')

@app.route('/grounds')
def grounds_page():
    return render_template('grounds.html')

@app.route('/gear')
def gear_page():
    return render_template('gear.html')

@app.route('/find')
def find_page():
    return render_template('find.html')