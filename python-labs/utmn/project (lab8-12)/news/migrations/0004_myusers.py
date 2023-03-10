# Generated by Django 4.1.3 on 2022-12-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, verbose_name='Имя пользователя')),
                ('email', models.TextField(blank=True, verbose_name='Электронная почта')),
                ('password', models.TextField(blank=True, verbose_name='Пароль')),
                ('role', models.TextField(blank=True, verbose_name='Права доступа')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубиковано')),
            ],
        ),
    ]
