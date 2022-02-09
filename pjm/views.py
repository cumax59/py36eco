from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from pjm.models import ecoProject

"""
def sayhello(request):
    return HttpResponse("Hello Django!")

def starterpage(request):
    now = datetime.now()
    return render(request, 'index.html', locals())
"""
def starterpage(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id') 
    return render(request, "index.html", locals())

def hello3(request):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def listone(request):
    try:
        unit = ecoProject.objects.get(prj_id=4)     # read only 1 record
    except:
        errormessage = "(Read Error!)"
    return render(request, "listone.html", locals())

def listall(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id') 
    return render(request, "listall.html", locals())