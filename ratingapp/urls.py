from django.urls import path,include
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home, name = 'home'),
    path('post/project/',views.post_project, name = 'post'),
]