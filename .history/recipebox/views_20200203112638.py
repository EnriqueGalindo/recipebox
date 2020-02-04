from .models import Recipe
from d

def index_view(request):
    recipes = Recipe.objects.all()
    return render