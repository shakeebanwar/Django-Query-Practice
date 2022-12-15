from django.db import models

# Create your models here.
class Author(models.Model):
    nickname = models.CharField(max_length=20, null=True, blank=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    birth_date = models.DateField()
class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=100)
    category = models.CharField(max_length=50)
    published = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    rating = models.IntegerField()