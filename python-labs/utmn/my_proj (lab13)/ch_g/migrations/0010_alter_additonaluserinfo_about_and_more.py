# Generated by Django 4.1.3 on 2023-01-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch_g', '0009_alter_additonaluserinfo_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additonaluserinfo',
            name='about',
            field=models.TextField(verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='additonaluserinfo',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='additonaluserinfo',
            name='city',
            field=models.TextField(verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='additonaluserinfo',
            name='photo',
            field=models.TextField(verbose_name='Фотография'),
        ),
    ]