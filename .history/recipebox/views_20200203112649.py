
from .models import Recipe

def index_view(request):
    recipes = Recipe.objects.all()
    return render