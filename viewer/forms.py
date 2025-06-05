from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, \
    Textarea, ModelForm, TextInput

from viewer.models import Genre, Creator, Country, Movie


class GenreForm(Form):
    name = CharField(label='Název žánru', max_length=32, required=True)

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()


"""
class MovieForm(Form):
    title_orig = CharField(label='Originální název', max_length=64, required=True)
    title_cz = CharField(label='Český název', max_length=64, required=False)
    genres = ModelChoiceField(label='Žánry', queryset=Genre.objects, required=False)
    directors = ModelChoiceField(label='Režie', queryset=Creator.objects, required=False)
    actors = ModelChoiceField(label='Herci', queryset=Creator.objects, required=False)
    composers = ModelChoiceField(label='Hudba', queryset=Creator.objects, required=False)
    length = IntegerField(label='Délka', required=False)
    description = CharField(label='Popis', widget=Textarea, required=False)
    year = IntegerField(label='Rok', required=False)
    countries = ModelChoiceField(label='Země', queryset=Country.objects, required=False)
"""


class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        labels = {
            'title_orig': 'Originální název',
            'title_cz': 'Český název',
            'genres': 'Žánry',
            'directors': 'Režie',
            'actors': 'Herci',
            'composers': 'Hudba',
            'length': 'Délka',
            'description': 'Popis',
            'year': 'Rok',
            'countries': 'Země'
        }

        help_texts = {
            'length': 'Délka filmu v minutách.',
            'description': 'Popis filmu, stručný obsah nebo jiné detaily.'
        }

        error_messages = {
            'title_orig': {
                'required': 'Tento údaj je povinný.'
            }
        }

    title_orig = CharField(max_length=64,
                           required=True,
                           widget=TextInput(attrs={'class': 'bg-info'}),
                           label='Originální název')

    def clean_title_orig(self):
        initial = self.cleaned_data['title_orig']
        return initial.capitalize()

    def clean_title_cz(self):
        initial = self.cleaned_data['title_cz']
        if initial:
            return initial.capitalize()
        return initial

    def clean_length(self):
        initial = int(self.cleaned_data['length'])
        if initial is not None and initial <= 0:
            raise ValidationError('Délka filmu musí být kladné číslo.')
        return initial


class CountryModelForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

        labels = {
            'name': 'Název země'
        }

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()

