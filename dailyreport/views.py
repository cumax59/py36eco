from django.shortcuts import render
import json
import re

# Create your views here.
from django.http import HttpResponse
from datetime import datetime, timedelta
from pjm.models import ecoProject
from dailyreport.models import CalEvent
# from dailyreport.forms import CalEventForm
from django.contrib.auth import get_user_model

User = get_user_model()

def sayhello(request):
    now = datetime.now()
    return render(request, "dashboardview.html", locals())

def calendarview(request):
    ret = dict()
    my_report_all = CalEvent.objects.all()
    ret['my_report_all'] = my_report_all
    return render(request, 'calendarview.html', ret)

def createEvent(request):
    today = datetime.now()
    ret = dict()
    category_all = [{'key': i[0], 'value': i[1]} for i in CalEvent.cat_choices]
    user_all = User.objects.exclude(username__in=['admin', request.user.username])
    ret['category_all'] = category_all
    ret['user_all'] = user_all
    if 'calDate' in request.GET and request.GET['calDate']:
        calDate = re.split('[-: ]', request.GET['calDate'])
        Y, M, D, h, m = map(int, calDate)
        start_time = datetime(Y, M, D, h, m)
        end_time = start_time + timedelta(hours=1)
        ret['start_time'] = start_time
        ret['end_time'] = end_time
        ret['today'] = today
    if request.method == "POST":
        # res = dict(result=False)
        ret = request.POST
        unit = CalEvent()
        unit.category = ret['eCategory']
        unit.content = ret['eventContent']
        unit.user = user_all[1]
        unit.start_time = ret['start_time']
        unit.end_time = ret['end_time']
        print(unit.start_time)
        unit.save()
        my_report_all = CalEvent.objects.all()
        new_return = dict()
        # create a new dict. ret instance is immutable
        new_return['my_report_all'] = my_report_all
        return render(request, 'calendarview.html', new_return)
    return render(request, 'createevent.html', ret)
