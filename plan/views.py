from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib.auth import authenticate,login
import requests
import logging
from .forms import FYform, OfficeForm,YojanaRegForm,ProjectTypesForms,TypeOfProjectForm
from .models import FY, YojanaDetails

# Create your views here.

def adminDashBoard(request):
    
    return render(request,'pages\\admindashboard.html') 

def default(request):
    """
    r = requests.get(
            "http://api.sparrowsms.com/v2/sms/",
            params={'token' : 'v2_hUlUgdGo3G5CnSXjGENwguXBbWQ.UGCu',
                  'from'  : 'LekbeshiMun',
                  'to'    : '9848288339',
                  'text'  : 'SMS Message to be sent'})

    status_code = r.status_code
    response = r.text 
    """

    return render(request,'login\\index.html',{'r':'apple'}) 


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

    
def registerPlan(request):
    form  = YojanaRegForm()
    return render (request,'pages\\registerplan.html',{'form':form})

def addFY(request):
    form = FYform()
    return render (request,'pages\\fymanagement.html',{'form':form})
    
def addStaff(request):
    return render(request,'pages\\adduser.html')

def addOffice(request):
      of = OfficeForm()
      if request.POST:
        oform = OfficeForm(request.POST)
        if oform.is_valid:
            oform.save()
      return render(request,'pages\\addoffice.html',{'form':of})        
def addProjectType(request):
        form = ProjectTypesForms()
        if request.POST:
           ptypef = ProjectTypesForms(request.POST)
           if ptypef.is_valid():
               ptypef.save()
        return render (request,'pages\\projecttype.html',{'form':form})
def addTypeOfProject(request):
    form  = TypeOfProjectForm()
    return render (request,'pages\\typeofProject.html',{'form':form})



