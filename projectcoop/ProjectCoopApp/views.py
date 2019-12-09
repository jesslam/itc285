from django.shortcuts import render, get_object_or_404
from .models import Member, Unit, TreasurerReport

# Create your views here.

def index(request):
    return render(request, 'projectcoopapp/index.html')

def getMembers(request):
    members = Member.objects.all()
    return render(request, 'projectcoopapp/members.html', {'members': members})

def getTreasurerReport(request):
    treasurerreport = TreasurerReport.objects.all()
    return render(request, 'projectcoopapp/treasurerreport.html', {'treasurerreport': treasurerreport}) 