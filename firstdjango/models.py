from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    category = models.CharField(max_length=50, default="General")