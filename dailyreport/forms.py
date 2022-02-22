from django import forms
from dailyreport.models import CalEvent

class CalEventForm(forms.ModelForm):
    class Meta:
        model = CalEvent
        fields = '__all__'