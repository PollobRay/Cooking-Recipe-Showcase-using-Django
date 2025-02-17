"""
URL configuration for cooking_recipe_showcase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food.views import *

urlpatterns = [
    path('', home,name='home'),
    path('home/', home,name='home'),
    path('all_recipes/', show_all_recipes, name='all_recipes'),
    path('add/', add_recipe, name='add_recipe'),
    path('recipe/<int:id>', view_recipe, name='view_recipe'),
    path('update/<int:id>', update_recipe, name='update_recipe'),
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
]

# For image visible
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()