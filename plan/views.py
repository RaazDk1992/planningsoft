from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib.auth import authenticate,login

from .forms import FYform,YojanaRegForm,ProjectTypesForms,TypeOfProjectForm
from .models import FY, YojanaDetails

# Create your views here.

def adminDashBoard(request):
    
    return render(request,'pages\\admindashboard.html') 

def default(request):
    return render(request,'login\\index.html') 


def verification(request):

    if request.method == 'POST':
        userName = request.POST['userName']
        passWord = request.POST['passWord']
        user = authenticate(request, username=userName, password=passWord)
        
        if user is not None:
            login(request,user)
           # 
            return redirect('admindashboard')
        else:
            return redirect('default')

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



