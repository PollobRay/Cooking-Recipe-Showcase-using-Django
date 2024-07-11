from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

# Create your views here.

def home(request):
    return render(request,"home.html")

def view_recipe(request,id):
    recipe = Recipe.objects.get(pk=id)
    return render(request,'recipe.html', context={'recipe':recipe})

def show_all_recipes(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    return render(request,'all_recipes.html', context={'recipes':queryset})

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

        return redirect('all_recipes')
    return render(request,'add_recipe.html')

def update_recipe(request,id):
    recipe = Recipe.objects.get(pk=id)

    if request.method == 'POST':
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get('recipe_image')
        
        if recipe_image:
            recipe.recipe_image=recipe_image

        recipe.save()
        return redirect('all_recipes') 
    return render(request,'update_recipe.html', context={'recipe':recipe})

def delete_recipe(request,id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return redirect('all_recipes')
