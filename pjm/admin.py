from django.contrib import admin
from pjm.models import UpdatesQueue, ecoProject

# Register your models here.
admin.site.register(ecoProject)
admin.site.register(UpdatesQueue)