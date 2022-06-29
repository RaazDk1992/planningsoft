from django.shortcuts import render
from .forms import FYform
from .models import FY
# Create your views here.
def default(request):
    return render(request,'login\\index.html') 

    
def registerPlan(request):
    form  = FYform()
    return render (request,'pages\\registerplan.html',{'form':form})