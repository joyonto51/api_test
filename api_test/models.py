from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
    writter = models.CharField(max_length=20, default='Nazrul Islam')
    author = models.CharField(max_length=30, default='Kotha prokash')

    def __str__(self):
        return self.name