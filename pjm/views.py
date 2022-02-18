from django.shortcuts import render
import json
from django.core import serializers
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from pjm.forms import ProjectForm
from pjm.models import ecoProject
from django.contrib.auth import get_user_model

user_model = get_user_model()
choices_dict = dict()

priority_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.PRIORITY_CHOICES]
category_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.CATEGORY_CHOICES]
status_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.STATUS_CHOICES]
stage_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.CURRENT_STAGE_CHOICES]
site_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.DPBG_SITE_CHOICES]
department_all = [{'key': i[0], 'value': i[1]} for i in ecoProject.PE_DEPARTMENT_CHOICES]
choices_dict['priority_all'] = priority_all
choices_dict['category_all'] = category_all
choices_dict['status_all'] = status_all
choices_dict['stage_all'] = stage_all
choices_dict['site_all'] = site_all
choices_dict['department_all'] = department_all

"""
def sayhello(request):
    return HttpResponse("Hello Django!")

def starterpage(request):
    now = datetime.now()
    return render(request, 'index.html', locals())
"""
def starterpage(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id') 
    print(all_ecoprojects)
    return render(request, "index.html", locals())

def testpasspara(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    # choices_dict['all_ecoprojects'] = all_ecoprojects 
    json_all_projects = serializers.serialize("json", all_ecoprojects)
    return render(request, "cardprojectview.html", {'all_projects': json_all_projects} )

def jsonview(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    # json_projects = serializers.serialize('json', all_ecoprojects)
    # print(json_projects) 
    # return HttpResponse(json_projects, content_type="application/json")
    # return render(request, "index.html", {'dict_name': json.dumps(json_projects)})
    return render(request, "index.html", locals())

def hello3(request):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def dashboardview(request):
    now = datetime.now()
    return render(request, "dashboardview.html", locals())

def calendarview(request):
    now = datetime.now()
    return render(request, "calendarview.html", locals())

def projectview(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    choices_dict['all_ecoprojects'] = all_ecoprojects 
    print(choices_dict)
    print("Category All")
    one_dict = choices_dict['category_all'][1]
    print(one_dict['value'])
    return render(request, "projectview.html", choices_dict)

def post(request):
    if request.method == "POST":
        mess = request.POST['prj_name']
        # print(mess)
    else:
        mess = "No message!"
    return render(request, "post.html", locals())

def createproject(request):
    ret = dict()
    today = datetime.now().strftime('%Y-%m-%d')
    user_all = user_model.objects.exclude(username__in=['admin', request.user.username])
    current_user = user_all[1]
    # print("username is")
    # print(user_all)
    # print(current_user)
    ret['user_all'] = user_all
    if request.method == "GET":
        return render(request, "createproject.html", choices_dict)
    if request.method == "POST":
        ret = request.POST
        unit = ecoProject()
        unit.prj_name = ret['cPrjName']
        unit.priority = ret['cPriority']
        unit.category = ret['cCategory']
        unit.status = 0  # use 0 when in project create
        unit.description = ret['cDescription']
        unit.current_stage = ret['cStage']
        # unit.create_date = ret['cCreateDate']
        unit.create_date = today # default today is the create day
        unit.start_date = ret['cStartDate']
        unit.end_date = ret['cEndDate']
        unit.close_date = ret['cEndDate'] # temporarily set same as end date
        unit.dpbg_site = ret['cSite']
        unit.pe_department = ret['cDepartment']
        # unit.prj_creator = user_all[1] # temp set to pjmuser
        unit.prj_creator = current_user
        unit.updates = 0 # default is set to no updates yet
        print(unit.create_date)
        unit.save()
        all_ecoprojects = ecoProject.objects.all().order_by('prj_id') 
    return render(request, "index.html", locals())

def editproject(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    a_project = all_ecoprojects[7]
    # choices_dict['all_ecoprojects'] = all_ecoprojects 
    print(a_project)
    return render(request, "editproject.html", locals())

def createEvent(request):
    return HttpResponse("Hello Django!")

def singlecard(request):
    return render(request, "singlecard.html")

