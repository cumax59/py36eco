from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# Max: A class is like a database table
# Max: After changes on models.py need makemigration again

class ecoProject(models.Model):
    PRIORITY_CHOICES = (    # verbose_name='專案級別'
        (0, 'Highest'),
        (1, 'Important'),
        (2, 'Normal'),
    )
    CATEGORY_CHOICES = (    # verbose_name='專案類別'
        (0, '年度計畫'),
        (1, '人力精實'),
        (2, '測試自動化'),
        (3, '設備備品'),
        (4, '耗材降低'),
        (5, '包材管控'),
        (6, 'Attrition降低'),
        (7, '製程改善'),
        (8, '效率提升'),
        (9, 'UPH提升'),
        (10, '品質提升'),
        (11, '自動化提升'),
        (12, '報表E化'),
        (13, '節能減排'),
        (14, '工程機電'),
        (15, '其他'),
    )
    STATUS_CHOICES = (      # verbose_name='專案狀態'
        (0, 'Ongoing'),
        (1, 'Pending'),
        (2, 'Closed'),
        (3, 'Cancel'),
    )
    CURRENT_STAGE_CHOICES = (    # verbose_name='專案開展階段'
        (0, '立案中'),
        (1, '需求分析'), 
        (2, '待排配開發'), 
        (3, '開發中'), 
        (4, '驗證中'), 
        (5, '已上線'), 
        (6, '取消'),   
    )
    DPBG_SITE_CHOICES = (    # verbose_name='廠區'
        (0, 'ALL'),
        (1, 'GL'),
        (2, 'ZZ PE1'),
        (3, 'ZZ PE2'),
        (4, 'ZZ SUR'),
        (5, 'TY'),
        (6, 'BZ'),
        (7, 'TN'),
    )
    PE_DEPARTMENT_CHOICES = (   # verbose_name='部門'
        (0, 'ALL'),
        (1, 'SFA'),
        (2, 'IE'),
        (3, 'AAE'),
        (4, 'AE'),
        (5, 'ME'),
        (6, 'AP'),
        (7, 'RF'),
        (8, 'Asset'),
        (9, 'PDCA'),
        (10, 'MEDD'),
        (11, 'CSA'),
        (12, 'Support'),
    )
    prj_id = models.AutoField(primary_key=True)
    prj_name = models.CharField(max_length=60, verbose_name='專案名稱')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2, verbose_name='專案級別')
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0, verbose_name='專案類別')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='專案狀態')
    description = models.CharField(max_length=100, default='', verbose_name='專案描述')
    current_stage = models.IntegerField(choices=CURRENT_STAGE_CHOICES, default=0, verbose_name='專案開展階段')
    # Future: follow category type, should have accordingly project stage
    create_date = models.DateField(auto_now_add=True, blank=False, verbose_name='立案日期')
    start_date = models.DateField(null=False, blank=True, default="", verbose_name='開始日期')
    end_date = models.DateField(null=False, blank=True, default="", verbose_name='預計完成日期')
    close_date = models.DateField(null=True, blank=True, default="", verbose_name='結案日期')
    dpbg_site = models.IntegerField(choices=DPBG_SITE_CHOICES, default=0, verbose_name='廠區')
    pe_department = models.IntegerField(choices=PE_DEPARTMENT_CHOICES, default=0, verbose_name='部門')
    prj_creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    updates = models.PositiveBigIntegerField(blank=False, default=0)
    # Future: 部門以另一個db table建立，專案類別也許也要

    def __str__(self):
        return self.prj_name

#  A List for storage of update messages. Message Queue for both  project and task usage
class UpdatesQueue(models.Model):
    update_id = models.AutoField(primary_key=True)
    parent = models.PositiveBigIntegerField(null=True, blank=True)
    content = models.TextField(max_length=240, default="", verbose_name='Status Updates')
    updatetime = models.DateTimeField(auto_now_add=True, blank=False)
    # editor = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='', verbose_name='作者')
    # next = models.PositiveBigIntegerField(null=True, blank=True)

    def __int__(self):
        return self.parent


