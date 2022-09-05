from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name='home'),
    path("skills", views.Skills.as_view(), name='skills'),
    path("projects", views.Projects.as_view(), name='projects'),
]
