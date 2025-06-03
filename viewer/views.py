from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from viewer.models import Movie, Creator, Country


def home(request):
    return render(request, 'home.html')


class MoviesListView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    template_name = 'movie.html'
    model = Movie
    context_object_name = 'movie'


class CreatorsListView(ListView):
    template_name = 'creators.html'
    model = Creator
    context_object_name = 'creators'


class ActorsView(View):
    def get(self, request):
        creators = Creator.objects.all()
        actors = []
        for creator in creators:
            if creator.acting.exists():
                actors.append(creator)
        return render(request, 'actors.html', {'actors': actors})


class CreatorDetailView(DetailView):
    template_name = 'creator.html'
    model = Creator
    context_object_name = 'creator'


class CountriesListView(ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'
