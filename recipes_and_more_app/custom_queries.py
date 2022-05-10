from django.db import connection



def ingredient_name_and_amount_query(receipt_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT ingredient_calories.ingredient_name, receipt_ingredient.amount, receipt_ingredient.amount_type \
                        FROM  receipt_ingredient \
                        Inner Join ingredient_calories on \
                        receipt_ingredient.ingredient_name_frk_id = ingredient_calories.id \
                        where receipt_ingredient.recipe_frk_id = %s", (receipt_id,))
        rows = cursor.fetchall()
        ingredients_of_receipt = []
        for row in rows:
            ingredient = {"ingredient_name": row[0], "amount": row[1], "amount_type": row[2]}
            ingredients_of_receipt.append(ingredient)
        return ingredients_of_receipt

# total_receipt_cal_per_100gr:
def total_receipt_cal_per_100gr(receipt_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select (COALESCE(SUM (ingredient_calories.ingredient_calories_per_100_gr_or_ml), 0) * 100)/COALESCE(SUM(receipt_ingredient.amount),0) \
                       from receipt_ingredient, ingredient_calories \
                       WHERE ingredient_calories.id = receipt_ingredient.ingredient_name_frk_id and \
                       receipt_ingredient.recipe_frk_id = %s \
                       group by receipt_ingredient.recipe_frk_id", (receipt_id,))
        total_cal = cursor.fetchone()[0]
        return total_cal


# search_recipe_by_category:
def search_recipe_by_category(category):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT recipe.id, recipe.recipe_name, recipe.pic_url \
                       FROM  recipe \
                       where recipe.recipe_category = %s", (category,))
        rows = cursor.fetchall()
        all_recipes_by_category = []
        for row in rows:
            recipe_details = {"recipe_id": row[0], "recipe_name": row[1], "recipe_url": row[2]}
            # all_recipes_by_category[row[0]] = recipe_details
            all_recipes_by_category.append(recipe_details)
        print(all_recipes_by_category)
        return all_recipes_by_category

