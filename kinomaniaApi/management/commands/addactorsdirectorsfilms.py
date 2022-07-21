from django.core.management.base import BaseCommand
from kinomaniaApi.models import Person, Movie

import wikipedia


popular_actors_directors_film = [
    ['Will Smith','I Am Legend', 'Francis Lawrence', 2009],
    ['Bruce Willis', 'Twelve Monkeys', 'Jonathan Lynn', 2001],
    ['Leonardo DiCaprio', 'The Wolf of Wall Street', 'Martin Scorsese', 2010],
    ['Anthony Hopkins', 'Hannibal', 'Ridley Scott', 1999],
    ['Brad Pitt', 'Once Upon a Time ... in Hollywood', 'Quentin Tarantino', 2019],
    ['Robert Downey Jr.', 'Captain America: Civil War', 'Jon Favreau', 2010],
    ['Al Pacino', 'House of Gucci', 'Francis Ford Coppola', 2021],
]

class Command(BaseCommand):
    help = 'Populates grades for students'

    def create_actors(self):
        for actor in popular_actors_directors_film:
            Person.objects.create(name=actor[0])

    def create_director(self):
        for director in popular_actors_directors_film:
            Person.objects.create(name=director[2], position='director')

    def create_movie(self):
        for movie in popular_actors_directors_film:
            actors = Person.objects.get(name=movie[0])
            title = movie[1]
            description = wikipedia.summary(str(title))
            director = Person.objects.get(name=movie[2])
            movie = Movie.objects.create(title=title,
                                description=description,
                                director=director,
                                year=movie[3]
                                )
            movie.actors.add(actors)

    def handle(self, *args, **options):
        self.create_actors()
        self.stdout.write(self.style.SUCCESS("Succesfully add actors"))
        self.create_director()
        self.stdout.write(self.style.SUCCESS("Succesfully add directors"))
        self.create_movie()
        self.stdout.write(self.style.SUCCESS("Succesfully create movies"))

