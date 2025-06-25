"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path, include

from accounts.views import user_logout, SignUpView
from hollymovies import settings
from viewer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('movies/', MoviesListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie'),
    #path('movie/create/', MovieFormView.as_view(), name='movie_create'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('creators/', CreatorsListView.as_view(), name='creators'),
    path('creator/<int:pk>/', CreatorDetailView.as_view(), name='creator'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<int:pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('actors/', ActorsView.as_view(), name='actors'),
    path('countries/', CountriesListView.as_view(), name='countries'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('genres/', GenresListView.as_view(), name='genres'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre'),
    path('genre/create/', GenreFormView.as_view(), name='genre_create'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),

    path('accounts/login/', LoginView.as_view(template_name='form.html'), name='login'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name='form.html'),
         name='password_change'),
    # ostatní defaultní cesty
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
