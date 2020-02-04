from django.shortcuts import render
from .models import Recipe, Author


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})


def author_view(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=auth)
    return render(request, "author.html", {"recipes": recipes, "author":author})


def recipes_view(request, id):
    recipes = Recipe.objects.get(id=id)
    return render(request, "recipe.html", {"recipes": recipes})
