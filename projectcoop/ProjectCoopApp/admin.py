from django.contrib import admin
from .models import Member, Unit, TreasurerReport, MeetingMinutes, Meeting

# Register your models here.

admin.site.register(Member)
admin.site.register(Unit)
admin.site.register(TreasurerReport)
admin.site.register(MeetingMinutes)
admin.site.register(Meeting)
