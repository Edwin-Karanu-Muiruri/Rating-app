# Generated by Django 3.0 on 2020-06-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]