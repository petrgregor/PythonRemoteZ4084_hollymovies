from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, \
    CreateView, UpdateView, DeleteView

from viewer.forms import GenreForm, MovieModelForm, CountryModelForm, \
    CreatorModelForm, GenreModelForm, ImageModelForm
from viewer.mixins import StaffRequiredMixin
from viewer.models import Movie, Creator, Country, Genre


@login_required
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


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


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


class CreatorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.add_creator'

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CreatorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.change_creator'

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CreatorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.delete_creator'


class CountriesListView(LoginRequiredMixin, ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'


class CountryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'country.html'
    model = Country
    context_object_name = 'country'


class CountryCreateView(StaffRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    success_url = reverse_lazy('countries')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CountryUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    model = Country
    success_url = reverse_lazy('countries')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class CountryDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Country
    success_url = reverse_lazy('countries')


class GenresListView(LoginRequiredMixin, ListView):
    template_name = 'genres.html'
    model = Genre
    context_object_name = 'genres'


class GenreDetailView(LoginRequiredMixin, DetailView):
    template_name = 'genre.html'
    model = Genre
    context_object_name = 'genre'


class GenreFormView(StaffRequiredMixin, FormView):
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


class GenreUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    model = Genre
    success_url = reverse_lazy('genres')

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)


class GenreDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')


class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_image'
