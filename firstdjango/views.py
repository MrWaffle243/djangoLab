from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, "all_books.html", {"books": all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, "single_book.html", {"book":single_book})

def view_books_from_year(request, year):
    books_from_year = Book.objects.filter(year=year)
    return render(request, "books_from_year.html", {"books": books_from_year, "year":year})

def view_books_by_category(request, category):
    books_by_category = Book.objects.filter(category=category)
    return render(request, "books_by_category.html", {"books": books_by_category, "category":category})

def view_books_by_category_and_year(request, category, year):
    books_by_category_and_year = Book.objects.filter(category=category, year=year)
    return render(request, "books_by_category_and_year.html", {"books": books_by_category_and_year, "category":category, "year":year})

@login_required
#@user_passes_test(lambda u: u.is_staff) So only staff can add books
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect("all_books")
    else:
        form = BookForm()

    return render(request, "add_book.html", {"form": form})

@login_required
def edit_book(request, bookid):
    # Get book or 404 if doesn't exist
    book = get_object_or_404(Book, id=bookid)

    # Check auth: user that added it OR staff
    if not request.user.is_staff and book.added_by != request.user:
        return HttpResponseForbidden("You can only edit books you added.")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('single_book', bookid=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, bookid):
    # Get book or 404 if doesn't exist
    book = get_object_or_404(Book, id=bookid)

    # Check auth: user that added it OR staff
    if not request.user.is_staff and book.added_by != request.user:
        return HttpResponseForbidden("You can only delete books you added.")

    if request.method == 'POST':
        book.delete()
        return redirect('all_books')

    return render(request, 'confirm_delete.html', {'book': book})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_books") # Redirect to all books, as theres no author page
    else:
        form = AuthorForm()

    return render(request, "add_author.html", {"form": form})

def register(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    user = request.user

    return render(request, "profile.html", {"user": user})
