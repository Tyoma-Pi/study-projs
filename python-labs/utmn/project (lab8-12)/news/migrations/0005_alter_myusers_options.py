# Generated by Django 4.1.3 on 2022-12-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_myusers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myusers',
            options={'ordering': ['-published'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
