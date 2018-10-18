from django import forms

#----------------------------------------------------------------------
#                         Form
#----------------------------------------------------------------------
from .models import Survey

class SurveyForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=200)
    year = forms.CharField(label='School Year', max_length=200)
    dob = forms.DateField(label='Date of birth')

    class Meta:
        model = Survey
        #fieds = ('post',)
        fields = ('name', 'year', 'dob') # Or a list of the fields that you want to include in your form
