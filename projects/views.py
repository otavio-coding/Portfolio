from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Project

# Create your views here.

class IndexView(generic.ListView):

    template_name = "projects/index.html"
    context_object_name = "projects"

    def get_queryset(self):
        """Return a list of all projects"""
        return Project.objects.all()

class DetailView(generic.DetailView):

    model = Project
    template_name = "projects/detail.html"
