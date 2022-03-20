from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Recipe)
admin.site.register(IngredientCalories)
admin.site.register(ReceiptIngredient)
# admin.site.register(CustomUser)
admin.site.register(RecipeReviews)
