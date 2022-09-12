from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from pytz import timezone

User = get_user_model()

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    recipe_name =  models.CharField(max_length=1000, default="")
    recipe_description =  models.TextField(max_length=10000, default="")
    ingredients =  models.CharField(max_length=10000, default="")
    category =  models.CharField(max_length=1000, default="")
    images = models.ImageField(upload_to='images/', default="")
    image = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.recipe_name

