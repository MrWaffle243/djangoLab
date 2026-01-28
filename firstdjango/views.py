from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

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