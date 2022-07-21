from django.urls import path
from .views import MovieListCreating,MovieDetailUpdateDelete, CinemaListCreating, CinemaRetrieveDelete, ScreeningListCreating, ScreeningDelete

urlpatterns = [
    path('movies/', MovieListCreating, name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailUpdateDelete, name='detail-update-or-create-movie'),
    path('cinema/', CinemaListCreating, name='cinema-list-create'),
    path('cinema/<int:pk>/', CinemaRetrieveDelete, name='cinema-detail-delete'),
    path('screening/', ScreeningListCreating, name='screening-lict-create'),
    path('screening/<int:pk>/', ScreeningDelete, name='delete-screening')
]