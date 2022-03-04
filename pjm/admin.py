from django.contrib import admin
from pjm.models import UpdatesQueue, ecoProject, Task, TaskUpdatesQueue

# Register your models here.
admin.site.register(ecoProject)
admin.site.register(UpdatesQueue)
admin.site.register(Task)
admin.site.register(TaskUpdatesQueue)