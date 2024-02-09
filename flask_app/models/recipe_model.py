from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash


class Recipe:  # replace Class name
    # replace schema and all the table names including after self.
    DB = 'properbloom_schema'
    def __init__(self, data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.method = data['method']
        self.coffee_amount = data['coffee_amount']
        self.water_temp = data['water_temp']
        self.water_amount = data['water_amount']
        self.brew_minutes = data['brew_minutes']
        self.brew_seconds = data['brew_seconds']
        self.grind_size = data['grind_size']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @staticmethod
    def validate_recipe(new_recipe):
        is_valid = True
        if len(new_recipe['recipe_name']) < 1:
            flash('Name field required!')
            is_valid = False
        if len(new_recipe['method']) < 1:
            flash('Recipe Method field required!')
            is_valid = False
        if len(new_recipe['coffee_amount']) < 1:
            flash('Coffee amount field required!')
            is_valid = False
        if len(new_recipe['water_temp']) < 1:
            flash('Water Tempeture field required!')
            is_valid = False
        if len(new_recipe['water_amount']) < 1:
            flash('Water Amount field required!')
            is_valid = False
        if len(new_recipe['grind_size']) < 1:
            flash('Grind Size field required!')
            is_valid = False
        if len(new_recipe['description']) < 1:
            flash('Instruction field required!')
            is_valid = False
        return is_valid





    @classmethod
    def CreateRecipe(cls, data):
        query = """
        INSERT INTO recipes (recipe_name, method, coffee_amount, water_temp, water_amount, brew_minutes, brew_seconds, grind_size, description, user_id)
        VALUES ( %(recipe_name)s, %(method)s, %(coffee_amount)s, %(water_temp)s, %(water_amount)s, %(brew_minutes)s, %(brew_seconds)s, %(grind_size)s, %(description)s, %(user_id)s );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod  # Get One Method
    def GetRecipeById(cls, data):
        query = """
        SELECT * FROM recipes
        WHERE id = %(id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (recipe) VALUES (%(recipe)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM recipes WHERE id = %(id)s ; """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes
        SET recipe_name = %(recipe_name)s, 
        method = %(method)s, 
        coffee_amount = %(coffee_amount)s, 
        water_temp = %(water_temp)s , 
        water_amount = %(water_amount)s , 
        brew_minutes = %(brew_minutes)s
        brew_seconds = %(brew_seconds)s
        grind_size = %(grind_size)s
        description = %(description)s
        WHERE id = %(recipe_id)s ;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_user_with_recipe(cls):
        query = """
        SELECT * FROM recipes
        LEFT JOIN users
        ON recipes.user_id = users.id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        recipes = []

        for row_from_db in results:
            one_recipe = cls(row_from_db)
            user_data = {
                **row_from_db,
                "id": row_from_db["users.id"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"],

            }
            one_recipe.creator = user_model.User(user_data)
            recipes.append(one_recipe)
        return recipes

    @classmethod
    def get_one_recipe(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users ON users.id = recipes.user_id
        WHERE recipes.id = %(recipe_id)s ; 
        """  # to fix 'bool' error change id in WHERE id to WHERE recipes.id
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_recipe = cls(results[0])

        user_data = {
            **results[0],
            "id": results[0]["users.id"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],

        }
        one_recipe.creator = user_model.User(user_data)

        return one_recipe
