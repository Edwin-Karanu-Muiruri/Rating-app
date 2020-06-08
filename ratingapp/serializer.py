from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','email')
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('profile','project_name','project_screenshot','project_description','project_url')
        