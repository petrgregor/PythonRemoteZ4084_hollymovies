from django.forms import Form, CharField


class GenreForm(Form):
    name = CharField(label='Název žánru', max_length=32, required=True)

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()
