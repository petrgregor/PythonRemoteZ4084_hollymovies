from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Genre, Country, Creator, Movie, Image


class MovieAdmin(ModelAdmin):

    # ListView
    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    list_display = ['id', 'title_orig', 'title_cz', 'year']
    list_display_links = ['id', 'title_orig', 'title_cz']
    ordering = ['title_cz']
    list_per_page = 10
    list_filter = ['genres', 'countries']
    search_fields = ['title_orig', 'title_cz']
    actions = ['cleanup_description']

    # FormView
    fieldsets = [
        ('Titles',
         {
             'fields': [
                 'title_orig',
                 'title_cz'
             ],
             'description': 'Zde jsou názvy filmu (originální a český).'
         }),
        ('External information',
         {
             'fields': [
                 'genres',
                 'countries',
                 'year',
                 'length'
             ]
         }),
        ('Creators',
         {
             'fields': [
                 'directors',
                 'actors',
                 'composers'
             ]
         }),
        ('Internal information',
         {
             'fields': [
                 'description',
                 'created',
                 'updated'
             ]
         })
    ]
    readonly_fields = ['created', 'updated']


admin.site.register(Country)
admin.site.register(Creator)
admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Movie, MovieAdmin)
