from django.shortcuts import render,redirect
from .forms import ProjectUploadForm,RateProjectForm,EditProfileForm
from .models import Project,Profile
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
def home(request):
    projects = Project.display_all_projects()
    project_ratings = Project.objects.all().order_by('-average_rating')
    highest_rating = project_ratings[0]
    return render(request,'home.html',{"projects":projects,"highest_rating":highest_rating})

def project(request):
    project = Project.objects.get(pk=id)
    voted = False
    if project.voters.filter(id=request.user.id).exists():
        voted = True

    return render(request,'project.html',{"project":project,"voted":voted})

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

def project_search(request):
    if "project" in request.GET and request.GET["project"]:
        searched_project = request.GET.get("project")
        projects = Project.search_project(searched_project)
        message =f"{searched_project}"
       
        
        return render(request, 'search.html', {"projects": projects,"message": message})
    else:
        message = "Please enter a project name to search"
        return render(request,'search.html', {"message": message}) 

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    projects = Project.get_user_projects(current_user)
    return render(request,'profile.html',{"profile":profile,"projects":projects})

def edit_profile(request):
    current_user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            bio  = form.cleaned_data['bio']
            profile_pic = form.cleaned_data['profile_pic']
            email  = form.cleaned_data['email']


            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.bio = bio
            updated_profile.profile_pic = profile_pic
            updated_profile.email = email
            updated_profile.save()
        return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request, 'edit_profile.html', {"form": form})


def add_voters(request,id):
    '''
    Adds voters' jury who have rated a project
    '''
    project = Project.objects.get(pk=id)
    voted = False
    if project.voters.filter(id=request.user.id).exists():
        voted = False
    else:
        project.voters.add(request.user)
        voted = False
    return HttpResponseRedirect(reverse('rate_project',args =[int(project.id)]))

def rate_project(request,id):
    '''
    Project rating function
    '''
    project = Project.objects.get(pk = id)
    if request.method == "POST":
        form = RateProjectForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']

            project.design_rating = project.design_rating + design
            project.usability_rating = project.usability_rating + usability
            project.content_rating = project.content_rating + content

            project.average_design_rating = project.design_rating/project.voters_count()
            project.average_usability_rating = project.usability_rating/project.voters_count()
            project.average_content_rating = project.content_rating/project.voters_count()

            project.average_rating = (project.average_content_rating + project.average_design_rating + project.average_usability_rating)/3

            project.save()
            return HttpResponseRedirect(reverse('project',args =[int(project.id)]))

    else:
        form = RateProjectForm()
    return render(request, 'rate_project.html', {"project":project, "form": form})

def project_details(request,id):
    '''
    Function to display project details
    '''
    project = Project.objects.get(pk = id)
    voted = False
    if project.voters.filter(id=request.user.id).exists():
        voted = True 
    
    return render(request, 'project.html', {"project":project, "voted": voted})

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