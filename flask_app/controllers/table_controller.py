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

@app.route('/kalita')
def region_kalita():
    return render_template('region_kalita.html')

@app.route('/v60')
def region_v60():
    return render_template('region_v60.html')

@app.route('/chemex')
def region_chemex():
    return render_template('region_chemex.html')

@app.route('/aeropress')
def region_aeropress():
    return render_template('region_aeropress.html')

@app.route('/frenchpress')
def region_frenchpress():
    return render_template('region_frenchpress.html')

@app.route('/espresso')
def region_espresso():
    return render_template('region_espresso.html')

@app.route('/mokapot')
def region_mokapot():
    return render_template('region_mokapot.html')

@app.route('/autodrip')
def region_autodrip():
    return render_template('region_autodrip.html')

@app.route('/kalita_africa')
def kalita_africa_page():
    return render_template('kalita_africa.html')

@app.route('/kalita_south_america')
def kalita_south_america_page():
    return render_template('kalita_south_america.html')

@app.route('/kalita_caribbean')
def kalita_caribbean_page():
    return render_template('kalita_caribbean.html')

@app.route('/kalita_asia')
def kalita_asia_page():
    return render_template('kalita_asia.html')

@app.route('/kalita_central_america')
def kalita_central_america_page():
    return render_template('kalita_central_america.html')

@app.route('/kalita_hawaiian')
def kalita_hawaiian_page():
    return render_template('kalita_hawaiian.html')


@app.route('/grounds')
def grounds_page():
    return render_template('grounds.html')

@app.route('/gear')
def gear_page():
    return render_template('gear.html')

@app.route('/find')
def find_page():
    return render_template('find.html')

@app.route('/region')
def region_info_page():
    return render_template('region_info.html')

