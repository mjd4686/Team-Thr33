from django.db import models
from django.urls import reverse
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#----------------------------------------------------------------------
#                        Main Model
#----------------------------------------------------------------------
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    year = models.IntegerField(default=datetime.now().year, blank=True, help_text="e.g. 2020")
    phone = models.CharField(max_length=10, blank=True, help_text="e.g. 555-555-5555")
    school = models.CharField(max_length=100, blank=True, help_text="e.g. UMass Amherst")
    major = models.CharField(max_length=100, blank=True, help_text="e.g. BS Computer Science")
    poc = models.CharField(max_length=50, blank=True, help_text="e.g. Yes/No")
    gender = models.CharField(max_length=60, blank=True, help_text="e.g. John Smith")
    firstgen = models.CharField(max_length=10, blank=True)
    trans = models.CharField(max_length=50, blank=True, help_text="e.g. Yes")
    info = models.CharField(max_length=100, blank=True, help_text="e.g. Tutor, Student, Teacher")
    pronoun = models.CharField(max_length=20, blank=True, help_text="e.g. He/his, She/her...");
    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Name: %s " %self.name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
