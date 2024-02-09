from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)





@app.route('/')
def Home():
    return render_template('home.html')







@app.route('/login_user', methods=["POST"])
def loginuser():

    login_data = {'email': request.form['email']}
    user_in_db = User.GetUserByEmail(login_data)

    if not user_in_db:
        flash('Invalid Email or Password')
        return redirect('/register')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email or Password')
        return redirect('/register')

    session['user_id'] = user_in_db.id

    return redirect('/user_recipes')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




@app.route('/user_recipes')
def user_recipes():

    if 'user_id' not in session:
        return redirect('/register')
    list_of_recipes = Recipe.get_user_with_recipe()

    new_user = User.GetUserById({'user_id': session['user_id']})

    return render_template('user_recipes.html', list_of_recipes=list_of_recipes, new_user=new_user)






@app.route('/register_user', methods=["POST"])
def successful_register():

    if not User.validate_user(request.form):
        return redirect('/register')

    pw_hash = bcrypt.generate_password_hash(
        request.form['password']).decode("utf-8")
    newUser_data = {
        'user_name': request.form['user_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.CreateUser(newUser_data)
    session['user_id'] = user_id
    return redirect('/')




@app.route('/user_recipes/<int:user_id>')
def show_success(user_id):

    if 'user_id' not in session:
        return redirect('/')
    newUser = User.GetUserById({'user_id': user_id})
    return render_template('user_recipes.html', newUser=newUser)






@app.route('/user_recipes/<int:id>')
def show_data(id):

    user = User.get_user_with_recipe({'id': id})
    print(user.user_recipes)
    return render_template('user_recipes.html', user=user)






@app.route('/register')
def Register():
    return render_template('register.html')


# @app.route('/login')
# def login_page():
#     return redirect('/')



@app.route('/new_recipe')
def NewRecipe():
    return render_template('new_recipe.html')



@app.route('/user_recipes')
def UserRecipes():
    return render_template('user_recipes.html')


@app.route('/brew')
def Brew():
    return render_template('brew.html')


@app.route('/shop')
def Shop():
    return render_template('shop.html')


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


# Region routes
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
    return render_template('region_aero.html')


@app.route('/frenchpress')
def region_frenchpress():
    return render_template('region_frenchpress.html')


@app.route('/espresso')
def region_espresso():
    return render_template('region_espresso.html')


@app.route('/mokapot')
def region_mokapot():
    return render_template('region_moka.html')


@app.route('/autodrip')
def region_autodrip():
    return render_template('region_autodrip.html')


# Kalita Recipies
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


# V60 Recipes
@app.route('/v60_africa')
def v60_africa_page():
    return render_template('v60_africa.html')


@app.route('/v60_south_america')
def v60_south_america_page():
    return render_template('v60_south_america.html')


@app.route('/v60_caribbean')
def v60_caribbean_page():
    return render_template('v60_caribbean.html')


@app.route('/v60_asia')
def v60_asia_page():
    return render_template('v60_asia.html')


@app.route('/v60_central_america')
def v60_central_america_page():
    return render_template('v60_central_america.html')


@app.route('/v60_hawaiian')
def v60_hawaiian_page():
    return render_template('v60_hawaiian.html')


# Areopress Recipes
@app.route('/aero_africa')
def aero_africa_page():
    return render_template('aero_africa.html')


@app.route('/aero_south_america')
def aero_south_america_page():
    return render_template('aero_south_america.html')


@app.route('/aero_caribbean')
def aero_caribbean_page():
    return render_template('aero_caribbean.html')


@app.route('/aero_asia')
def aero_asia_page():
    return render_template('aero_asia.html')


@app.route('/aero_central_america')
def aero_central_america_page():
    return render_template('aero_central_america.html')


@app.route('/aero_hawaiian')
def aero_hawaiian_page():
    return render_template('aero_hawaiian.html')


# Chemex Recipes
@app.route('/chemex_africa')
def chemex_africa_page():
    return render_template('chemex_africa.html')


@app.route('/chemex_south_america')
def chemex_south_america_page():
    return render_template('chemex_south_america.html')


@app.route('/chemex_caribbean')
def chemex_caribbean_page():
    return render_template('chemex_caribbean.html')


@app.route('/chemex_asia')
def chemex_asia_page():
    return render_template('chemex_asia.html')


@app.route('/chemex_central_america')
def chemex_central_america_page():
    return render_template('chemex_central_america.html')


@app.route('/chemex_hawaiian')
def chemex_hawaiian_page():
    return render_template('chemex_hawaiian.html')


# Espresso Recipes
@app.route('/espresso_africa')
def espresso_africa_page():
    return render_template('espresso_africa.html')


@app.route('/espresso_south_america')
def espresso_south_america_page():
    return render_template('espresso_south_america.html')


@app.route('/espresso_caribbean')
def espresso_caribbean_page():
    return render_template('espresso_caribbean.html')


@app.route('/espresso_asia')
def espresso_asia_page():
    return render_template('espresso_asia.html')


@app.route('/espresso_central_america')
def espresso_central_america_page():
    return render_template('espresso_central_america.html')


@app.route('/espresso_hawaiian')
def espresso_hawaiian_page():
    return render_template('espresso_hawaiian.html')


# French Press Recipes
@app.route('/frenchpress_africa')
def frenchpress_africa_page():
    return render_template('frenchpress_africa.html')


@app.route('/frenchpress_south_america')
def frenchpress_south_america_page():
    return render_template('frenchpress_south_america.html')


@app.route('/frenchpress_caribbean')
def frenchpress_caribbean_page():
    return render_template('frenchpress_caribbean.html')


@app.route('/frenchpress_asia')
def frenchpress_asia_page():
    return render_template('frenchpress_asia.html')


@app.route('/frenchpress_central_america')
def frenchpress_central_america_page():
    return render_template('frenchpress_central_america.html')


@app.route('/frenchpress_hawaiian')
def frenchpress_hawaiian_page():
    return render_template('frenchpress_hawaiian.html')


# MokaPot Recipes
@app.route('/moka_africa')
def moka_africa_page():
    return render_template('moka_africa.html')


@app.route('/moka_south_america')
def moka_south_america_page():
    return render_template('moka_south_america.html')


@app.route('/moka_caribbean')
def moka_caribbean_page():
    return render_template('moka_caribbean.html')


@app.route('/moka_asia')
def moka_asia_page():
    return render_template('moka_asia.html')


@app.route('/moka_central_america')
def moka_central_america_page():
    return render_template('moka_central_america.html')


@app.route('/moka_hawaiian')
def moka_hawaiian_page():
    return render_template('moka_hawaiian.html')


# Auto Drip Recipes
@app.route('/autodrip_africa')
def autodrip_africa_page():
    return render_template('autodrip_africa.html')


@app.route('/autodrip_south_america')
def autodrip_south_america_page():
    return render_template('autodrip_south_america.html')


@app.route('/autodrip_caribbean')
def autodrip_caribbean_page():
    return render_template('autodrip_caribbean.html')


@app.route('/autodrip_asia')
def autodrip_asia_page():
    return render_template('autodrip_asia.html')


@app.route('/autodrip_central_america')
def autodrip_central_america_page():
    return render_template('autodrip_central_america.html')


@app.route('/autodrip_hawaiian')
def autodrip_hawaiian_page():
    return render_template('autodrip_hawaiian.html')
