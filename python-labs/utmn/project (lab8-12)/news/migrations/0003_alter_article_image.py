# Generated by Django 4.1.3 on 2022-12-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.TextField(blank=True, verbose_name='Изображение'),
        ),
    ]
