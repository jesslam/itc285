from django.shortcuts import render, get_object_or_404
from .models import Members, Units, TreasurerReports, meetingMinutes, Meetings

# Create your views here.

def index(request):
    return render(request, 'projectcoopapp/index.html')

def getMembers(request):
    members = Members.objects.all()
    return render(request, 'projectcoopapp/members.html', {'members': members})

def getTreasurerReport(request):
    treasurerreport = TreasurerReports.objects.all()
    return render(request, 'projectcoopapp/treasurerreport.html', {'treasurerreports': treasurerreports}) 

def getMeetingMinutes(request):
    meetingminutes = meetingMinutes.objects.all()
    return render(request, 'projectcoop/meetingminutes.html', {'meetingminutes': meetingminutes})