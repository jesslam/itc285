from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('getMembers/', views.getMembers, name = 'members'),
    path('gettreasurerreport/', views.getTreasurerReport, name = 'treasurerreport')
]