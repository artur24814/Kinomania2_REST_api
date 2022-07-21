import pytest
from rest_framework.test import APIClient
from kinomaniaApi.models import Person, Movie, Cinema, Screening
from kinomaniaApi.management.commands.addactorsdirectorsfilms import popular_actors_directors_film

from django.utils import timezone
now = timezone.now()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def actor():
    actor = Person.objects.create(name=popular_actors_directors_film[1][0])
    return actor

@pytest.fixture
def director():
    director = Person.objects.create(name=popular_actors_directors_film[2][2], position='director')
    return director

@pytest.fixture
def movie(director, actor):
    movie = Movie.objects.create(title='Django', description='Django', director=director, year=2009)
    movie.actors.add(actor)
    return movie

@pytest.fixture
def cinema():
    cinema = Cinema.objects.create(name='kinomania')
    return cinema

@pytest.fixture
def screening(movie, cinema):
    screening = Screening.objects.create(cinema=cinema, movie=movie, date=now)
    return screening