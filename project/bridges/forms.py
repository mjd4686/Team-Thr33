from django import forms
from datetime import datetime
#----------------------------------------------------------------------
#                         Form
#----------------------------------------------------------------------
from .models import Survey

class SurveyForm(forms.ModelForm): 
    name = forms.CharField(label='Your Name', max_length=60)
    email = forms.EmailField(label='Email Address',max_length=70)
    phone = forms.CharField(label='Phone Number',max_length=10)
    year = forms.IntegerField(label='Graduation Year', min_value=datetime.now().year, max_value=datetime.now().year+6)
    pronoun = forms.CharField(label='Preferred Pronouns', max_length=20)    
    dob = forms.DateField(label='Date of Birth')
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
