from rest_framework.serializers import ModelSerializer

from viewer.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        #fields = '__all__'
        fields = ['title_orig', 'title_cz', 'length', 'description',
                  'year', 'genres', 'countries', 'actors', 'directors',
                  'composers']

