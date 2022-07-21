from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=128, choices=(('actor', 'actor'),('director','director')), default='actor')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    director = models.ForeignKey(Person, related_name="movies_directed", on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    actors = models.ManyToManyField(Person, related_name="movies_cast")

    def __str__(self):
        return self.title

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    movies = models.ManyToManyField(Movie, through="Screening")

    def __str__(self):
        return self.name


class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
