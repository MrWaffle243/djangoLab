from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthDate = models.DateField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    category = models.CharField(max_length=50, default="General")
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


