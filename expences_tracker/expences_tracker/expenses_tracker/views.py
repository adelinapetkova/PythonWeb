from django.shortcuts import render, redirect

from expences_tracker.expenses_tracker.forms import CreateProfileForm, CreateEditExpenseForm, DeleteExpenseForm, \
    EditProfileForm
from expences_tracker.expenses_tracker.helpers import get_profile
from expences_tracker.expenses_tracker.models import Profile, Expense


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    total_price_expenses = 0
    for ex in expenses:
        total_price_expenses += ex.price

    context = {
        'profile': profile,
        'expenses': expenses,
        'left': profile.budget - total_price_expenses,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = Profile(**form.cleaned_data)
            profile.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        create_expense_form = CreateEditExpenseForm(request.POST)
        if create_expense_form.is_valid():
            expense = Expense(**create_expense_form.cleaned_data)
            expense.save()
            return redirect('index')
    else:
        create_expense_form = CreateEditExpenseForm()

    context = {
        'create_expense_form': create_expense_form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense_to_edit = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        edit_expense_form = CreateEditExpenseForm(request.POST)
        if edit_expense_form.is_valid():
            expense_to_edit.title = edit_expense_form.cleaned_data['title']
            expense_to_edit.expense_image = edit_expense_form.cleaned_data['expense_image']
            expense_to_edit.description = edit_expense_form.cleaned_data['description']
            expense_to_edit.price = edit_expense_form.cleaned_data['price']
            expense_to_edit.save()
            # save_to_do
            return redirect('index')
    else:
        edit_expense_form = CreateEditExpenseForm(initial=expense_to_edit.__dict__)

    context = {
        'edit_expense_form': edit_expense_form,
        'expense_to_edit': expense_to_edit,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense_to_delete = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        delete_expense_form = DeleteExpenseForm(request.POST)
        expense_to_delete.delete()
        return redirect('index')
    else:
        delete_expense_form = DeleteExpenseForm(initial=expense_to_delete.__dict__)

    context = {
        'expense_to_delete': expense_to_delete,
        'delete_expense_form': delete_expense_form,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses_list = Expense.objects.all()
    total_number_of_items = len(expenses_list)
    total_for_expenses = 0

    for ex in expenses_list:
        total_for_expenses += ex.price

    left_budget = profile.budget - total_for_expenses

    context = {
        'profile': profile,
        'expenses_list': expenses_list,
        'total_number_of_items': total_number_of_items,
        'left_budget': left_budget,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile_to_edit = get_profile()

    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES)
        if edit_form.is_valid():
            profile_to_edit.profile_image=edit_form.cleaned_data['profile_image']
            profile_to_edit.budget=edit_form.cleaned_data['budget']
            profile_to_edit.first_name=edit_form.cleaned_data['first_name']
            profile_to_edit.last_name=edit_form.cleaned_data['last_name']
            profile_to_edit.save()

        return redirect('show profile')
        # save_to_do
    else:
        edit_form = EditProfileForm(initial=profile_to_edit.__dict__)

    context={
        'profile_to_edit':profile_to_edit,
        'edit_form': edit_form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile=get_profile()
    expenses=Expense.objects.all()
    if request.method=='POST':
        profile.delete()
        for ex in expenses:
            ex.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')
