from django.shortcuts import render, redirect

from library.web.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from library.web.helpers import get_profile
from library.web.models import Book


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    books_lists = []
    current_list = []
    count = 1
    for book in books:
        current_list.append(book)
        if count % 3 == 0:
            books_lists.append(current_list)
            current_list = []
        count += 1

    if current_list:
        books_lists.append(current_list)

    context = {
        'profile': profile,
        'books_lists': books_lists,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBookForm()

    context = {
        'form': form,
        'profile':profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
        'profile':profile,
    }
    return render(request, 'edit-book.html', context)


def show_book_details(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    books = Book.objects.all()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
