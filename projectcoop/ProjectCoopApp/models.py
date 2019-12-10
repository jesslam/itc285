from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Members(models.Model):
    MemberID = models.IntegerField(),
    FirstName = models.CharField
    LastName = models.CharField
    UnitNum = models.CharField
    OwnerCheck = models.BooleanField()

    def __str__(self):
        return self.firstname+ ' ' + self.lastname

    class Meta:
        db_table = 'members'
        verbose_name_plural = 'members'

class Units(models.Model):
    UnitID = models.IntegerField()
    UnitNum = models.CharField(max_length = 5)
    MemberID = models.ForeignKey(Members, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.unitnum

    class Meta:
        db_table = 'units'
        verbose_name_plural = 'units'

class TreasurerReports(models.Model):
    TreasurerRptID = models.IntegerField()
    ReportDate = models.DateField()
    CheckingBal = models.FloatField()
    SavingsBal = models.FloatField()
    UnitID = models.ForeignKey(Units, on_delete = models.DO_NOTHING)
    UnitDuesBal = models.FloatField()
    TreasurerNotes = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.treasurerreports

    class Meta:
        db_table = 'treasurerreports'
        verbose_name_plural = 'treasurerreports'

class Meetings(models.Model):
    MeetingID = models.IntegerField()
    BoardMtg = 'BD'
    GenMtg = 'GA'
    CommitteeMtg = 'CO'
    EmergMtg = 'EM'
    MeetingType_choices = [
        (BoardMtg, 'Board Meeting'),
        (GenMtg, 'General Assembly Meeting'),
        (CommitteeMtg, 'Committee Meeting'),
        (EmergMtg,'Emergency Meeting'),
    ]
    MeetingType = models.CharField(
        max_length = 2,
        choices = MeetingType_choices,
    )

    def __str__(self):
        return self.meetings

    class Meta:
        db_table = 'meetings'
        verbose_name_plural = 'meetings'
    
class meetingMinutes(models.Model):
    MeetingMinID = models.IntegerField()
    MeetingDate = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    MeetingMinutesText = models.TextField(null = True, blank = True)
    TreasurerReportID = models.ForeignKey(TreasurerReports, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.meetingminutes

    class Meta:
        db_table = 'meetingminutes'
        verbose_name_plural = 'meetingminutes'


class Attendees(models.Model):
    MemberID = models.ForeignKey(Members, on_delete = models.DO_NOTHING)
    MeetingID = models.ForeignKey(Meetings, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.attendees

    class Meta:
        db_table = 'attendees'
        verbose_name_plural = 'attendees'




