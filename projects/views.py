from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    proj = Project.objects.all()
    context = {
        'projects' : proj,
    }
    return render(request, 'project_index.html', context)

def project_detail(request,pkey):
    proj = Project.objects.get(pk=pkey)
    context = {
        'project' : proj,
    }
    return render(request, 'project_detail.html', context)
    