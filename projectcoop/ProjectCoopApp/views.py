from django.shortcuts import render, get_object_or_404
from .models import Member, Unit, TreasurerReport

# Create your views here.

def index(request):
    return render(request, 'ProjectCoop/index.html')

def getmembers(request):
    coop_members = Member.objects.all()
    return render('ProjectCoop/members.html', {'coop_members': coop_members})
