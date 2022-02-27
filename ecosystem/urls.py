"""ecosystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dailyreport.views import sayhello, calendarview, createEvent
from pjm import views
# hello3, listone, listall

urlpatterns = [
    path('admin/', admin.site.urls), 
    # will run admin.site.urls this function, so need import admin
    path('hello3/', views.hello3),
    path('', views.starterpage),
    path('projects/', views.projectview),
    path('singlecardview/<str:index>', views.singlecardview),  
    path('dashboardview/', views.dashboardview),
    path('createproject/', views.createproject),
    path('editproject/', views.editproject),
    path('cardprojectview/', views.cardprojectview),
    path('ganttview/', views.ganttview),
    path('jsonview/', views.jsonview),
    path('addupdates/', views.addupdates),
    path('post/', views.post),
    path('sayhello/', sayhello),
    path('calendar/', calendarview), 
    path('calendar/create/', createEvent),
]
