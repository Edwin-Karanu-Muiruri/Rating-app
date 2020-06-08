from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name = 'home'),
    path('post/project/',views.post_project, name = 'post'),
    path('profile/',views.profile, name = 'profile'),
    path('accounts/profile/',views.profile,name = 'account profile'),
    path('api/profile/',views.Profile.as_view()),
    path('api/project/',views.Project.as_view())
]