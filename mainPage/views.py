from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')


def python_projects(request):
    return render(request, 'python_projects.html')
