from django.db import models

# Create your models here.

class MovieCategories(models.Model):
    name = models.CharField(max_length=250)

class Actors(models.Model):
    Firstname = models.CharField(max_length=250)
    Lastname = models.CharField(max_length=250)
    age = models.IntegerField(max_length=250)

class FilmDirector(models.Model):
    name = models.CharField(max_length=250)
    Lastname = models.CharField(max_length=250)

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    ranking = models.IntegerField(1)
    category = models.ForeignKey(MovieCategories, on_delete=models.PROTECT)
    actor = models.ManyToManyField(Actors)
    director = models.ManyToManyField(FilmDirector)


