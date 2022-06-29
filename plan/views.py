from django.shortcuts import render
from .forms import FYform,YojanaRegForm,ProjectTypesForms,TypeOfProjectForm
from .models import FY, YojanaDetails
# Create your views here.
def default(request):
    return render(request,'login\\index.html') 

    
def registerPlan(request):
    form  = YojanaRegForm()
    return render (request,'pages\\registerplan.html',{'form':form})

def addFY(request):
    form = FYform()
    return render (request,'pages\\fymanagement.html',{'form':form})
def addProjectType(request):
    form = ProjectTypesForms()
    return render (request,'pages\\projecttype.html',{'form':form})
def addTypeOfProject(request):
    form  = TypeOfProjectForm()
    return render (request,'pages\\typeofProject.html',{'form':form})



