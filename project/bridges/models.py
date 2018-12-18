from django.db import models
from django.urls import reverse
from datetime import datetime
from django import forms


#----------------------------------------------------------------------
#                        Main Model
#----------------------------------------------------------------------
class People(models.Model):

    email = models.EmailField(primary_key=True, max_length=70, blank=True, help_text="e.g. Student Email")
    # year = models.IntegerField(default=datetime.now().year, blank=True, help_text="e.g. 2020")
    name = models.CharField(max_length=60, blank=True, help_text="e.g. John Smith")
    phone = models.CharField(max_length=10, blank=True, help_text="e.g. 555-555-5555")
    school = models.CharField(max_length=100, blank=True, help_text="e.g. UMass Amherst")
    dob = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=100, blank=True, help_text="e.g. BS Computer Science")
    poc = models.CharField(max_length=50, blank=True, help_text="e.g. Yes/No")
    gender = models.CharField(max_length=60, blank=True, help_text="e.g. John Smith")
    role = models.CharField(max_length=100, blank=True, help_text="e.g. Tutor, Student, Teacher")
    fisrtgen = models.BooleanField(default=False)
    change_list_template = 'chart.html'

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Name: %s " %self.name


class Role(models.Model):
    role = models.CharField(max_length=60, blank=True, help_text="e.g. Volenteer")
    #person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Role name: %s " %self.role

#----------------------------------------------------------------------
#                             Events
#----------------------------------------------------------------------
class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, help_text="e.g. Party")
    site = models.CharField(max_length=60, blank=True, help_text="e.g. Caffeteria")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Event name: %s " %self.name

class EventAttendee(models.Model):
    people= models.ManyToManyField(People, blank=True)
    event = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Event name: %s " %self.name
