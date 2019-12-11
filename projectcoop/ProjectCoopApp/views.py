from django.shortcuts import render, get_object_or_404
from .models import Members, Units, TreasurerReports, meetingMinutes, Meetings
from .forms import meetingMinutesForm, TreasurerReportsForm

# Create your views here.

def index(request):
    return render(request, 'projectcoopapp/index.html')

def getMembers(request):
    members = Members.objects.all()
    return render(request, 'projectcoopapp/members.html', {'members': members})

def getTreasurerReport(request):
    treasurerreport = TreasurerReports.objects.all()
    return render(request, 'projectcoopapp/treasurerreport.html', {'treasurerreport': treasurerreport}) 

def getMeetingMinutes(request):
    meetingminutes = meetingMinutes.objects.all()
    return render(request, 'projectcoop/meetingminutes.html', {'meetingminutes': meetingminutes})

def newMeetingMinutes(request):
    form = meetingMinutesForm
    if request.method=='POST':
        form=meetingMinutesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=meetingMinutesForm()
    else: 
        form=meetingMinutesForm()

    return render(request, 'projectcoopapp/newmeetingminutes.html', {'form':form})

def getCoopDef(request):
    # coopdef = coopdef.objects.all()
    return render(request, 'projectcoopapp/coopdef.html')
