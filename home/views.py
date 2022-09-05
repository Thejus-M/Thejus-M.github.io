from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Project

class Home(TemplateView):
    template_name = "home/home.html"
    extra_context={}
    


class Skills(TemplateView):
    template_name = "home/skills.html"



class Projects(ListView):
    model = Project
    template_name = "home/projects.html"
    context_object_name='project'

