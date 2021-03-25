from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Profile, Project
from django.http import HttpResponse
"""
Add class based views
"""


def main(request):

    profile_1 = Profile()
    profile_1.name = 'Jason Tyson'
    profile_1.job = 'Backend Developer'

    return render(request, 'templates/main.html', {'profile_1': profile_1})


def python_projects(request):

    py_project_1 = Project()
    py_project_1.name = "Automated Reports"
    py_project_1.client = "Massachusetts General Hospital"
    py_project_1.icon = "medical document.svg"
    py_project_1.desc = ""
    py_project_1.gallery = "xs_Morg_Blood.jpg"

    py_project_2 = Project()
    py_project_2.name = "Productivity Dashboard"
    py_project_2.client = "Massachusetts General Hospital"
    py_project_2.icon = "medical hospital.svg"
    py_project_2.desc = ""
    py_project_2.gallery = ""

    py_project_3 = Project()
    py_project_3.name = "Timekeeping Dashboard"
    py_project_3.client = "Self"
    py_project_3.icon = "medical hospital.svg"
    py_project_3.desc = ""
    py_project_3.gallery = ""

    py_project_4 = Project()
    py_project_4.name = "Misc"
    py_project_4.client = "Self"
    py_project_4.icon = ""
    py_project_4.desc = ""
    py_project_4.gallery = ""

    py_project_5 = Project()
    py_project_5.name = "Game Liberation"
    py_project_5.client = "Self"
    py_project_5.icon = ""
    py_project_5.desc = ""
    py_project_5.gallery = ""

    py_project_6 = Project()
    py_project_6.name = "Portfolio"
    py_project_6.client = "Self"
    py_project_6.icon = ""
    py_project_6.desc = ""
    py_project_6.gallery = ""

    py_projects = [py_project_1, py_project_2, py_project_3]

    return render(request, 'templates/python_projects.html', {"py_projects": py_projects})
