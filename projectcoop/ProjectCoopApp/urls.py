from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('members/', views.getmembers, name = 'members'),
    path('treasurerreport/', views.getTreasurerReport, name = 'treasurer_rpt')
]