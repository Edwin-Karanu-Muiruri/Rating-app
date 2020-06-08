from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name = 'home'),
    path('post/project/',views.post_project, name = 'post'),
    path('profile/',views.profile, name = 'profile'),
    path('accounts/profile/',views.profile,name = 'account profile'),
    path('profile/edit/', views.edit_profile,name= 'edit_profile'),
    path('post/<int:id>', views.project_details, name = "project"),
    path('search/', views.project_search, name = "project_search"),
    path('project/rate/<int:id>', views.rate_project, name ="rate_project"),
    path('project/votes/<int:id>', views.add_voters, name ="add_voters"),
    path('api/profiles/',views.ProfileList.as_view()),
    path('api/projects/',views.ProjectList.as_view()),
]