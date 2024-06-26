from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# ADD RECIPE ROUTE
@app.route('/recipe/new')
def new_recipe():

    return render_template('new_recipe.html')



@app.route('/add_recipe', methods = ["POST"])
def add_new_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/new')

    newRecipe_data = {
        'recipe_name' : request.form['recipe_name'],
        'method' : request.form['method'],
        'coffee_amount' : request.form['coffee_amount'],
        'water_temp' : request.form['water_temp'],
        'water_amount' : request.form['water_amount'],
        'brew_minutes' : request.form['brew_minutes'],
        'brew_seconds' : request.form['brew_seconds'],
        'grind_size' : request.form['grind_size'],
        'description' : request.form['description'],
        'user_id' : session['user_id']
        
    }

    Recipe.CreateRecipe(newRecipe_data)
    return redirect('/user_recipes')


# EDIT RECIPE ROUTE
@app.route ('/recipe/edit/<int:recipe_id>')
def show_edit_recipe(recipe_id):
    one_recipe = Recipe.get_one_recipe({'recipe_id' : recipe_id})
    return render_template('edit_recipe.html', one_recipe=one_recipe)



@app.route ('/recipe/edit/<int:recipe_id>', methods = ['POST'])
def edit_recipe(recipe_id):

    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipe/edit/{recipe_id}') 
    
    Recipe.update({
        **request.form,
        'recipe_id' : recipe_id
    })

    return redirect('/user_recipes')





# DELETE A RECIPE ROUTE
@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    Recipe.delete({ 'id' : recipe_id})
    return redirect('/user_recipes')


# SHOW ONE RECIPE ROUTE
@app.route('/recipe/show/<int:recipe_id>')
def show_recipe(recipe_id):

    one_recipe = Recipe.get_one_recipe({ 'recipe_id' : recipe_id})
    return render_template('show_recipe.html', one_recipe=one_recipe)



