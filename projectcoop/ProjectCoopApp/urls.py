from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('getmembers/', views.getmembers, name = 'members'),
    path('gettreasurerreport/', views.getTreasurerReport, name = 'treasurer_rpt')
]