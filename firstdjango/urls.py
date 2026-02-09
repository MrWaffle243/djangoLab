from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("books", view_all_books, name="all_books"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:bookid>", view_single_book, name="single_books"),
    path("books/year/<int:year>", view_books_from_year, name="books_from_year"),
    path("books/category/<str:category>", view_books_by_category, name="books_by_category"),
    path("books/category/<str:category>/year/<int:year>", view_books_by_category_and_year, name="books_by_category_and_year"),
    path("authors/add/", views.add_author, name="add_author"),
]

