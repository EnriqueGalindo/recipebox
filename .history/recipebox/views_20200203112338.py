from .models import Recipe

def index_view(request):
    recipes = Recipe.title.objects.all()
