# Generated by Django 4.1.3 on 2022-12-18 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ch_g', '0003_additonaluserinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additonaluserinfo',
            options={'ordering': ['-published'], 'verbose_name': 'Доп. информация', 'verbose_name_plural': 'Доп. информация'},
        ),
    ]
