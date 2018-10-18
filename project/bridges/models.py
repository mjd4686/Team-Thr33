from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#from django.contrib.auth.models import User

#----------------------------------------------------------------------
#                        Survey Model
#----------------------------------------------------------------------
class Survey(models.Model):
    #link users to model:
    #user = models.ForeignKey(User,on_delete=models.CASCADE,)

    #Preliminary
    name = models.CharField(max_length=200, blank =True ,help_text="e.g. John Smith")
    year = models.CharField(max_length=200, null=True, blank=True, help_text="What school year")
    dob= models.DateField(null=True, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Participant name: %s" %self.name
