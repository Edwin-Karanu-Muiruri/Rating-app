# Generated by Django 3.0 on 2020-06-08 20:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratingapp', '0011_auto_20200608_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='voters',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
