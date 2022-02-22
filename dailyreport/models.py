from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# Max: A class is like a database table
# Max: After changes on models.py need makemigration again

class CalEvent(models.Model):
    cat_choices = ((0, 'Meeting'), (1, 'NPI'), (2, 'Task'))
    event_id = models.AutoField(primary_key=True)
    category = models.IntegerField(choices=cat_choices, default=0, verbose_name='Category')
    content = models.CharField(max_length=100, default='', verbose_name='工作描述')
    user = models.ForeignKey(User, related_name='report_user', on_delete=models.DO_NOTHING, default='')
    attention = models.ManyToManyField(User, related_name='attention', blank=True)
    start_time = models.DateTimeField(default='', verbose_name='開始時間')
    end_time = models.DateTimeField(default='', verbose_name='結束時間')
    add_time = models.DateField(auto_now_add=True, verbose_name="添加時間")

    def __int__(self):
        return self.event_id

    class Meta:
        verbose_name = '工作日報'
        verbose_name_plural = verbose_name
