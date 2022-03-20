--display the name of the ingredient and the amount:
SELECT ingredient_calories.ingredient_name,
       receipt_ingredient.amount, receipt_ingredient.amount_type
    FROM ingredient_calories, receipt_ingredient
    WHERE ingredient_calories.id = receipt_ingredient.ingredient_name_frk_id;

--total_receipt_cal_per_100gr:
select (COALESCE(SUM (ingredient_calories.ingredient_calories_per_100_gr_or_ml), 0) * 100) /
		COALESCE(SUM(receipt_ingredient.amount),0)
from receipt_ingredient, ingredient_calories
WHERE ingredient_calories.id = receipt_ingredient.ingredient_name_frk_id
group by receipt_ingredient.recipe_frk_id