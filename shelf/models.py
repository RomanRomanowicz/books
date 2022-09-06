from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256)
    pic = models.ImageField()


class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    pic = models.FileField(upload_to='book_pic')


class Sfelf(models.Model):
    pass