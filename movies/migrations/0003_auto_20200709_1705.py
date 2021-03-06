# Generated by Django 3.0.8 on 2020-07-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200709_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='film_director', to='movies.Actor', verbose_name='режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Актер'),
        ),
    ]
