from django.shortcuts import render

# Create your views here.
def default(request):
    return render(request,'login\\index.html') 

    
def registerPlan(request):
    return render (request,'pages\\registerplan.html')