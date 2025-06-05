import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, \
    Textarea, ModelForm, TextInput, DateField, NumberInput

from viewer.models import Genre, Creator, Country, Movie


class GenreForm(Form):
    name = CharField(label='Název žánru', max_length=32, required=True)

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

        labels = {
            'name': 'Název žánru'
        }

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


class CreatorModelForm(ModelForm):
    class Meta:
        model = Creator
        #fields = ['name', 'surname', 'artistic_name']
        #exclude = ['biography']
        fields = '__all__'

        labels = {
            'name': 'Jméno',
            'surname': 'Příjmení',
            'artistic_name': 'Umělecké jméno',
            'date_of_birth': 'Datum narození',
            'date_of_death': 'Datum úmrtí',
            'country': 'Země',
            'biography': 'Biografie'
        }

    date_of_birth = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label='Datum narození')
    date_of_death = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label='Datum úmrtí')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        initial = self.cleaned_data['name']
        if initial:
            return initial.capitalize()
        return initial

    def clean_surname(self):
        initial = self.cleaned_data['surname']
        if initial:
            return initial.capitalize()
        return initial

    def clean_artistic_name(self):
        initial = self.cleaned_data['artistic_name']
        if initial:
            return initial.capitalize()
        return initial

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        if initial and initial > date.today():
            raise ValidationError('Datum narození nesmí být v budoucnosti.')
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        if initial and initial > date.today():
            raise ValidationError('Datum úmrtí nesmí být v budoucnosti.')
        return initial

    def clean_biography(self):
        initial = self.cleaned_data['biography']
        sentences = re.sub(f'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        error_message = ''
        initial_surname = cleaned_data.get('surname')
        initial_artistic_name = cleaned_data.get('artistic_name')
        if not initial_surname and not initial_artistic_name:
            error_message += 'Je nutné zadat příjmení nebo umělecké jméno (nebo obojí).'
            #raise ValidationError('Je nutné zadat příjmení nebo umělecké jméno (nebo obojí).')

        initial_date_of_birth = cleaned_data.get('date_of_birth')
        initial_date_of_death = cleaned_data.get('date_of_death')
        if initial_date_of_birth and initial_date_of_death and initial_date_of_death <= initial_date_of_birth:
            error_message += ' Datum úmrtí nesmí být dřív, než datum narození.'
            #raise ValidationError('Datum úmrtí nesmí být dřív, než datum narození.')

        if error_message:
            raise ValidationError(error_message)

        return cleaned_data
