from django.shortcuts import render
from .models import Recipe


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})


def author_view(request):
    recipes = Recipe.objects.all()
    return render(request, "author.html", {"recipes": recipes})


def recipes_view(request, id):
    recipes = Recipe.objects.get(id=id)
    return render(request, "recipe.html", {"recipes": recipes})
