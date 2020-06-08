from django.shortcuts import render,redirect
from .forms import ProjectUploadForm
from .models import Project,Profile,Rating
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
def home(request):
    projects = Project.display_all_projects()
    return render(request,'home.html',{"projects":projects})

def project(request):
    return render(request,'project.html')

def post_project(request):
    if request.method == "POST":
        form = ProjectUploadForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
        return redirect('home')
    else:
        form = ProjectUploadForm()
    return render(request,'postproject.html',{"form":form})

def profile(request):
    return render(request,'profile.html')

class ProfileList(APIView):
    def get(self,request,format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many = True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self,request,format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many = True)
        return Response(serializers.data)