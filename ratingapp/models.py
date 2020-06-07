from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    '''
    Profile class for users
    '''
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.CharField(max_length = 255)
    email = models.EmailField( default = None)

class Project(models.Model):
    '''
    Projects class to define the project outlook
    '''
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    project_name = models.CharField(max_length = 100)
    project_screenshot = CloudinaryField('image')
    project_description = models.TextField()
    project_url = models.CharField(max_length = 300)

class Rating(models.Model):
    '''
    Ratings class for rating of projects
    '''
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    content_rating = models.IntegerField()
    design_rating = models.IntegerField()
    usability_rating = models.IntegerField()
    overall_rating = models.IntegerField()