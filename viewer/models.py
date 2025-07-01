from django.db.models import Model, CharField, DateField, ForeignKey, SET_NULL, \
    TextField, DateTimeField, ManyToManyField, IntegerField, ImageField, CASCADE

from accounts.models import Profile


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return self.name


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return self.name


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    artistic_name = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators')
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'name', 'artistic_name', 'date_of_birth']

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname}, artictic_name={self.artistic_name})"

    def __str__(self):
        if self.date_of_birth:
            return f"{self.name} {self.surname} ({self.date_of_birth.year})"
        return f"{self.name} {self.surname}"

    def full_name(self):
        full_name_ = ''
        if self.name:
            full_name_ += self.name + ' '
        if self.artistic_name:
            full_name_ += f'"{self.artistic_name}" '
        if self.surname:
            full_name_ += self.surname
        return full_name_


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False, unique=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    directors = ManyToManyField(Creator, blank=True, related_name='directing')
    actors = ManyToManyField(Creator, blank=True, related_name='acting')
    composers = ManyToManyField(Creator, blank=True, related_name='composing')
    length = IntegerField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    year = IntegerField(null=True, blank=True)
    countries = ManyToManyField(Country, blank=True, related_name='movies')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig', 'year']

    def __repr__(self):
        if self.year:
            return f"Movie(title_orig={self.title_orig}, year={self.year})"
        return f"Movie(title_orig={self.title_orig})"

    def __str__(self):
        if self.year:
            return f"{self.title_orig} ({self.year})"
        return f"{self.title_orig}"

    def length_format(self):
        # převod délky filmu z minut na formát h:mm
        # 142 min -> 2:22
        # 122 min -> 2:02
        if self.length:
            hours = self.length // 60
            minutes = self.length % 60
            return f"{hours}:{minutes:02}"
            #return f"{hours}h {minutes}min"
        return None


class Image(Model):
    image = ImageField(upload_to='images/', default=None, null=False, blank=False)
    movie = ForeignKey(Movie, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    creators = ManyToManyField(Creator, blank=True, related_name='images')
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return f"Image(image={self.image})"

    def __str__(self):
        return f"Image: {self.image}"


class Review(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE, null=False, blank=False, related_name='reviews')
    reviewer = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=False, related_name='reviews')
    rating = IntegerField(null=True, blank=True)
    comment = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __repr__(self):
        return (f"Review(movie={self.movie}, "
                f"reviewer={self.reviewer}, "
                f"rating={self.rating}, "
                f"comment={self.comment[:20]})")

    def __str__(self):
        return f"{self.reviewer}: {self.movie} ({self.rating})"
