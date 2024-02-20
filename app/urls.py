from django.urls import path

from .views import create_recipe, create_ingredient

# /recipe/

urlpatterns = [
    path('create/', create_recipe, name='create-recipe'),
    path('create/ingridient', create_ingredient, name='create-ingredient'),
]