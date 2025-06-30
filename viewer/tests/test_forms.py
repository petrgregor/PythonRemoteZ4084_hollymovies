from django.test import TestCase

from viewer.forms import CreatorModelForm
from viewer.models import Country


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
