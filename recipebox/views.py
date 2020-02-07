from django.shortcuts import render, redirect, reverse
from .models import Recipe, Author
from .forms import RecipeAddForm, AuthorAddForm


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})


def author_view(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, "author.html", {"recipes": recipes, "author":author})


def recipes_view(request, id):
    recipes = Recipe.objects.get(id=id)
    return render(request, "recipe.html", {"recipes": recipes})


def add_recipe_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create( 
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"]
                )
            return redirect(reverse("home"))
    form = RecipeAddForm()


def add_author_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )
            return redirect(reverse("home"))
    form = AuthorAddForm()

    return render(request, html, {'form': form})
