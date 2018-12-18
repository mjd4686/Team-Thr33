from django import forms
from datetime import datetime
#----------------------------------------------------------------------
#                         Users
#----------------------------------------------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )

class ProfileForm(UserCreationForm):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')

    first_name = forms.CharField(label='First Name', max_length=60)
    last_name = forms.CharField(label='First Name', max_length=60)
    email = forms.EmailField(label='Email Address',max_length=70)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label='Date of Birth')
    #poc = forms.TypedChoiceField(label='Person of Color',coerce=lambda x: x =='True',
    #                               choices=((False, 'No'), (True, 'Yes')))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )
