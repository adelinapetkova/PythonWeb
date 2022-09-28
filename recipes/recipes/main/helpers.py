from recipes.main.models import Recipe


def get_recipe():
    recipes = Recipe.objects.all()
    if recipes:
        return recipes
    return None
