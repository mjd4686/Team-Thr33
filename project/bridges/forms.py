from django import forms
from datetime import datetime
#----------------------------------------------------------------------
#                         Users
#----------------------------------------------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), help_text="Required.")
    year = forms.IntegerField(help_text="Optional. e.g. 2020")
    phone = forms.CharField(max_length=10, help_text="Optional. e.g. 555-555-5555")
    school = forms.CharField(max_length=100, help_text="Optional. e.g. UMass Amherst")
    major = forms.CharField(max_length=100, help_text="Optional. e.g. BS Computer Science")
    pocchoices = ['Asian', 'Black/African', 'Hispanic/Latinx', 'Native American', 'Pacific Islander', 'White', 'Prefer not to answer']
    poc = forms.ChoiceField(choices=[(x, x) for x in pocchoices], required=True, help_text="Optional. I identify as ...")
    genders = ['Female', 'Male', 'Non-binary', 'Prefer not to answer']
    gender = forms.ChoiceField(choices=[(x, x) for x in genders], required=True, help_text="Optional. I identify as ...")
    fgchoices = ['Yes', 'No', 'Prefer not to answer']
    firstgen = forms.ChoiceField(choices=[(x, x) for x in fgchoices], required=True, help_text="Optional. Are you the first in your family to go to college?")
    pronoun = forms.CharField(max_length=20, help_text="Optional. e.g. He/his, She/her...")
    info = forms.CharField(max_length=100, help_text="Optional. e.g. Tutor, Student, Teacher")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', 'year', 'phone', 'school', 'major', 'gender', 'poc', 'firstgen', 'info')

