import pytest
from kinomaniaApi.models import Movie, Cinema, Screening


@pytest.mark.django_db
def test_MovieListCreatingView(client, actor, director):
    response = client.get('/kinomania/movies/')
    director_name = director.name
    actor_name = actor.name
    response_post = client.post(path='/kinomania/movies/', data={'title': 'Die Hard',
                                                      'director': director_name,
                                                      'year': 2009,
                                                      'actors': actor_name})
    count_movie = Movie.objects.all().count()

    assert response.status_code == 200
    assert response_post.status_code == 201
    assert count_movie == 1

@pytest.mark.django_db
def test_MovieRetrieveUpdateDeleteView(client, movie):
    response = client.get('/kinomania/movies/1/')
    count_movie = Movie.objects.all().count()

    response_put = client.put('/kinomania/movies/1/', {'title': movie.title,
                                                 'director': movie.director,
                                                 'description': 'some new description',
                                                 'year': 2000,
                                                 'actors': movie.actors.first()
                                                 })

    response_delete = client.delete('/kinomania/movies/1/')
    count_movie_after_delete = Movie.objects.all().count()

    assert response.status_code == 200
    assert count_movie == 1
    assert response_put.status_code == 200
    assert response_delete.status_code == 204
    assert count_movie_after_delete == 0

@pytest.mark.django_db
def test_CinemaListCreatingView(client):
    response = client.get('/kinomania/cinema/')

    response_post = client.post('/kinomania/cinema/', data={"name": 'kinomania'})
    count_cinema = Cinema.objects.all().count()

    assert response.status_code == 200
    assert response_post.status_code == 201
    assert count_cinema == 1

@pytest.mark.django_db
def test_CinemaRetrieveDeleteView(client, cinema):
    response = client.get('/kinomania/cinema/1/')
    count_cinema = Cinema.objects.all().count()

    response_delete = client.delete('/kinomania/cinema/1/')
    count_cinema_after_delete = Cinema.objects.all().count()

    assert count_cinema == 1
    assert response.status_code == 200
    assert response_delete.status_code == 204
    assert count_cinema_after_delete == 0

@pytest.mark.django_db
def test_ScreeningListCreatingView(client, movie, cinema, screening):
    response = client.get('/kinomania/screening/')

    response_post = client.post('/kinomania/screening/', data={'cinema': cinema.name,
                                                               'movie': movie.title,
                                                               'date': screening.date
    })
    count_screening = Screening.objects.all().count()

    assert response.status_code == 200
    assert response_post.status_code == 201
    assert count_screening == 2

@pytest.mark.django_db
def test_ScreeningDeleteViews(client,screening):
    response = client.get('/kinomania/screening/1/')
    count_screening = Screening.objects.all().count()

    response_delete = client.delete('/kinomania/screening/1/')
    count_screening_after_delete = Screening.objects.all().count()

    assert count_screening == 1
    assert response.status_code == 200
    assert response_delete.status_code == 204
    assert count_screening_after_delete == 0
