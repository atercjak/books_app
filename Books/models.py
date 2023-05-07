from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=150, null=True)
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    name = models.CharField(max_length=120)
    books = models.ManyToManyField(Book, related_name='books')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_bookshelves')

    def __str__(self):
        return self.name
