from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from datetime import datetime
from django import forms
#from django.contrib.auth.models import User

#----------------------------------------------------------------------
#                        Survey Model
#----------------------------------------------------------------------
class Survey(models.Model):
    #link users to model:
    #user = models.ForeignKey(User,on_delete=models.CASCADE,)
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    BIRTH_MONTH_CHOICES = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    BIRTH_DATE_CHOICES = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23',
    '24','25','26','27','28','29','30','31')
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
    date = models.DateField(("Date"), default=datetime.today)


    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Participant name: %s" %self.name


#----------------------------------------------------------------------
#                             Final
#----------------------------------------------------------------------

class Affiliate(models.Model):
    #link users to model:
    #user = models.ForeignKey(User,on_delete=models.CASCADE,)
    email = models.EmailField(primary_key=True, max_length=70, blank=True, help_text="e.g. Student Email")
    name = models.CharField(max_length=60, blank=True, help_text="e.g. John Smith")
    phone = models.CharField(max_length=10, blank=True, help_text="e.g. 555-555-5555")
    school = models.CharField(max_length=100, blank=True, help_text="e.g. UMass Amherst")
    dob = models.DateField(null=True, blank=True)
    #Person of color
    poc = models.BooleanField(default=False)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Affiliate name: %s " %self.name

class Role(models.Model):
    role = models.CharField(max_length=60, blank=True, help_text="e.g. Volenteer")
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Role name: %s " %self.role

class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, help_text="e.g. Party")
    site = models.CharField(max_length=60, blank=True, help_text="e.g. Caffeteria")
    date = models.DateField(null=True, blank=True)
    tour = models.BooleanField(default=False)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Event name: %s " %self.name

class EventAttendee(models.Model):
    email = models.EmailField(primary_key=True, max_length=70, blank=True, help_text="e.g. Student Email")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Event name: %s " %self.name


class HSStudent(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    collegechoice = models.CharField(max_length=100, blank=True, help_text="e.g. UMass, Ucon")
    pemail = models.EmailField(max_length=70, blank=True, help_text="e.g. Parent Email")


    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "Student name: %s " %self.affiliate.name

class CollegeStudent(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    major = models.CharField(max_length=100, blank=True, help_text="e.g. BS Computer Science")
    major2 = models.CharField(max_length=100, blank=True, help_text="e.g. BA Math ")
    gradyear = models.DateField(null=True, blank=True)
    fisrtgen = models.BooleanField(default=False)
    degree = models.CharField(max_length=100, blank=True, help_text="e.g. MS Art ")
    job = models.CharField(max_length=100, blank=True, help_text="e.g. Tutor at Umass ")
    endofyear = models.DateField(null=True, blank=True)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return "College student name: %s " %self.affiliate.name

class SaleSummary(Survey):
    class Meta:
        proxy = True
        verbose_name = "Sale Summary"
        verbose_name_plural = "Sales Summary"