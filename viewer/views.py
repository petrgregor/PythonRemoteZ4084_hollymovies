from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, \
    CreateView, UpdateView, DeleteView

from accounts.models import Profile
from viewer.forms import GenreForm, MovieModelForm, CountryModelForm, \
    CreatorModelForm, GenreModelForm, ImageModelForm, ReviewModelForm
from viewer.mixins import StaffRequiredMixin
from viewer.models import Movie, Creator, Country, Genre, Review, Image


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

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['review_form'] = ReviewModelForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewModelForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            profile = Profile.objects.get(user=request.user)

            if Review.objects.filter(movie=self.object, reviewer=profile).exists():
                review = Review.objects.get(movie=self.object, reviewer=profile)
                review.rating = rating
                review.comment = comment
                review.save()
            else:
                Review.objects.create(
                    movie=self.object,
                    reviewer=profile,
                    rating=rating,
                    comment=comment
                )

            return redirect(reverse('movie', kwargs={'pk': self.object.pk}))

        return redirect('movies')



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


class ImageListView(PermissionRequiredMixin, ListView):
    template_name = 'images.html'
    model = Image
    context_object_name = 'images'
    permission_required = 'viewer.view_images'


class ImageDetailView(DetailView):
    template_name = 'image.html'
    model = Image
    context_object_name = 'image'


class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('images')
    permission_required = 'viewer.add_image'


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    model = Image
    success_url = reverse_lazy('images')
    permission_required = 'viewer.change_image'


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Image
    success_url = reverse_lazy('images')
    permission_required = 'viewer.delete_iamge'


class ReviewDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model = Review
    success_url = reverse_lazy('movies')


def name_day(request):
    url = "https://svatky.adresa.info/json?lang=cs"
    #print(f"url: {url}")
    result_request = requests.get(url)
    #print(f"result_request: {result_request}")
    result_json = result_request.json()
    #print(f"result_json: {result_json}")
    name = result_json[0]['name']
    context = {'name': name}
    return render(request, 'nameday.html', context)


def search(request):
    if request.method == 'POST':
        search_string = request.POST.get('search').strip()
        if search_string:
            movies_title_orig = Movie.objects.filter(title_orig__contains=search_string)
            movies_title_cz = Movie.objects.filter(title_cz__contains=search_string)
            movies_description = Movie.objects.filter(description__contains=search_string)

            creator_name = Creator.objects.filter(name__contains=search_string)
            creator_artistic_name = Creator.objects.filter(artistic_name__contains=search_string)
            creator_surname = Creator.objects.filter(surname__contains=search_string)

            movie_genre = Movie.objects.filter(genres__name__contains=search_string)
            movie_country = Movie.objects.filter(countries__name__contains=search_string)

            context = {
                'search': search_string,
                'movie_title_orig': movies_title_orig,
                'movie_title_cz': movies_title_cz,
                'movie_description': movies_description,
                'creator_name': creator_name,
                'creator_artistic_name': creator_artistic_name,
                'creator_surname': creator_surname,
                'movie_genre': movie_genre,
                'movie_country': movie_country
            }

            return render(request, 'search.html', context)
    return render(request, 'home.html')
