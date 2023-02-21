from django.contrib import admin
from .models import Author, Language, Genre, Print, Book, AdditonalUserInfo, Favourites

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fsl_name', 'birthday', 'deathday', 'short_info', 'published')
    list_display_links = ['fsl_name']
    search_fields = ['fsl_name']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'published')
    list_display_links = ['language']
    search_fields = ['language']


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', 'published')
    list_display_links = ['genre']
    search_fields = ['genre']


class PrintAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created', 'description', 'published')
    list_display_links = ['name']
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'year', 'print', 'isbn', 'published')
    filter_horizontal = ('authors', 'languages', 'genres')
    list_display_links = ['name']
    search_fields = ['name']


class AdditonalUserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'city', 'birthday', 'about', 'published')
    list_display_links = ['user']
    search_fields = ['user']


class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'books', 'published')
    list_display_links = ['user']
    search_fields = ('user', 'books')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Print, PrintAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(AdditonalUserInfo, AdditonalUserInfoAdmin)
admin.site.register(Favourites, FavouritesAdmin)
