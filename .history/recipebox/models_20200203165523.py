from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField

def __str__(self:
    )
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=15)
    instructions = models.TextField()
