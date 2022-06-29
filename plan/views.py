from django.shortcuts import render
from .forms import FYform,YojanaRegForm
from .models import FY, YojanaDetails
# Create your views here.
def default(request):
    return render(request,'login\\index.html') 

    
def registerPlan(request):
    form  = YojanaRegForm()
    return render (request,'pages\\registerplan.html',{'form':form})