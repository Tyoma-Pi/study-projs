# Generated by Django 4.1.3 on 2022-12-18 22:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ch_g', '0004_alter_additonaluserinfo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='additonaluserinfo',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата рождения'),
            preserve_default=False,
        ),
    ]
