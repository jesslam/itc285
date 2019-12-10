from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('members/', views.getMembers, name = 'members'),
    path('treasurerreport/', views.getTreasurerReport, name = 'treasurerreport'),
    path('meetingminutes/', views.getMeetingMinutes, name = 'meetingminutes')
]