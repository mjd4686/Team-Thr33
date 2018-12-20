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

    year = models.IntegerField(default=datetime.now().year, null=True, blank=True, help_text="e.g. 2020")
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
        return "Name: %s " %self.user

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Survey(models.Model):
    reference = models.CharField(max_length=150, blank=True, null=True)
    prior_attendee = models.BooleanField(default=False, blank=True, null=True)
    suggestion = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    event_name = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Survey name: %s " %self.role

