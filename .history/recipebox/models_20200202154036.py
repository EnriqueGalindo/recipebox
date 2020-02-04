from django.db import models

class Author(models.Model)
    name = models.CharField(max_length=30)
    Bio = models.TextField