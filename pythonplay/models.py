# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievements(models.Model):
    achievename = models.CharField(db_column='AchieveName', primary_key=True, max_length=255)  # Field name made lowercase.
    goal = models.CharField(max_length=255)
    reward = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'achievements'


class Achievementslist(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, AchieveName) found, that is not supported. The first column is selected.
    achievename = models.ForeignKey(Achievements, models.DO_NOTHING, db_column='AchieveName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'achievementslist'
        unique_together = (('userid', 'achievename'),)


class Taskcompletions(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase. The composite primary key (UserID, TaskID) found, that is not supported. The first column is selected.
    taskid = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='TaskID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taskcompletions'
        unique_together = (('userid', 'taskid'),)


class Tasks(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tasks'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    experience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
