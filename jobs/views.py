from django.shortcuts import render

from .models import Job
import os
cwd = os.getcwd()
base_dir = os.path.dirname(cwd)

def home(request):
    jobs = Job.objects
    im = '\media\images\sr40.jpg'
    return render(request, 'jobs/home.html', {'jobs': jobs, 'image': im})