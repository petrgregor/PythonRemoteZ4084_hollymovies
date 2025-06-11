from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, \
    CreateView, UpdateView, DeleteView

from viewer.forms import GenreForm, MovieModelForm, CountryModelForm, \
    CreatorModelForm, GenreModelForm
from viewer.models import Movie, Creator, Country, Genre


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


class MovieFormView(FormView):
    template_name = 'form.html'
    #form_class = MovieForm
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title_orig=cleaned_data['title_orig'],
            title_cz=cleaned_data['title_cz'],
            #genres=cleaned_data['genres'],
            # a dalšé položky z formuláře
        )
        return result

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    model = Movie
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


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


class CreatorCreateView(CreateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CreatorUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    model = Creator
    success_url = reverse_lazy('creators')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CreatorDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Creator
    success_url = reverse_lazy('creators')


class CountriesListView(ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'


class CountryDetailView(DetailView):
    template_name = 'country.html'
    model = Country
    context_object_name = 'country'


class CountryCreateView(CreateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    success_url = reverse_lazy('countries')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CountryUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    model = Country
    success_url = reverse_lazy('countries')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CountryDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Country
    success_url = reverse_lazy('countries')


class GenresListView(ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    template_name = 'genre.html'
    model = Genre
    context_object_name = 'genre'


class GenreFormView(FormView):
    template_name = 'form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data['name']
        )
        return result

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class GenreUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    model = Genre
    success_url = reverse_lazy('genres')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class GenreDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')
