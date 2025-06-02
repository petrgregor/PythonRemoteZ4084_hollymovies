from django.shortcuts import render

from viewer.models import Movie


def home(request):
    return render(request, 'home.html')


def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies': movies_list}
    return render(request, 'movies.html', context)


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        return render(request, 'movie.html', {'movie': Movie.objects.get(id=pk)})
    return render(request, 'home.html')
