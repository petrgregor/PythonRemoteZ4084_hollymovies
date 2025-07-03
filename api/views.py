from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from api.serializers import MovieSerializer
from viewer.models import Movie


class Movies(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MovieDetail(RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin, GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
