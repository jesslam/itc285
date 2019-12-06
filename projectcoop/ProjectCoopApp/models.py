from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    MemberID = models.IntegerField,
    FirstName = models.CharField(max_length = 50),
    LastName = models.CharField(max_length = 50),
    UnitNum = models.CharField(max_length = 5),
    Owner = models.boolean(null=False)

    def __str__(self):
        return self.members

    class Meta:
        db_table = 'member'
        verbose_name_plural = 'members'

class Unit(models.Model):
    UnitID = models.IntegerField,
    UnitNum = models.CharField(max_length = 5),
    MemberID = models.ForeignKey(Member, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.units

    class Meta:
        db_table = 'unit'
        verbose_name_plural = 'units'

class TreasurerReport(models.Model):
    TreasurerRptID = models.IntegerField,
    CheckingBal = models.float,
    SavingsBal = models.float,
    UnitID = models.ForeignKey(Unit, on_delete = models.DO_NOTHING)
    UnitDuesBal = models.float,
    TreasurerNotes = models.text

    def __str__(self):
        return self.treasurerreport

    class Meta:
        db_table = 'treasurerreport'
        verbose_name_plural = 'treasurerreports'



