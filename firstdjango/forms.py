from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "year", "author", "price", "synopsis", "category"]

    def clean_year(self):
        year = self.cleaned_data["year"]

        if year > date.today().year:
            raise ValidationError("The year published cannot be in the future.")

        if year < 1440:
            raise ValidationError("The printing press was not invented until 1440.")

        return year

    def clean_title(self):
        # Check if insert or update (new book or editing book)
        isInsert = self.instance.pk == None

        title = self.cleaned_data["title"]

        if isInsert and Book.objects.filter(title__iexact=title).exists():
            raise ValidationError("A book of that title already exists")

        return title

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "birthDate"]

    def clean_birthDate(self):
        birthDate = self.cleaned_data["birthDate"]

        if birthDate > date.today():
            raise ValidationError("Author cannot be born in the future")
        
        return birthDate
