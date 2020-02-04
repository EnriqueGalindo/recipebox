from django.db import models

class Author(models.Model)
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=280)

class Recipe(models.Model)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)