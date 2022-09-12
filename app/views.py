from crypt import methods
from unicodedata import name
from django.shortcuts import render, redirect
from .forms import NewUserForm, RecipeForm
from .models import Recipe
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import requests



def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        return render(request=request, template_name="app/register.html", context={"register_form": form})
    form = NewUserForm()
    return render(request=request, template_name="app/register.html", context={"register_form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "app/login.html", {"login_form": form})
    form = AuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"login_form": form})


def index(request):
    
    all_recipe = Recipe.objects.all()
    return render(request, 'app/index.html', {'all_recipe': all_recipe, 'count': len(all_recipe)})


def add_recipe(request):

    if request.method == 'POST':
        if(request.POST.get('recipe_id') != None):
            print(request.POST.get('recipe_id'))

            recipe = Recipe.objects.get(id=int(request.POST.get('recipe_id')))
            form = RecipeForm(instance=recipe)

            return render(request, "app/add_recipe.html", {'user': request.user, 'form': form, 'edit': request.POST.get('recipe_id')})
        else:
            form = RecipeForm(request.POST, request.FILES)

            if request.POST.get('edit') != None:
                recipe = Recipe.objects.get(
                    id=int(request.POST.get('id')))
                form = RecipeForm(request.POST, request.FILES, instance=recipe)

            if form.is_valid():
                obj = form.save()
                obj.owner = request.user
                obj.save()
                return redirect("/")
            else:
                return render(request, "app/add_recipe.html", {'user': request.user, 'form': form})
    else:
        form = RecipeForm()
        # print(request.user.id)
        return render(request, "app/add_recipe.html", {'user': request.user, 'form': form})


def my_recipe(request):
    user_recipe = []
    if( request.method == "POST"):
        Recipe.objects.filter(id=int(request.POST.get('delete'))).delete()
        return redirect('my_recipe')
    if(request.user.is_authenticated):
        user_recipe = Recipe.objects.filter(owner=request.user)
    return render(request=request, template_name='app/my_recipe.html', context={'user': request.user, 'my_recipe': user_recipe})


def view_recipe(request, category, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, "app/view_recipe.html", {'recipe': recipe})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")
