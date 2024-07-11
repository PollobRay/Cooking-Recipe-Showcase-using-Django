from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

# Create your views here.

def show_all_recipes(request):
    return render(request,'all_recipes.html')

def add_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description  = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe = Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        recipe.save()

        return redirect('recipes')
    return render(request,'add_recipe.html')