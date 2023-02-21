from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    fsl_name = models.TextField('ФИО', blank=True, null=False, unique=True)
    birthday = models.DateField('Дата рождения', blank=True, null=False)
    deathday = models.DateField('Дата смерти', blank=True, null=False)
    short_info = models.TextField('Краткое описание', blank=True, null=False)
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['-published']

    def __str__(self):
        return self.fsl_name


class Language(models.Model):
    language = models.TextField('Язык, на котором написана книга', blank=True, null=False)
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['-published']

    def __str__(self):
        return self.language


class Genre(models.Model):
    genre = models.TextField('Жанр книг', blank=True, null=False)
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['-published']

    def __str__(self):
        return self.genre


class Print(models.Model):
    name = models.TextField('Название издательства', blank=True, null=False)
    city = models.TextField('Город издательства', blank=True, null=False)
    created = models.DateField('Дата создания', blank=True, null=False)
    description = models.TextField('Описание издательства', blank=True, null=False)
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['-published']

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.TextField('Название', blank=True, null=False)
    authors = models.ManyToManyField(Author, related_name='authors')
    languages = models.ManyToManyField(Language, related_name='languages')
    genres = models.ManyToManyField(Genre, related_name='genres')
    description = models.TextField('Описание книги', blank=True, null=False)
    year = models.DateField('Дата выпуска', blank=True, null=False)
    print = models.ForeignKey(Print, on_delete=models.DO_NOTHING)
    isbn = models.TextField('ISBN', blank=True, null=False, validators=[
        RegexValidator(
            r'^97[89][\s\-]?\d[\s\-]?(\d{4}[\s\-]?\d{4}|\d{2}[\s\-]?\d{6})[\s\-]?\d$',
            'Введите ISBN правильно'
        )
    ])
    dlcount = models.IntegerField('Кол-во скачиваний', blank=True, null=False, validators=[
        RegexValidator(
            r'^\d+$',
            'Количество скачиваний не может быть отрицательным'
        )
    ])
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-published']

    def __str__(self):
        return self.name


class AdditonalUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.TextField('Фотография')
    city = models.TextField('Город')
    birthday = models.DateField('Дата рождения')
    about = models.TextField('О себе')
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Доп. информация'
        verbose_name_plural = 'Доп. информация'
        ordering = ['-published']


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    published = models.DateTimeField('Добавлено в базу', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['-published']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class PrintForm(ModelForm):
    class Meta:
        model = Print
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


# Пушкин Александр Сергеевич
# 16.12.1820 (1820-12-16)
# 16.12.1920 (1920-12-16)
# Мудрейший из мудрейших. Создатель современного русского языка.
# Author.objects.create(fsl_name='Пушкин Александр Сергеевич', birthday='1820-12-16', deathday='1920-12-16', short_info='Мудрейший из мудрейших. Создатель современного русского языка.')

# Проза в стихах
# Genre.objects.create(genre='Проза в стихах')

# Арзамас
# Москва
# 16.12.1845 (1845-12-16)
# Созданное Пушкиным А. А. издательство, помогающее юным авторам и поэтам, при этом размещающее газеты с новостями.
# Print.objects.create(name='Арзамас', city='Москва', created='1845-12-16', description='Созданное Пушкиным А. А. издательство, помогающее юным авторам и поэтам, при этом размещающее газеты с новостями.')

# Русский
# Английский
# Французский
# Language.objects.bulk_create([Language(language=lang) for lang in ['Русский', 'Английский', 'Французский']])

# Евгений Онегин
# История одного Евгения о приключениях, войне, драме и политике.
# 16.12.1850 (1850-12-16)
# 978-0-12-345678-6
# 5
