from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Person, Movie, Cinema, Screening

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        pass

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)
    #movie can have many actors
    actors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Person.objects.filter(position='actor'))
    #but just one director
    director = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.filter(position='director'))

    class Meta:
        model = Movie
        fields = ['pk', "title", "year", "description", "director", "actors", 'url']

    #create method get_url() for identify url for our serializer model
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('detail-update-or-create-movie', kwargs={'pk': obj.pk}, request=request)


class CinemaSerialiser(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detail-update-or-create-movie'
    )
    class Meta:
        model = Cinema
        fields = ['id','name', 'movies', 'city']

class ScreeningSerialiser(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Screening
        fields = ['id','cinema', 'movie', 'date']

