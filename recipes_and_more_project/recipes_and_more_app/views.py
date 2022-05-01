from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .custom_queries import ingredient_name_and_amount_query, total_receipt_cal_per_100gr, search_recipe_by_category
from .models import Recipe, RecipeReviews
from .serializers import RecipeSerializer, RecipeReviewsSerializer, SpecificFullRecipeSerializer


# Displays on the main page a list of all the recipes with basic data and an image:
@api_view(['GET'])
def recipes_list(request):
    all_recipes = Recipe.objects.all()
    all_recipes_serializer = RecipeSerializer(all_recipes, many=True)
    return Response(all_recipes_serializer.data)


# Displays all the details of the recipe, including the information on ingredients and calories per 100 grams
@api_view(['GET'])
def full_recipe_by_id(request, receipt_id):
    if request.method == 'GET':
        ingredient_name_amount_result = ingredient_name_and_amount_query(receipt_id)
        total_receipt_cal_per_100gr_result = total_receipt_cal_per_100gr(receipt_id)
        specific_full_recipe = Recipe.objects.get(id=receipt_id)
        serializer_specific_full_recipe = SpecificFullRecipeSerializer(specific_full_recipe)
        ret_val = dict(serializer_specific_full_recipe.data)
        ret_val['receipt_cal_per_100gr'] = total_receipt_cal_per_100gr_result
        ret_val['ingredient_name_amount_result'] = ingredient_name_amount_result
        return Response(ret_val, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def recipe_reviews(request, recipe_id):
    if request.method == 'GET':
        recipe_reviews_list = RecipeReviews.objects.filter(recipe_id=recipe_id)
        serializer_recipe_reviews_list = RecipeReviewsSerializer(recipe_reviews_list, many=True)
        return Response(serializer_recipe_reviews_list.data)

    elif request.method == 'POST':
        serializer_recipe_reviews_list = RecipeReviewsSerializer(data=request.data)
        if serializer_recipe_reviews_list.is_valid():
            serializer_recipe_reviews_list.save()
            return Response(serializer_recipe_reviews_list.data, status=status.HTTP_201_CREATED)
        return Response(serializer_recipe_reviews_list.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recipe_search_by_category(request, category):
    if request.method == 'GET':
        search_recipe_by_category_result = search_recipe_by_category(category)
        return Response(search_recipe_by_category_result, status=status.HTTP_200_OK)

