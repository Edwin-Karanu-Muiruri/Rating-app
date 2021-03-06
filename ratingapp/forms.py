from django.forms import ModelForm
from .models import Project,Profile
from django import forms

class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','content_rating','design_rating','usability_rating','average_content_rating','average_design_rating','average_usability_rating','average_rating','voters']

class RateProjectForm(forms.Form):
    content = forms.IntegerField(min_value = 1, max_value = 10)
    design = forms.IntegerField(min_value = 1, max_value = 10)
    usability = forms.IntegerField(min_value = 1, max_value = 10)

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']