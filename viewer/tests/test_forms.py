import datetime

from django.test import TestCase

from viewer.forms import CreatorModelForm, MovieModelForm, ReviewModelForm
from viewer.models import Country, Genre, Creator


class CreatorTestForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        Country.objects.create(name="Česko")
        Country.objects.create(name="Slovensko")

    def test_creator_form_is_valid(self):
        creator_form = CreatorModelForm(
            data={
                'name': '    martin    ',
                'surname': '    novák   ',
                'artistic_name': '   creator   ',
                'date_of_birth': '1965-09-17',
                'date_of_death': '2002-05-11',
                'country': '1',
                'biography': '   první věta.  druhá věta.  '
            }
        )
        self.assertTrue(creator_form.is_valid())

    def test_creator_form_surname_artistic_name_is_invalid(self):
        creator_form = CreatorModelForm(
            data={
                'name': '    martin    ',
                'surname': '       ',
                'artistic_name': '      ',
                'date_of_birth': '1965-09-17',
                'date_of_death': '2002-05-11',
                'country': '1',
                'biography': '   první věta.  druhá věta.  '
            }
        )
        self.assertFalse(creator_form.is_valid())

    def test_creator_form_date_of_birth_is_invalid(self):
        creator_form = CreatorModelForm(
            data={
                'name': '    martin    ',
                'surname': '    novák   ',
                'artistic_name': '   creator   ',
                'date_of_birth': '2035-09-17',
                'date_of_death': '2125-05-11',
                'country': '1',
                'biography': '   první věta.  druhá věta.  '
            }
        )
        self.assertFalse(creator_form.is_valid())

    def test_creator_form_date_of_death_is_invalid(self):
        creator_form = CreatorModelForm(
            data={
                'name': '    martin    ',
                'surname': '    novák   ',
                'artistic_name': '   creator   ',
                'date_of_birth': '1935-09-17',
                'date_of_death': '2035-05-11',
                'country': '1',
                'biography': '   první věta.  druhá věta.  '
            }
        )
        self.assertFalse(creator_form.is_valid())

    def test_creator_form_dates_is_invalid(self):
        creator_form = CreatorModelForm(
            data={
                'name': '    martin    ',
                'surname': '    novák   ',
                'artistic_name': '   creator   ',
                'date_of_birth': '2010-09-17',
                'date_of_death': '2002-05-11',
                'country': '1',
                'biography': '   první věta.  druhá věta.  '
            }
        )
        self.assertFalse(creator_form.is_valid())


class MovieTestForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre_drama = Genre.objects.create(name='Drama')
        genre_comedy = Genre.objects.create(name='Komedie')

        country_cz = Country.objects.create(name='Česko')
        country_sk = Country.objects.create(name='Slovensko')

        creator1 = Creator.objects.create(
            name='Arnošt',
            surname='Novák',
            date_of_birth=datetime.date(1975, 10, 12),
            country=country_cz,
            biography="Režisér několika filmů."
        )

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

    def test_movie_form_is_valid(self):
        movie_form = MovieModelForm(
            data={
                'title_orig': '   originální název   ',
                'title_cz': '   Český název  ',
                'genres': ['1', '2'],
                'directors': ['1'],
                'actors': ['2', '3'],
                'length': '125',
                'description': '  popis filmu  ',
                'year': '2005',
                'countries': ['1', '2']
            }
        )
        self.assertTrue(movie_form.is_valid())

    def test_movie_form_title_orig_is_invalid(self):
        movie_form = MovieModelForm(
            data={
                'title_orig': '      ',
                'title_cz': '   Český název  ',
                'genres': ['1', '2'],
                'directors': ['1'],
                'actors': ['2', '3'],
                'length': '125',
                'description': '  popis filmu  ',
                'year': '2005',
                'countries': ['1', '2']
            }
        )
        self.assertFalse(movie_form.is_valid())

    def test_movie_form_length_is_invalid(self):
        movie_form = MovieModelForm(
            data={
                'title_orig': '   originální název   ',
                'title_cz': '   Český název  ',
                'genres': ['1', '2'],
                'directors': ['1'],
                'actors': ['2', '3'],
                'length': '-123',
                'description': '  popis filmu  ',
                'year': '2005',
                'countries': ['1', '2']
            }
        )
        self.assertFalse(movie_form.is_valid())

        movie_form = MovieModelForm(
            data={
                'title_orig': '   originální název   ',
                'title_cz': '   Český název  ',
                'genres': ['1', '2'],
                'directors': ['1'],
                'actors': ['2', '3'],
                'length': '0',
                'description': '  popis filmu  ',
                'year': '2005',
                'countries': ['1', '2']
            }
        )
        self.assertFalse(movie_form.is_valid())


class ReviewTestForm(TestCase):
    def test_form_is_valid_rating_comment(self):
        form = ReviewModelForm(
            data={
                'rating': 9,
                'comment': 'Skvělý film.'
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_is_valid_rating(self):
        form = ReviewModelForm(
            data={
                'rating': 9
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_is_valid_comment(self):
        form = ReviewModelForm(
            data={
                'comment': 'Skvělý film.'
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = ReviewModelForm(
            data={
                'rating': '',
                'comment': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_rating_zero(self):
        form = ReviewModelForm(
            data={
                'rating': 0,
                'comment': ''
            }
        )
        self.assertFalse(form.is_valid())
