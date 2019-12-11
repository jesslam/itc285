from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('members/', views.getMembers, name = 'members'),
    path('treasurerreport/', views.getTreasurerReport, name = 'treasurerreport'),
    path('newmeetingminutes/', views.newMeetingMinutes, name = 'newmeetingminutes'),
    path('coopdef/', views.getCoopDef, name = 'coopdef')
]