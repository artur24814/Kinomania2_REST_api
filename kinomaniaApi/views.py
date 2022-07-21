from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Cinema, Screening
from .serializers import MovieSerializer, CinemaSerialiser, ScreeningSerialiser

import wikipedia
from requests import get
from django.contrib.gis.geoip2 import GeoIP2



class MovieListCreatingView(APIView):
    """
    a view for creating and see list all movies
    """

    serializer_class = MovieSerializer

    def get(self, request):
        serializer_context = {
            'request': request,
        }
        movies = Movie.objects.all()

        serializer = self.serializer_class(instance=movies, many=True, context=serializer_context)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description') or None
            if description is None:
                try:
                    description = wikipedia.summary(str(title))
                except Exception:
                    description = title
            serializer.save(description=description)
            response = {
                'message': "movie is create",
                'data': data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


MovieListCreating = MovieListCreatingView.as_view()


class MovieRetrieveUpdateDeleteView(APIView):
    """
    a view for get movie detail view, update and delete movie
    """

    serializer_class = MovieSerializer

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        serializer_context = {
            'request': request,
        }

        serializer = self.serializer_class(instance=movie, context=serializer_context)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        data = request.data

        serializer = self.serializer_class(instance=movie, data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Movie updated',
                'data': data
            }

            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


MovieDetailUpdateDelete = MovieRetrieveUpdateDeleteView.as_view()

class CinemaListCreatingView(APIView):
    """
    Views for get ang create cinema
    if you didn't wright city, it will add automatically, checking your public id and find your city
    """
    serializer_class = CinemaSerialiser

    def get(self, request):
        serializer_context = {
            'request': request,
        }

        cinemas = Cinema.objects.all()

        serializer = self.serializer_class(instance=cinemas, many=True, context=serializer_context)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            #check cinema
            city = serializer.validated_data.get('city') or None
            #if in label cinema nothing
            if city is None:
                g = GeoIP2('geoip')
                ip = get('https://api.ipify.org').content.decode('utf8')
                city_from_ip = g.city(f'{ip}')
                city = city_from_ip['city']
                serializer.save(city=city)
            response = {
                'message': "cinema is create",
                'data': data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

CinemaListCreating = CinemaListCreatingView.as_view()

class CinemaRetrieveDeleteView(APIView):
    """
    a view for get cinema detail view and delete cinema
    """

    serializer_class = CinemaSerialiser

    def get(self, request, pk):
        serializer_context = {
            'request': request,
        }
        cinema = get_object_or_404(Cinema, pk=pk)
        #get all screening at this cinema
        screenings = Screening.objects.filter(cinema=cinema.id)
        screnings_in_cinema = {}
        for screening in screenings:
            screnings_in_cinema[f'{screening.movie}'] = f'{screening.date}'
        serializer = self.serializer_class(instance=cinema, context=serializer_context)

        response = {
            'screenings': screnings_in_cinema,
            'data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cinema = get_object_or_404(Cinema, pk=pk)

        cinema.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

CinemaRetrieveDelete = CinemaRetrieveDeleteView.as_view()


class ScreeningListCreatingView(APIView):
    """
    views for get and create screening
    """

    serializer_class = ScreeningSerialiser

    def get(self, request):
        serializer_context = {
            'request': request,
        }

        screenings = Screening.objects.all()

        serializer = self.serializer_class(instance=screenings, many=True, context=serializer_context)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': "screening is create",
                'data': data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

ScreeningListCreating = ScreeningListCreatingView.as_view()

class ScreeningDeleteViews(APIView):
    """
    views for get screening detail and delete screening
    """

    serializer_class = ScreeningSerialiser

    def get(self, request, pk):
        serializer_context = {
            'request': request,
        }

        screenings = Screening.objects.get(pk=pk)

        serializer = self.serializer_class(instance=screenings, context=serializer_context)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        screening = get_object_or_404(Screening, pk=pk)

        screening.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

ScreeningDelete = ScreeningDeleteViews.as_view()
