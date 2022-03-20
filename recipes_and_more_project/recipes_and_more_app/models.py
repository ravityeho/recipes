from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



# Create your models here.

class Recipe(models.Model):
    CATEGORIES = [
        ('BREAD & DOUGH', 'bread & dough'),
        ('CAKES', 'cakes'),
        ('COOKIES & BISCUITS', 'cookies & biscuits'),
        ('CUPCAKES & MUFFINS', 'cupcakes & muffins'),
        ('DESSERTS', 'desserts'),
        ('PANCAKES & CREPES', 'pancakes & crepes'),
        ('DESSERTS, PIES & TARTS', 'desserts, pies & tarts'),
    ]

    recipe_category = models.CharField(null=True, blank=True, max_length=128, choices=CATEGORIES)
    recipe_name = models.CharField(null=False, blank=False, max_length=256)
    recipe_description = models.CharField(null=False, blank=False, max_length=512)
    preparation_time = models.PositiveIntegerField(null=False, blank=False)
    total_time = models.PositiveIntegerField(null=False, blank=False)
    recipe_content = models.CharField(null=False, blank=False, max_length=2048)
    pic_url = models.URLField(null=True, blank=True)
    difficulty_level = models.PositiveSmallIntegerField(null=False, blank=False,
                                                        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_deleted = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.recipe_name

    class Meta:
        db_table = 'recipe'



class IngredientCalories(models.Model):
    ALERGENS = [
        ('GLUTEN', 'Gluten'),
        ('EGGS', 'Eggs'),
        ('LACTOSE', 'lactose'),
        ('NUTS', 'Nuts'),
        ('PEANUTS', 'Peanuts'),
        ('SESAME SEEDS', 'Sesame Seeds'),
        ('SOY', 'Soy'),
        ('NON', 'Non')
    ]

    ingredient_name = models.CharField(null=False, blank=False, max_length=256)
    ingredient_calories_per_100_gr_or_ml = models.FloatField(null=False, blank=False)
    optional_allergens = models.CharField(null=True, blank=True, max_length=128, choices=ALERGENS)
    optional_allergens_2 = models.CharField(null=True, blank=True, max_length=128, choices=ALERGENS)
    #proteins

    def __str__(self):
        return self.ingredient_name

    class Meta:
        db_table = 'ingredient_calories'



class ReceiptIngredient(models.Model):
    MEASUREMENT = [
        ('GRAM', 'Gram'),
        ('KG', 'Kg'),
        ('ML', 'Ml'),
        ('TEASPOON', 'Teaspoon'),
        ('TABLESPOON', 'Tablespoon'),
        ('CUP', 'Cup'),
        ('LEAF', 'Leaf'),
        ('SERVING PACKET', 'Serving Packet'),
        ('FLUID OUNCE (FL. OZ)', '(Fluid Ounce (fl. oz)'),
        ('QUART', 'Quart'),
        ('PINT', 'Pint')
    ]

    recipe_frk = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredient_name_frk = models.ForeignKey(IngredientCalories, on_delete=models.PROTECT)
    # ingredient_calories_frk = models.ForeignKey(IngredientCalories, on_delete=models.PROTECT)
    amount = models.FloatField(null=False, blank=False)
    amount_type = models.CharField(null=True, blank=True, max_length=128, choices=MEASUREMENT)

    def __str__(self):
        return f"Recipe: {self.recipe_frk}: ->___{self.ingredient_name_frk}"

    class Meta:
        db_table = "receipt_ingredient"


# class CustomUser(AbstractUser):
#     # email = models.CharField(null=False, blank=False, max_length=128)
#     address = models.CharField(null=False, blank=False, max_length=256)
#     date_joined = models.DateField(auto_now_add=True)


class RecipeReviews(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    review_date = models.DateField(auto_now_add=True)
    review_title = models.CharField(null=False, blank=False, max_length=256)
    review_content = models.CharField(null=False, blank=False, max_length=1024)
    review_grade = models.PositiveSmallIntegerField(null=False, blank=False,
                                                    validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.user_id}: ->___{self.review_title}"

    class Meta:
        db_table = "recipe_reviews"

