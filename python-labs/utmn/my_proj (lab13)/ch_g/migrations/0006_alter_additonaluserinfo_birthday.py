# Generated by Django 4.1.3 on 2022-12-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch_g', '0005_additonaluserinfo_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additonaluserinfo',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
