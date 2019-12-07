from django.shortcuts import render, get_object_or_404
from .models import Member, Unit, TreasurerReport

# Create your views here.

def index(request):
    return render(request, 'projectcoopapp/index.html')

def getmembers(request):
    coop_members = Member.objects.all()
    return render(request, 'projectcoopapp/members.html', {'coop_members': coop_members})

def getTreasurerReport(request):
    treasurer_rpt = TreasurerReport.objects.all()
    return render(request, 'projectcoopapp/treasurerreport.html', {'treasurer_rpt': treasurer_rpt}) 