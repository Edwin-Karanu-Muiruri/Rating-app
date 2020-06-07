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