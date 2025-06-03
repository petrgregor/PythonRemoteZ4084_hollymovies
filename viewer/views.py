from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from viewer.models import Movie


def home(request):
    return render(request, 'home.html')


def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies': movies_list}
    return render(request, 'movies.html', context)


class MoviesView(View):
    def get(self, request):
        movies_list = Movie.objects.all()
        context = {'movies': movies_list}
        return render(request, 'movies.html', context)


class MoviesTemplateView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()}


class MoviesListView(ListView):
    template_name = 'movies.html'
    model = Movie
    # POZOR, defaultně se objekt poslaný do template jmenuje 'object_list'
    # buď v template používáme název 'object_list'
    # nebo můžu dodatečně přejmenovat:
    context_object_name = 'movies'


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        return render(request, 'movie.html', {'movie': Movie.objects.get(id=pk)})
    return render(request, 'home.html')


class MovieDetailView(DetailView):
    template_name = 'movie.html'
    model = Movie
    context_object_name = 'movie'
