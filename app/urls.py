from django.urls import path, re_path
from django.contrib.auth import views as auth_views #import this

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("add_recipe", views.add_recipe, name="add_recipe"),
    path("my_recipe", views.my_recipe, name="my_recipe"),
    path("logout", views.logout_request, name= "logout"),
    path("recipes/<category>/<id>", views.view_recipe, name="view_recipe")
]