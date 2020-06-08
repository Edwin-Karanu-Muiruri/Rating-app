from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    '''
    Profile class for users
    '''
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.CharField(max_length = 255)
    email = models.EmailField()

    def __str__(self):
        return self.user.username 

    @receiver(post_save, sender = User)
    def create_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile( sender, instance, **kwargs):
        instance.profile.save()

class Rating(models.Model):
    '''
    Ratings class for rating of projects
    '''
    content_rating = models.IntegerField()
    design_rating = models.IntegerField()
    usability_rating = models.IntegerField()
    overall_rating = models.IntegerField()

class Project(models.Model):
    '''
    Projects class to define the project outlook
    '''
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    project_name = models.CharField(max_length = 100)
    project_screenshot = CloudinaryField('image')
    project_description = models.TextField()
    project_url = models.CharField(max_length = 300)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod 
    def search_project(cls,name):
        return Project.objects.filter(title__icontains = name)

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)