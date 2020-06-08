from django.shortcuts import render,redirect
from .forms import ProjectUploadForm
from .models import Project,Profile,Rating
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'home.html')

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