from django import forms
from datetime import datetime
#----------------------------------------------------------------------
#                         People
#----------------------------------------------------------------------
from .models import People

class SurveyForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    name = forms.CharField(label='Your Name', max_length=60)
    email = forms.EmailField(label='Email Address',max_length=70)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label='Date of Birth')
    poc = forms.TypedChoiceField(label='Person of Color',coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')))


    class Meta:
        model = Survey
        fields = ('name', 'email', 'dob','poc', )
