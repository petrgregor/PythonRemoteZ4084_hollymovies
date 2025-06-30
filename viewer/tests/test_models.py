import datetime

from django.test import TestCase

from viewer.models import Movie, Genre, Country, Creator


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title_orig='Originální název filmu',
            title_cz='Český název filmu',
            length=123,
            description='Popis filmu',
            year=2000
        )

        genre_drama = Genre.objects.create(name='Drama')
        genre_comedy = Genre.objects.create(name='Komedie')
        movie.genres.add(genre_drama)
        movie.genres.add(genre_comedy)

        country_cz = Country.objects.create(name='Česko')
        country_sk = Country.objects.create(name='Slovensko')
        movie.countries.add(country_cz)
        movie.countries.add(country_sk)
        movie.countries.add(country_cz)

        creator1 = Creator.objects.create(
            name='Arnošt',
            surname='Novák',
            date_of_birth=datetime.date(1975, 10, 12),
            country=country_cz,
            biography="Režisér několika filmů."
        )
        movie.directors.add(creator1)

        creator2 = Creator.objects.create(
            artistic_name='Umělec',
            country=country_sk,
            date_of_birth=datetime.date(2001, 5, 4),
            biography='Skvělý herec.'
        )
        creator3 = Creator.objects.create(
            surname='Svoboda',
            country=country_cz,
            date_of_birth=datetime.date(1940, 4, 16),
            date_of_death=datetime.date(2021, 10, 10),
            biography='Legendární herec.'
        )
        movie.actors.add(creator2)
        movie.actors.add(creator3)

        movie.save()

        movie2 = Movie.objects.create(
            title_orig='Pelíšky',
            length=41
        )

    def setUp(self):
        print('-' * 80)

    def test_title_orig(self):
        movie = Movie.objects.get(id=1)
        print(f"test_title_orig: '{movie.title_orig}'")
        self.assertEqual(movie.title_orig, 'Originální název filmu')

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        print(f"test_movie_str: '{movie.__str__()}'")
        self.assertEqual(movie.__str__(), 'Originální název filmu (2000)')

        movie2 = Movie.objects.get(id=2)
        print(f"test_movie_str: '{movie2.__str__()}'")
        self.assertEqual(movie2.__str__(), 'Pelíšky')

    def test_movie_countries_count(self):
        movie = Movie.objects.get(id=1)
        number_of_countries = movie.countries.count()
        print(f"test_movie_countries_count: {number_of_countries}")
        self.assertEqual(number_of_countries, 2)

    def test_length_format(self):
        movie = Movie.objects.get(id=1)
        print(f"test_length_format: {movie.length_format()}")
        self.assertEqual(movie.length_format(), "2:03")

        movie2 = Movie.objects.get(id=2)
        print(f"test_length_format: {movie2.length_format()}")
        self.assertEqual(movie2.length_format(), "0:41")

    def test_creator_full_name(self):
        creator = Creator.objects.get(id=1)
        print(f"test_creator_full_name: {creator.full_name()}")
        self.assertEqual(creator.full_name(), "Arnošt Novák")

