from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
        {
        'id':'1',
        'title':"Ecommerce Website",
        'description':'Fully functional Ecommerce website'
        },
        {
        'id':'2',
        'title':"Portfolio Website",
        'description':'Project for my portfolio'        
        },
        {
        'id':'3',
        'title':"Social Network",
        'description':'awesome project I am working on'          
        },
]

def projects(request):
        page = 'projects'
        number = 10
        context = {'page': page, 'number': number, 'projects': projectsList}
        return render(request, 'projects/projects.html', context)
    
def project(request, pk):
        projectOBJ = None
        for i in projectsList:
                if i ['id'] == pk:
                        projectObj = i
        return render(request, 'projects/single-project.html', {'project':projectObj})
