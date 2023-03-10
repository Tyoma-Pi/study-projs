# Generated by Django 4.1.3 on 2022-12-17 10:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsl_name', models.TextField(blank=True, unique=True, verbose_name='ФИО')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('deathday', models.DateField(blank=True, verbose_name='Дата смерти')),
                ('short_info', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.TextField(blank=True, verbose_name='Жанр книг')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.TextField(blank=True, verbose_name='Язык, на котором написана книга')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Название издательства')),
                ('city', models.TextField(blank=True, verbose_name='Город издательства')),
                ('created', models.DateField(blank=True, verbose_name='Дата создания')),
                ('description', models.TextField(blank=True, verbose_name='Описание издательства')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание книги')),
                ('year', models.DateField(blank=True, verbose_name='Год выпуска')),
                ('isbn', models.TextField(blank=True, validators=[django.core.validators.RegexValidator('^97[89][\\s\\-]?\\d[\\s\\-]?(\\d{4}[\\s\\-]?\\d{4}|\\d{2}[\\s\\-]?\\d{6})[\\s\\-]?\\d$')], verbose_name='ISBN')),
                ('dlcount', models.IntegerField(blank=True, verbose_name='Кол-во скачиваний')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
                ('authors', models.ManyToManyField(related_name='authors', to='ch_g.author')),
                ('genres', models.ManyToManyField(related_name='genres', to='ch_g.genre')),
                ('languages', models.ManyToManyField(related_name='languages', to='ch_g.language')),
                ('print', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ch_g.print')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-published'],
            },
        ),
    ]
