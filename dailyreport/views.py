from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from pjm.models import ecoProject
from django.contrib.auth import get_user_model

user_model = get_user_model()

def sayhello(request):
    now = datetime.now()
    return render(request, "dashboardview.html", locals())
