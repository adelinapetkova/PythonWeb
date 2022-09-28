from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from recipes.main.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes.main.helpers import get_recipe
from recipes.main.models import Recipe


def show_home(request):
    recipes = get_recipe()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeCreateForm(request.POST)

        if recipe_form.is_valid():
            recipe = Recipe(
                title=recipe_form.cleaned_data['title'],
                image_url=recipe_form.cleaned_data['image_url'],
                description=recipe_form.cleaned_data['description'],
                ingredients=recipe_form.cleaned_data['ingredients'],
                time=recipe_form.cleaned_data['time'],
            )
            recipe.save()
            return redirect('index')
    else:
        recipe_form = RecipeCreateForm()

    context = {
        'recipe_form': recipe_form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe_to_edit=Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe_form = RecipeEditForm(request.POST)

        if recipe_form.is_valid():
            recipe_to_edit.title = recipe_form.cleaned_data['title']
            recipe_to_edit.image_url=recipe_form.cleaned_data['image_url']
            recipe_to_edit.description=recipe_form.cleaned_data['description']
            recipe_to_edit.ingredients=recipe_form.cleaned_data['ingredients']
            recipe_to_edit.time=recipe_form.cleaned_data['time']
            recipe_to_edit.save()
            return redirect('index')
    else:
        recipe_form = RecipeEditForm(initial=recipe_to_edit.__dict__)

    context = {
        'recipe_edit_form': recipe_form,
        'recipe_to_edit': recipe_to_edit,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe_to_delete = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe_form = RecipeDeleteForm(request.POST)
        recipe_to_delete.delete()
        return redirect('index')
    else:
        recipe_form = RecipeDeleteForm(initial=recipe_to_delete.__dict__)

    context = {
        'recipe_delete_form': recipe_form,
        'recipe_to_delete': recipe_to_delete,
    }
    return render(request, 'delete.html', context)


def show_recipe_details(request, pk):
    recipe_for_details = Recipe.objects.get(pk=pk)
    context={
        'recipe_for_details': recipe_for_details,
        'ingredients_list': recipe_for_details.ingredients.split(','),
    }
    return render(request, 'details.html', context)
