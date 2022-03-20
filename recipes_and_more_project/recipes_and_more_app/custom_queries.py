
from django.db import connection


# display the name of the ingredient and the amount:
def ingredient_name_and_amount_query():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ingredient_calories.ingredient_name,
            receipt_ingredient.amount, receipt_ingredient.amount_type
            FROM ingredient_calories, receipt_ingredient
            WHERE ingredient_calories.id = receipt_ingredient.ingredient_name_frk_id
            """)
        rows = cursor.fetchall()
        ingredient_name_amount_list = []
        for row in rows:
            ingredient_name_amount_dict = {"ingredient_name": row[0], "amount": row[1], "amount_type": row[2]}
            ingredient_name_amount_list.append(ingredient_name_amount_dict)
        return ingredient_name_amount_list


def ingredient_name_and_amount_query(receipt_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT ingredient_calories.ingredient_name, receipt_ingredient.amount, receipt_ingredient.amount_type \
                        FROM  receipt_ingredient \
                        Inner Join ingredient_calories on \
                        receipt_ingredient.ingredient_name_frk_id = ingredient_calories.id \
                        where receipt_ingredient.recipe_frk_id = {receipt_id}")
        rows = cursor.fetchall()
        ingredients_of_receipt = []
        for row in rows:
            ingredient = {"ingredient_name": row[0], "amount": row[1], "amount_type": row[2]}
            ingredients_of_receipt.append(ingredient)
        return ingredients_of_receipt

# total_receipt_cal_per_100gr:
def total_receipt_cal_per_100gr():
    with connection.cursor() as cursor:
        cursor.execute("""
            select (COALESCE(SUM (ingredient_calories.ingredient_calories_per_100_gr_or_ml), 0) * 100) /
		        COALESCE(SUM(receipt_ingredient.amount),0)
            from receipt_ingredient, ingredient_calories
            WHERE ingredient_calories.id = receipt_ingredient.ingredient_name_frk_id
            group by receipt_ingredient.recipe_frk_id
            """)
        total_cal = cursor.fetchall()
        return total_cal
