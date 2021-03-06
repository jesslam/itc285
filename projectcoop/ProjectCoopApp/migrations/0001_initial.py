# Generated by Django 3.0 on 2019-12-10 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MeetingID', models.IntegerField()),
                ('MeetingType', models.CharField(choices=[('BD', 'Board Meeting'), ('GA', 'General Assembly Meeting'), ('CO', 'Committee Meeting'), ('EM', 'Emergency Meeting')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meetings',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OwnerCheck', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'members',
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnitID', models.IntegerField()),
                ('UnitNum', models.CharField(max_length=5)),
                ('MemberID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ProjectCoopApp.Members')),
            ],
            options={
                'verbose_name_plural': 'units',
                'db_table': 'units',
            },
        ),
        migrations.CreateModel(
            name='TreasurerReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TreasurerRptID', models.IntegerField()),
                ('ReportDate', models.DateField()),
                ('CheckingBal', models.FloatField()),
                ('SavingsBal', models.FloatField()),
                ('UnitDuesBal', models.FloatField()),
                ('TreasurerNotes', models.TextField(blank=True, null=True)),
                ('UnitID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ProjectCoopApp.Units')),
            ],
            options={
                'verbose_name_plural': 'treasurerreports',
                'db_table': 'treasurerreports',
            },
        ),
        migrations.CreateModel(
            name='meetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MeetingMinID', models.IntegerField()),
                ('MeetingDate', models.DateField()),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
                ('MeetingMinutesText', models.TextField(blank=True, null=True)),
                ('TreasurerReportID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ProjectCoopApp.TreasurerReports')),
            ],
            options={
                'verbose_name_plural': 'meetingminutes',
                'db_table': 'meetingminutes',
            },
        ),
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MeetingID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ProjectCoopApp.Meetings')),
                ('MemberID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ProjectCoopApp.Members')),
            ],
            options={
                'verbose_name_plural': 'attendees',
                'db_table': 'attendees',
            },
        ),
    ]
