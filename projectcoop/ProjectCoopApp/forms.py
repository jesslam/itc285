from django import forms
from .models import Members, Units, TreasurerReports, meetingMinutes, Meetings

class meetingMinutesForm(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = '__all__'

class TreasurerReportsForm(forms.ModelForm):
    class Meta:
        model = TreasurerReports
        fields = '__all__'