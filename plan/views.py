from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib.auth import authenticate,login
import requests
import logging
from .forms import DocForm, FYform, OfficeForm,YojanaRegForm,ProjectTypesForms,TypeOfProjectForm
from .models import FY, Office, YojanaDetails

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
    org_ref = Office.objects.all()
    if request.method == 'POST':
        uid = request.POST['signup_uid']
        firstname = request.POST['signup_first_name']
        lastname = request.POST['signup_last_name']
        mail = request.POST['signup_mail']
        phone = request.POST['signup_phone']
        org_ref = request.POST['org_ref_list']
        password = 'phone'
        user = User.objects.create_user(username = uid, first_name = firstname, last_name = lastname,password  = password, email = mail, is_active = False)
        user.profile.sanketNo = request.POST['signup_first_name']
        user.profile.contactNo = 'erererere'
        user.profile.is_active = True
       # user.save()
    return render(request,'pages\\adduser.html',{'org_ref':org_ref})


def addDoc(request):
    docForm = DocForm(initial={'doc_body':'<span></span>'})
    if request.POST:
        print("------------------------->")
        df = DocForm(request.POST)
        if df.is_valid:
            df.save()
        else:
            print("Error-----------------------")
    return render(request,'pages\\adoc.html',{'form':docForm})


        

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



