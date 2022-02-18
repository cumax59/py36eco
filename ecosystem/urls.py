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
from dailyreport.views import sayhello
from pjm import views
# hello3, listone, listall

urlpatterns = [
    path('admin/', admin.site.urls), 
    # will run admin.site.urls this function, so need import admin
    path('', views.starterpage),
    path('hello3/', views.hello3),
    path('dashboardview/', views.dashboardview),
    path('calendar/', views.calendarview),
    path('projects/', views.projectview),
    path('createproject/', views.createproject),
    path('editproject/', views.editproject),
    path('testpasspara/', views.testpasspara),
    path('post/', views.post),
    path('calendar/createEvent/', views.createEvent),
    path('sayhello/', sayhello),
    path('jsonview/', views.jsonview),
    path('singlecard/', views.singlecard),
]
