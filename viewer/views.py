from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from viewer.models import Movie, Creator


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
