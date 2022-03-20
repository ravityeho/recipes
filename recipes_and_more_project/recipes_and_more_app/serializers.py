from rest_framework import serializers

from .models import Recipe, RecipeReviews


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe_category', 'recipe_name', 'recipe_description', 'preparation_time',
                  'total_time', 'pic_url', 'difficulty_level']


class SpecificFullRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe_category', 'recipe_name', 'recipe_description', 'preparation_time',
                  'total_time', 'recipe_content', 'pic_url', 'difficulty_level']


class RecipeReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeReviews
        fields = '__all__'
