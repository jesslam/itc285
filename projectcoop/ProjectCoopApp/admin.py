from django.contrib import admin
from .models import Members, Units, TreasurerReports, meetingMinutes, Meetings

# Register your models here.

admin.site.register(Members)
admin.site.register(Units)
admin.site.register(TreasurerReports)
admin.site.register(meetingMinutes)
admin.site.register(Meetings)
