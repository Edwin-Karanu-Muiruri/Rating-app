# Generated by Django 3.0 on 2020-06-07 14:26

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratingapp', '0002_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_screenshot', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('project_description', models.TextField()),
                ('project_url', models.CharField(max_length=300)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingapp.Profile')),
            ],
        ),
    ]