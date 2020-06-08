from django.forms import ModelForm
from .models import Project

class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','ratings']