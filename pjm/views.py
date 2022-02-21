from re import U
from django.shortcuts import render
import json
from django.core import serializers
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from pjm.forms import ProjectForm
from pjm.models import UpdatesQueue, ecoProject
from django.contrib.auth import get_user_model

user_model = get_user_model()
"""
def sayhello(request):
    return HttpResponse("Hello Django!")

def starterpage(request):
    now = datetime.now()
    return render(request, 'index.html', locals())
"""
def starterpage(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id') 
    return render(request, "projectview.html", locals())

def projectview(request):
    # projectview still take Django QuerySet to get all_projects info
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    return render(request, "projectview.html", locals())

def singlecardview(request, index):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    one_prj = all_ecoprojects[int(index)]
    prj_updates = UpdatesQueue.objects.filter(parent=one_prj.prj_id)    
    if request.method == "GET":
        print("Index been chosen: ", index)
        print("Prj Updates content: ", prj_updates)
        return render(request, "singlecardview.html", locals())
    if request.method == "POST":
        ret = request.POST
        update_content = ret['added2']
        working_id = one_prj.prj_id
        if len(update_content) > 3:    # too few words, reject to add 
            one_update = UpdatesQueue.objects.create(parent=working_id, content=update_content)
            one_update.save()
            one_prj = ecoProject.objects.get(prj_id=working_id)
            one_prj.updates = one_prj.updates + 1
            one_prj.save()
            all_ecoprojects = ecoProject.objects.all().order_by('prj_id') #sync records from database
            one_prj = all_ecoprojects[int(index)]
            prj_updates = UpdatesQueue.objects.filter(parent=working_id)
            print("update list:")
            print(prj_updates)   
        return render(request, "singlecardview.html", locals())

def cardprojectview(request):
    # this testing JSON data to pass all_project info
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

def addupdates(request):
    all_ecoprojects = ecoProject.objects.all().order_by('prj_id')
    # choices_dict['all_ecoprojects'] = all_ecoprojects 
    json_all_projects = serializers.serialize("json", all_ecoprojects)
    if request.method == "GET":
        return render(request, "addupdates.html", {'all_projects': json_all_projects})
    if request.method == "POST":
        ret = request.POST['added2']
        print("The update text is:")
        print(ret)
        ret.strip()
        print(ret)
        #update_content = ret['addupdates']
        #print(update_content)
    return render(request, "addupdates.html", {'all_projects': json_all_projects})

