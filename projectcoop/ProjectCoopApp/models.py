from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    MemberID = models.IntegerField(),
    FirstName = models.CharField
    LastName = models.CharField
    UnitNum = models.CharField
    OwnerCheck = models.BooleanField()

    def __str__(self):
        return self.firstname+ ' ' + self.lastname

    class Meta:
        db_table = 'member'
        verbose_name_plural = 'members'

class Unit(models.Model):
    UnitID = models.IntegerField()
    UnitNum = models.CharField(max_length = 5)
    MemberID = models.ForeignKey(Member, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.unitnum

    class Meta:
        db_table = 'unit'
        verbose_name_plural = 'units'

class TreasurerReport(models.Model):
    TreasurerRptID = models.IntegerField()
    ReportDate = models.DateField()
    CheckingBal = models.FloatField()
    SavingsBal = models.FloatField()
    UnitID = models.ForeignKey(Unit, on_delete = models.DO_NOTHING)
    UnitDuesBal = models.FloatField()
    TreasurerNotes = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.treasurerreport

    class Meta:
        db_table = 'treasurerreport'
        verbose_name_plural = 'treasurerreports'

class Meeting(models.Model):
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
        return self.meeting

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'
    
class MeetingMinutes(models.Model):
    MeetingMinID = models.IntegerField()
    MeetingDate = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    MeetingMinutesText = models.TextField(null = True, blank = True)
    TreasurerReportID = models.ForeignKey(TreasurerReport, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.meetingminutes

    class Meta:
        db_table = 'meetingminutes'
        verbose_name_plural = 'meetingminutes'


class Attendee(models.Model):
    MemberID = models.ForeignKey(Member, on_delete = models.DO_NOTHING)
    MeetingID = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.attendees

    class Meta:
        db_table = 'attendee'
        verbose_name_plural = 'attendees'




