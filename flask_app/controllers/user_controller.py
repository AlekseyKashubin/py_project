from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/register')
def Register():
    return render_template('register.html')


# @app.route('/login')
# def login_page():
#     return redirect('/')




@app.route('/login_user', methods = ["POST"])
def loginuser():

    login_data = {'email':request.form['email']}
    user_in_db = User.GetUserByEmail(login_data)

    if not user_in_db:
        flash('Invalid Email or Password')
        return redirect('/register')
    
    if not bcrypt.check_password_hash( user_in_db.password, request.form['password'] ):
        flash('Invalid Email or Password')
        return redirect('/register')
    
    session['user_id'] = user_in_db.id

    return redirect('/')






@app.route('/user_recipes')
def user_recipes():

    if 'user_id' not in session:
        return redirect('/register')
    list_of_recipes = Recipe.get_user_with_recipe()

    new_user = User.GetUserById({'user_id':session['user_id']})

    return render_template('user_recipes.html', list_of_recipes=list_of_recipes, new_user=new_user)







@app.route('/register', methods = ["POST"])
def successful_register():
    
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password']).decode("utf-8")

    newUser_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }

    user_id = User.CreateUser(newUser_data)

    session['user_id'] = user_id

    return redirect('/')







@app.route('/logout')
def logout( ):
    session.clear()
    return redirect('/')







@app.route('/user_recipes/<int:user_id>')
def show_success(user_id):

    if 'user_id' not in session:
        return redirect('/')
    newUser = User.GetUserById({'user_id' : user_id})
    return render_template('user_recipes.html', newUser = newUser)








@app.route('/user_recipes/<int:id>')
def show_data(id):

    user = User.get_user_with_recipe({'id' : id})
    print(user.user_recipes)
    return render_template('user_recipes.html', user=user)