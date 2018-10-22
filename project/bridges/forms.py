from django import forms
from datetime import datetime
#----------------------------------------------------------------------
#                         Form
#----------------------------------------------------------------------
from .models import Survey

class SurveyForm(forms.ModelForm): 
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    name = forms.CharField(label='Your Name', max_length=60)
    email = forms.EmailField(label='Email Address',max_length=70)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label='Date of Birth')
    phone = forms.CharField(label='Phone Number',max_length=10)
    year = forms.IntegerField(label='Graduation Year', min_value=datetime.now().year, max_value=datetime.now().year+6)
    pronoun = forms.CharField(label='Preferred Pronouns', max_length=20)    
    color = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((False, 'No'), (True, 'Yes')))
    firstgen = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((False, 'No'), (True, 'Yes')))
    workstudy = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((False, 'No'), (True, 'Yes')))
    major = forms.CharField(label='Major', max_length=50)

    class Meta:
        model = Survey
        fields = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major') # Or a list of the fields that you want to include in your form
