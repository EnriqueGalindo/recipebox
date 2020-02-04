from .models import Recipe
from

def index_view(request):
    recipes = Recipe.objects.all()
    return render