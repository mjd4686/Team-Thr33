from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from datetime import datetime
#from django.contrib.auth.models import User

#----------------------------------------------------------------------
#                        Survey Model
#----------------------------------------------------------------------
class Survey(models.Model):
    #link users to model:
    #user = models.ForeignKey(User,on_delete=models.CASCADE,)

    #Preliminary
    name = models.CharField(max_length=60, blank=True, help_text="e.g. John Smith")
    email = models.EmailField(max_length=70, blank=True, help_text="e.g. Student Email")
    phone = models.CharField(max_length=10, blank=True, help_text="e.g. 555-555-5555")
    year = models.IntegerField(default=datetime.now().year, blank=True, help_text="e.g. 2020")    
    pronoun = models.CharField(max_length=20, null=True, blank=True, help_text="e.g Him/his/he")    
    dob = models.DateField(null=True, blank=True)
    color = models.BooleanField(default=False)
    firstgen = models.BooleanField(default=False)
    workstudy = models.BooleanField(default=False)
    major = models.CharField(max_length=50, blank =True ,help_text="e.g. Comp Sci")

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Participant name: %s" %self.name
