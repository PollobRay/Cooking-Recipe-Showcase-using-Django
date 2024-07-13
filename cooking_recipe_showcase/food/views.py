from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def add_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description  = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe = Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            user_id = request.user.id       # indicate who is adding the recipe
        )
        recipe.save()
        return redirect('all_recipes')
    return render(request,'add_recipe.html')

@login_required(login_url='login')
def update_recipe(request,id):
    recipe = Recipe.objects.get(pk=id)

    if request.method == 'POST':
        recipe.id=id
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get('recipe_image')
        
        if recipe_image:
            recipe.recipe_image=recipe_image

        recipe.save()
        return redirect('all_recipes') 
    return render(request,'update_recipe.html', context={'recipe':recipe})

@login_required(login_url='login')
def delete_recipe(request,id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return redirect('all_recipes')


def user_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        check = request.POST.getlist('check')
        #messages.success(request,user_name)

        #check username is alreay exits or not
        if User.objects.filter(username=user_name).exists():
            messages.info(request,"User Name is Already Taken")
        
        elif password != re_password:
            messages.info(request,"Two passwords are different")
        
        elif not check:
            messages.info(request,"Check to Agree all statements")

        else:
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = user_name,
                password = password 
            )
            user.set_password(user.password)
            user.save()

            messages.info(request,"Registation Successful !!!")

    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username = user_name, password = password)

        if user is None:
            messages.error(request,"Username & Password are Incorrect")
        else:
            login(request,user) # create session
            return redirect('home')

    return render(request,'login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')

@login_required(login_url='login')
def user_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        user = User.objects.get(id = request.user.id)

        #check username is alreay exits or not
        if password != re_password:
            messages.info(request,"Two passwords are different")
        
        else:
            user.first_name = first_name
            user.last_name = last_name
            user.password = password
            user.set_password(user.password)
            user.save()

            messages.info(request,"Information Updated !!!")

            return redirect('profile')

    return render(request, 'profile.html')
