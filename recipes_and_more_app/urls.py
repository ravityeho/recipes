from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('recipes_list', views.recipes_list, name='recipes_list'),
    path("full_recipe_by_id/<int:receipt_id>", views.full_recipe_by_id, name='full_recipe_by_id'),
    path("recipes_list/<int:recipe_id>/recipe_reviews", views.recipe_reviews, name='recipe_reviews'),
    path("recipe_search_by_category/<str:category>", views.recipe_search_by_category,
         name='recipe_search_by_category')
]
