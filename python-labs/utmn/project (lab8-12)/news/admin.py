from django.contrib import admin
from .models import Article, Rubric, Hashtag, ArticleHashtag, MyUsers

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'annotation', 'image', 'rubnum', 'published')
    list_display_links = ['title']
    search_fields = ('title', 'keywords')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_display_links = ['name']
    search_fields = ['name']


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_display_links = ['name']
    search_fields = ['name']


class ArticleHashtagAdmin(admin.ModelAdmin):
    list_display = ('fk_id_art', 'fk_id_ht', 'published')
    list_display_links = ('fk_id_art', 'fk_id_ht')
    search_fields = ('fk_id_art', 'fk_id_ht')


# class MyUsersAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'password', 'role', 'published')
#     list_display_links = ['username']
#     search_fields = ('username', 'email')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(ArticleHashtag, ArticleHashtagAdmin)
